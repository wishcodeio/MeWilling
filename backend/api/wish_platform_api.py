from flask import Blueprint, request, jsonify, render_template
from datetime import datetime
import sqlite3
import os
import json

wish_platform_bp = Blueprint('wish_platform', __name__, url_prefix='/api/wish_platform')

# 数据库文件路径
DB_PATH = 'data/wish_platform.db'

def init_db():
    """初始化数据库"""
    os.makedirs('data', exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 创建许愿表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT NOT NULL,
            status TEXT DEFAULT 'active',
            deadline DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            fulfilled_at TIMESTAMP,
            user_id TEXT DEFAULT 'default_user'
        )
    ''')
    
    # 创建许愿统计表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wish_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT DEFAULT 'default_user',
            total_wishes INTEGER DEFAULT 0,
            fulfilled_wishes INTEGER DEFAULT 0,
            active_wishes INTEGER DEFAULT 0,
            wish_power INTEGER DEFAULT 100,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """获取数据库连接"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def update_stats():
    """更新统计数据"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 计算统计数据
    cursor.execute('SELECT COUNT(*) as total FROM wishes WHERE user_id = ?', ('default_user',))
    total_wishes = cursor.fetchone()['total']
    
    cursor.execute('SELECT COUNT(*) as fulfilled FROM wishes WHERE user_id = ? AND status = ?', ('default_user', 'fulfilled'))
    fulfilled_wishes = cursor.fetchone()['fulfilled']
    
    cursor.execute('SELECT COUNT(*) as active FROM wishes WHERE user_id = ? AND status = ?', ('default_user', 'active'))
    active_wishes = cursor.fetchone()['active']
    
    # 计算愿力指数（基于实现率）
    wish_power = 100
    if total_wishes > 0:
        fulfillment_rate = fulfilled_wishes / total_wishes
        wish_power = min(100, max(50, int(fulfillment_rate * 100 + 50)))
    
    # 更新或插入统计数据
    cursor.execute('SELECT id FROM wish_stats WHERE user_id = ?', ('default_user',))
    existing = cursor.fetchone()
    
    if existing:
        cursor.execute('''
            UPDATE wish_stats 
            SET total_wishes = ?, fulfilled_wishes = ?, active_wishes = ?, 
                wish_power = ?, last_updated = CURRENT_TIMESTAMP
            WHERE user_id = ?
        ''', (total_wishes, fulfilled_wishes, active_wishes, wish_power, 'default_user'))
    else:
        cursor.execute('''
            INSERT INTO wish_stats (user_id, total_wishes, fulfilled_wishes, active_wishes, wish_power)
            VALUES (?, ?, ?, ?, ?)
        ''', ('default_user', total_wishes, fulfilled_wishes, active_wishes, wish_power))
    
    conn.commit()
    conn.close()

# 初始化数据库
init_db()

@wish_platform_bp.route('/wishes', methods=['GET'])
def get_wishes():
    """获取所有许愿"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, content, category, status, deadline, 
                   created_at, updated_at, fulfilled_at
            FROM wishes 
            WHERE user_id = ?
            ORDER BY created_at DESC
        ''', ('default_user',))
        
        wishes = []
        category_map = {
            'health': '🏥 健康',
            'love': '💕 愛情',
            'career': '💼 事業',
            'wealth': '💰 財富',
            'family': '👨‍👩‍👧‍👦 家庭',
            'study': '📚 學習',
            'travel': '✈️ 旅行',
            'spiritual': '🧘 靈性成長',
            'other': '🌈 其他'
        }
        
        for row in cursor.fetchall():
            wish = dict(row)
            wish['category_display'] = category_map.get(wish['category'], wish['category'])
            if wish['created_at']:
                wish['created_at'] = datetime.fromisoformat(wish['created_at'].replace('Z', '+00:00'))
            wishes.append(wish)
        
        conn.close()
        return jsonify({'success': True, 'wishes': wishes})
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@wish_platform_bp.route('/wishes', methods=['POST'])
def create_wish():
    """创建新许愿"""
    try:
        data = request.get_json()
        
        if not data or not data.get('title') or not data.get('content'):
            return jsonify({'success': False, 'message': '标题和内容不能为空'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO wishes (title, content, category, deadline, user_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data['title'],
            data['content'],
            data.get('category', 'other'),
            data.get('deadline'),
            'default_user'
        ))
        
        wish_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # 更新统计数据
        update_stats()
        
        return jsonify({
            'success': True, 
            'message': '许愿成功！愿你的梦想成真 ✨',
            'wish_id': wish_id
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@wish_platform_bp.route('/wishes/<int:wish_id>/status', methods=['POST'])
def update_wish_status(wish_id):
    """更新许愿状态"""
    try:
        data = request.get_json()
        status = data.get('status')
        
        if status not in ['active', 'fulfilled', 'progress', 'cancelled']:
            return jsonify({'success': False, 'message': '无效的状态'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 检查许愿是否存在
        cursor.execute('SELECT id FROM wishes WHERE id = ? AND user_id = ?', (wish_id, 'default_user'))
        if not cursor.fetchone():
            return jsonify({'success': False, 'message': '许愿不存在'}), 404
        
        # 更新状态
        fulfilled_at = datetime.now().isoformat() if status == 'fulfilled' else None
        cursor.execute('''
            UPDATE wishes 
            SET status = ?, updated_at = CURRENT_TIMESTAMP, fulfilled_at = ?
            WHERE id = ? AND user_id = ?
        ''', (status, fulfilled_at, wish_id, 'default_user'))
        
        conn.commit()
        conn.close()
        
        # 更新统计数据
        update_stats()
        
        status_messages = {
            'fulfilled': '恭喜！愿望已实现 🎉',
            'progress': '愿望进行中，继续加油 💪',
            'active': '愿望重新激活 ✨',
            'cancelled': '愿望已取消 😔'
        }
        
        return jsonify({
            'success': True, 
            'message': status_messages.get(status, '状态更新成功')
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@wish_platform_bp.route('/wishes/<int:wish_id>', methods=['DELETE'])
def delete_wish(wish_id):
    """删除许愿"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 检查许愿是否存在
        cursor.execute('SELECT id FROM wishes WHERE id = ? AND user_id = ?', (wish_id, 'default_user'))
        if not cursor.fetchone():
            return jsonify({'success': False, 'message': '许愿不存在'}), 404
        
        # 删除许愿
        cursor.execute('DELETE FROM wishes WHERE id = ? AND user_id = ?', (wish_id, 'default_user'))
        
        conn.commit()
        conn.close()
        
        # 更新统计数据
        update_stats()
        
        return jsonify({'success': True, 'message': '许愿已删除'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@wish_platform_bp.route('/stats', methods=['GET'])
def get_stats():
    """获取统计数据"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM wish_stats WHERE user_id = ?', ('default_user',))
        stats = cursor.fetchone()
        
        if not stats:
            # 如果没有统计数据，创建默认数据
            update_stats()
            cursor.execute('SELECT * FROM wish_stats WHERE user_id = ?', ('default_user',))
            stats = cursor.fetchone()
        
        conn.close()
        
        return jsonify({
            'success': True,
            'stats': dict(stats) if stats else {
                'total_wishes': 0,
                'fulfilled_wishes': 0,
                'active_wishes': 0,
                'wish_power': 100
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# 主页面路由（处理表单提交）
@wish_platform_bp.route('/', methods=['GET', 'POST'])
def wish_platform_page():
    """许愿平台主页面"""
    if request.method == 'POST':
        # 处理表单提交
        try:
            title = request.form.get('wish_title')
            content = request.form.get('wish_content')
            category = request.form.get('wish_category')
            deadline = request.form.get('wish_deadline')
            
            if not title or not content:
                return render_template('wish_platform.html', error='标题和内容不能为空')
            
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO wishes (title, content, category, deadline, user_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, content, category, deadline or None, 'default_user'))
            
            conn.commit()
            conn.close()
            
            # 更新统计数据
            update_stats()
            
            # 重定向到避免重复提交
            from flask import redirect, url_for
            return redirect(url_for('wish_platform.wish_platform_page'))
            
        except Exception as e:
            return render_template('wish_platform.html', error=f'提交失败：{str(e)}')
    
    # GET请求，显示页面
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 获取所有许愿
        cursor.execute('''
            SELECT id, title, content, category, status, deadline, 
                   created_at, updated_at, fulfilled_at
            FROM wishes 
            WHERE user_id = ?
            ORDER BY created_at DESC
        ''', ('default_user',))
        
        wishes = []
        category_map = {
            'health': '🏥 健康',
            'love': '💕 愛情',
            'career': '💼 事業',
            'wealth': '💰 財富',
            'family': '👨‍👩‍👧‍👦 家庭',
            'study': '📚 學習',
            'travel': '✈️ 旅行',
            'spiritual': '🧘 靈性成長',
            'other': '🌈 其他'
        }
        
        for row in cursor.fetchall():
            wish = dict(row)
            wish['category_display'] = category_map.get(wish['category'], wish['category'])
            if wish['created_at']:
                try:
                    wish['created_at'] = datetime.fromisoformat(wish['created_at'].replace('Z', '+00:00'))
                except:
                    wish['created_at'] = datetime.now()
            wishes.append(wish)
        
        # 获取统计数据
        cursor.execute('SELECT * FROM wish_stats WHERE user_id = ?', ('default_user',))
        stats = cursor.fetchone()
        
        if not stats:
            update_stats()
            cursor.execute('SELECT * FROM wish_stats WHERE user_id = ?', ('default_user',))
            stats = cursor.fetchone()
        
        conn.close()
        
        stats_dict = dict(stats) if stats else {
            'total_wishes': 0,
            'fulfilled_wishes': 0,
            'active_wishes': 0,
            'wish_power': 100
        }
        
        return render_template('wish_platform.html', 
                             wishes=wishes,
                             **stats_dict)
        
    except Exception as e:
        return render_template('wish_platform.html', 
                             error=f'加载数据失败：{str(e)}',
                             wishes=[],
                             total_wishes=0,
                             fulfilled_wishes=0,
                             active_wishes=0,
                             wish_power=100)
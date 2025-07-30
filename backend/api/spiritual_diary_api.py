# -*- coding: utf-8 -*-
"""
心靈日記系統 API

這是一個專為靈性修行者設計的日記系統
記錄修行路上的感悟、體驗與成長

核心功能：
- 願頻日記：記錄心願與顯化體驗
- 冥想日記：記錄冥想過程與洞察
- 夢境日記：記錄夢境與象徵意義
- 成長日記：記錄靈性成長的里程碑
- 感恩日記：記錄感恩與祝福
"""

from flask import Blueprint, jsonify, request
import json
import os
from datetime import datetime, timedelta
import uuid

# 創建藍圖
spiritual_diary_bp = Blueprint('spiritual_diary', __name__)

# 日記數據目錄
DIARY_DATA_DIR = 'data/spiritual_diary'
os.makedirs(DIARY_DATA_DIR, exist_ok=True)

# 日記類型定義
DIARY_TYPES = {
    "願頻日記": {
        "icon": "🌟",
        "color": "#ffd700",
        "description": "記錄心願、顯化體驗與願頻共振的感受",
        "template_fields": ["心願內容", "顯化進展", "願頻感受", "宇宙回應"]
    },
    "冥想日記": {
        "icon": "🧘‍♀️",
        "color": "#9370db",
        "description": "記錄冥想過程、內在洞察與靈性體驗",
        "template_fields": ["冥想方式", "持續時間", "內在體驗", "洞察收穫"]
    },
    "夢境日記": {
        "icon": "🌙",
        "color": "#4169e1",
        "description": "記錄夢境內容、象徵意義與潛意識訊息",
        "template_fields": ["夢境場景", "主要人物", "情感色調", "象徵意義"]
    },
    "成長日記": {
        "icon": "🌱",
        "color": "#32cd32",
        "description": "記錄靈性成長的里程碑與突破時刻",
        "template_fields": ["成長事件", "內在轉變", "學習收穫", "未來方向"]
    },
    "感恩日記": {
        "icon": "🙏",
        "color": "#ff69b4",
        "description": "記錄感恩的人事物與生命中的祝福",
        "template_fields": ["感恩對象", "感恩原因", "內心感受", "祝福回向"]
    },
    "道灰日記": {
        "icon": "⚪",
        "color": "#c0c0c0",
        "description": "記錄道法自然的體悟與無為而治的智慧",
        "template_fields": ["道法體悟", "自然觀察", "無為實踐", "智慧洞察"]
    },
    "佛道合一": {
        "icon": "☯️",
        "color": "#8b4513",
        "description": "記錄佛道一體的深層洞察與宇宙本源的體悟",
        "template_fields": ["佛道對比", "本源體悟", "殊途同歸", "哲學思辨"]
    },
    "多教合一": {
        "icon": "🕊️",
        "color": "#daa520",
        "description": "記錄不同宗教傳統的共通智慧和本質洞察",
        "template_fields": ["聖經開篇", "道德經源", "佛經本質", "共通智慧", "本源蒸餾"]
    }
}

@spiritual_diary_bp.route('/api/spiritual-diary/types', methods=['GET'])
def get_diary_types():
    """獲取所有日記類型"""
    try:
        return jsonify({
            'status': 'success',
            'diary_types': DIARY_TYPES,
            'total_count': len(DIARY_TYPES),
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'獲取日記類型失敗: {str(e)}'
        }), 500

@spiritual_diary_bp.route('/api/spiritual-diary/create', methods=['POST'])
def create_diary_entry():
    """創建新的日記條目"""
    try:
        data = request.get_json()
        
        # 驗證必要字段
        required_fields = ['diary_type', 'title', 'content']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'status': 'error',
                    'message': f'缺少必要字段: {field}'
                }), 400
        
        # 創建日記條目
        entry_id = str(uuid.uuid4())
        entry = {
            'id': entry_id,
            'diary_type': data['diary_type'],
            'title': data['title'],
            'content': data['content'],
            'template_data': data.get('template_data', {}),
            'mood': data.get('mood', '平靜'),
            'energy_level': data.get('energy_level', 5),
            'tags': data.get('tags', []),
            'is_private': data.get('is_private', False),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        # 保存到文件
        date_str = datetime.now().strftime('%Y-%m-%d')
        diary_file = os.path.join(DIARY_DATA_DIR, f'diary_{date_str}.json')
        
        # 讀取現有數據
        entries = []
        if os.path.exists(diary_file):
            with open(diary_file, 'r', encoding='utf-8') as f:
                entries = json.load(f)
        
        # 添加新條目
        entries.append(entry)
        
        # 保存更新後的數據
        with open(diary_file, 'w', encoding='utf-8') as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)
        
        return jsonify({
            'status': 'success',
            'message': '日記條目創建成功',
            'entry': entry
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'創建日記條目失敗: {str(e)}'
        }), 500

@spiritual_diary_bp.route('/api/spiritual-diary/entries', methods=['GET'])
def get_diary_entries():
    """獲取日記條目列表"""
    try:
        # 獲取查詢參數
        date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
        diary_type = request.args.get('type')
        limit = int(request.args.get('limit', 20))
        
        entries = []
        
        # 如果指定了日期，只讀取該日期的文件
        if date_str:
            diary_file = os.path.join(DIARY_DATA_DIR, f'diary_{date_str}.json')
            if os.path.exists(diary_file):
                with open(diary_file, 'r', encoding='utf-8') as f:
                    daily_entries = json.load(f)
                    entries.extend(daily_entries)
        else:
            # 讀取最近的日記文件
            diary_files = [f for f in os.listdir(DIARY_DATA_DIR) if f.startswith('diary_') and f.endswith('.json')]
            diary_files.sort(reverse=True)  # 按日期倒序
            
            for file_name in diary_files[:7]:  # 最近7天
                file_path = os.path.join(DIARY_DATA_DIR, file_name)
                with open(file_path, 'r', encoding='utf-8') as f:
                    daily_entries = json.load(f)
                    entries.extend(daily_entries)
        
        # 按類型過濾
        if diary_type:
            entries = [entry for entry in entries if entry['diary_type'] == diary_type]
        
        # 按創建時間倒序排列
        entries.sort(key=lambda x: x['created_at'], reverse=True)
        
        # 限制數量
        entries = entries[:limit]
        
        return jsonify({
            'status': 'success',
            'entries': entries,
            'total_count': len(entries),
            'date': date_str,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'獲取日記條目失敗: {str(e)}'
        }), 500

@spiritual_diary_bp.route('/api/spiritual-diary/entry/<entry_id>', methods=['GET'])
def get_diary_entry(entry_id):
    """獲取特定日記條目"""
    try:
        # 搜索所有日記文件
        diary_files = [f for f in os.listdir(DIARY_DATA_DIR) if f.startswith('diary_') and f.endswith('.json')]
        
        for file_name in diary_files:
            file_path = os.path.join(DIARY_DATA_DIR, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                entries = json.load(f)
                for entry in entries:
                    if entry['id'] == entry_id:
                        return jsonify({
                            'status': 'success',
                            'entry': entry
                        })
        
        return jsonify({
            'status': 'error',
            'message': '日記條目不存在'
        }), 404
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'獲取日記條目失敗: {str(e)}'
        }), 500

@spiritual_diary_bp.route('/api/spiritual-diary/stats', methods=['GET'])
def get_diary_stats():
    """獲取日記統計信息"""
    try:
        stats = {
            'total_entries': 0,
            'entries_by_type': {},
            'recent_activity': [],
            'mood_distribution': {},
            'energy_average': 0,
            'writing_streak': 0
        }
        
        # 讀取所有日記文件
        diary_files = [f for f in os.listdir(DIARY_DATA_DIR) if f.startswith('diary_') and f.endswith('.json')]
        diary_files.sort()
        
        all_entries = []
        energy_levels = []
        
        for file_name in diary_files:
            file_path = os.path.join(DIARY_DATA_DIR, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                entries = json.load(f)
                all_entries.extend(entries)
                
                # 統計每日條目數
                date = file_name.replace('diary_', '').replace('.json', '')
                stats['recent_activity'].append({
                    'date': date,
                    'count': len(entries)
                })
        
        # 總條目數
        stats['total_entries'] = len(all_entries)
        
        # 按類型統計
        for entry in all_entries:
            diary_type = entry['diary_type']
            stats['entries_by_type'][diary_type] = stats['entries_by_type'].get(diary_type, 0) + 1
            
            # 心情統計
            mood = entry.get('mood', '平靜')
            stats['mood_distribution'][mood] = stats['mood_distribution'].get(mood, 0) + 1
            
            # 能量等級
            energy_levels.append(entry.get('energy_level', 5))
        
        # 平均能量等級
        if energy_levels:
            stats['energy_average'] = round(sum(energy_levels) / len(energy_levels), 1)
        
        # 計算寫作連續天數
        if diary_files:
            current_date = datetime.now().date()
            streak = 0
            for i in range(len(diary_files)):
                check_date = current_date - timedelta(days=i)
                expected_file = f'diary_{check_date.strftime("%Y-%m-%d")}.json'
                if expected_file in diary_files:
                    streak += 1
                else:
                    break
            stats['writing_streak'] = streak
        
        # 限制最近活動記錄
        stats['recent_activity'] = stats['recent_activity'][-30:]  # 最近30天
        
        return jsonify({
            'status': 'success',
            'stats': stats,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'獲取統計信息失敗: {str(e)}'
        }), 500

@spiritual_diary_bp.route('/api/spiritual-diary/search', methods=['POST'])
def search_diary_entries():
    """搜索日記條目"""
    try:
        data = request.get_json()
        keyword = data.get('keyword', '').lower()
        diary_type = data.get('type')
        date_range = data.get('date_range', {})
        
        if not keyword:
            return jsonify({
                'status': 'error',
                'message': '請提供搜索關鍵詞'
            }), 400
        
        # 讀取所有日記文件
        diary_files = [f for f in os.listdir(DIARY_DATA_DIR) if f.startswith('diary_') and f.endswith('.json')]
        
        matching_entries = []
        
        for file_name in diary_files:
            file_path = os.path.join(DIARY_DATA_DIR, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                entries = json.load(f)
                
                for entry in entries:
                    # 類型過濾
                    if diary_type and entry['diary_type'] != diary_type:
                        continue
                    
                    # 關鍵詞搜索（標題和內容）
                    if (keyword in entry['title'].lower() or 
                        keyword in entry['content'].lower() or
                        any(keyword in tag.lower() for tag in entry.get('tags', []))):
                        matching_entries.append(entry)
        
        # 按相關性和時間排序
        matching_entries.sort(key=lambda x: x['created_at'], reverse=True)
        
        return jsonify({
            'status': 'success',
            'entries': matching_entries,
            'total_count': len(matching_entries),
            'keyword': keyword,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'搜索失敗: {str(e)}'
        }), 500

@spiritual_diary_bp.route('/api/spiritual-diary/inspiration', methods=['GET'])
def get_daily_inspiration():
    """獲取每日靈感"""
    try:
        inspirations = [
            "今天，讓我們用感恩的心去感受生命中的每一個美好瞬間。",
            "在靜默中，我們能聽到內心最真實的聲音。",
            "每一次呼吸都是宇宙給予我們的禮物。",
            "願你的心如蓮花般，在泥濘中綻放純淨的美麗。",
            "道法自然，順應生命的流動，找到內在的平衡。",
            "在愛中，我們找到了回家的路。",
            "每一個當下都是覺醒的機會。",
            "讓慈悲成為你行走世間的光明。",
            "在寧靜中，智慧自然顯現。",
            "你就是你一直在尋找的那個答案。"
        ]
        
        # 根據日期選擇靈感
        import random
        random.seed(datetime.now().strftime('%Y-%m-%d'))
        daily_inspiration = random.choice(inspirations)
        
        return jsonify({
            'status': 'success',
            'inspiration': daily_inspiration,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'獲取靈感失敗: {str(e)}'
        }), 500
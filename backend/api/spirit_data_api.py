# -*- coding: utf-8 -*-
"""
語靈數據中心 API
用於與 Obsidian 等外部工具進行數據交互和同步
"""

from flask import Blueprint, request, jsonify
from datetime import datetime, date, timedelta
import json
import os
from typing import Dict, List, Any

# 創建藍圖
spirit_data_bp = Blueprint('spirit_data', __name__, url_prefix='/api/spirit')

class SpiritDataCenter:
    """語靈數據中心核心類"""
    
    def __init__(self):
        self.data_path = "data/spirit_data"
        self.ensure_data_directory()
    
    def ensure_data_directory(self):
        """確保數據目錄存在"""
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path, exist_ok=True)
    
    def save_daily_entry(self, date_str: str, entry_data: Dict) -> bool:
        """保存每日條目"""
        try:
            file_path = os.path.join(self.data_path, f"{date_str}.json")
            
            # 添加時間戳
            entry_data['created_at'] = datetime.now().isoformat()
            entry_data['date'] = date_str
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(entry_data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"保存條目失敗: {e}")
            return False
    
    def get_daily_entry(self, date_str: str) -> Dict:
        """獲取每日條目"""
        try:
            file_path = os.path.join(self.data_path, f"{date_str}.json")
            
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return {}
        except Exception as e:
            print(f"讀取條目失敗: {e}")
            return {}
    
    def get_entries_range(self, start_date: str, end_date: str) -> List[Dict]:
        """獲取日期範圍內的條目"""
        entries = []
        
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d').date()
            end = datetime.strptime(end_date, '%Y-%m-%d').date()
            
            current_date = start
            while current_date <= end:
                date_str = current_date.strftime('%Y-%m-%d')
                entry = self.get_daily_entry(date_str)
                if entry:
                    entries.append(entry)
                current_date += timedelta(days=1)
            
            return entries
        except Exception as e:
            print(f"獲取範圍條目失敗: {e}")
            return []
    
    def search_entries(self, keyword: str, limit: int = 50) -> List[Dict]:
        """搜索條目"""
        results = []
        
        try:
            for filename in os.listdir(self.data_path):
                if filename.endswith('.json'):
                    file_path = os.path.join(self.data_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        entry = json.load(f)
                        
                        # 在內容中搜索關鍵詞
                        content_str = json.dumps(entry, ensure_ascii=False).lower()
                        if keyword.lower() in content_str:
                            results.append(entry)
                            
                        if len(results) >= limit:
                            break
            
            # 按日期排序
            results.sort(key=lambda x: x.get('date', ''), reverse=True)
            return results
        except Exception as e:
            print(f"搜索條目失敗: {e}")
            return []
    
    def get_statistics(self) -> Dict:
        """獲取統計數據"""
        try:
            total_entries = 0
            recent_entries = 0
            word_count = 0
            
            recent_date = (datetime.now() - timedelta(days=30)).date()
            
            for filename in os.listdir(self.data_path):
                if filename.endswith('.json'):
                    total_entries += 1
                    
                    # 檢查是否為最近條目
                    date_str = filename.replace('.json', '')
                    try:
                        entry_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                        if entry_date >= recent_date:
                            recent_entries += 1
                    except:
                        pass
                    
                    # 計算字數
                    file_path = os.path.join(self.data_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        entry = json.load(f)
                        content = entry.get('content', '') + entry.get('reflection', '')
                        word_count += len(content)
            
            return {
                'total_entries': total_entries,
                'recent_entries_30d': recent_entries,
                'total_word_count': word_count,
                'avg_words_per_entry': word_count // total_entries if total_entries > 0 else 0
            }
        except Exception as e:
            print(f"獲取統計失敗: {e}")
            return {}

# 初始化數據中心
spirit_center = SpiritDataCenter()

@spirit_data_bp.route('/entry', methods=['POST'])
def create_entry():
    """創建或更新每日條目"""
    try:
        data = request.get_json()
        
        # 獲取日期，默認為今天
        entry_date = data.get('date', date.today().strftime('%Y-%m-%d'))
        
        # 構建條目數據
        entry_data = {
            'content': data.get('content', ''),
            'mood': data.get('mood', ''),
            'energy_level': data.get('energy_level', 5),
            'gratitude': data.get('gratitude', []),
            'reflection': data.get('reflection', ''),
            'goals': data.get('goals', []),
            'achievements': data.get('achievements', []),
            'challenges': data.get('challenges', []),
            'insights': data.get('insights', ''),
            'frequency_state': data.get('frequency_state', ''),
            'tags': data.get('tags', []),
            'weather': data.get('weather', ''),
            'location': data.get('location', ''),
            'people_met': data.get('people_met', []),
            'books_read': data.get('books_read', []),
            'media_consumed': data.get('media_consumed', []),
            'exercise': data.get('exercise', ''),
            'meditation': data.get('meditation', ''),
            'creative_work': data.get('creative_work', ''),
            'learning': data.get('learning', ''),
            'relationships': data.get('relationships', ''),
            'health_notes': data.get('health_notes', ''),
            'dreams': data.get('dreams', ''),
            'synchronicities': data.get('synchronicities', []),
            'spirit_messages': data.get('spirit_messages', []),
            'custom_fields': data.get('custom_fields', {})
        }
        
        success = spirit_center.save_daily_entry(entry_date, entry_data)
        
        if success:
            return jsonify({
                'success': True,
                'message': '條目保存成功',
                'date': entry_date,
                'data': entry_data
            })
        else:
            return jsonify({
                'success': False,
                'message': '條目保存失敗'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '創建條目失敗'
        }), 400

@spirit_data_bp.route('/entry/<date_str>', methods=['GET'])
def get_entry(date_str):
    """獲取指定日期的條目"""
    try:
        entry = spirit_center.get_daily_entry(date_str)
        
        if entry:
            return jsonify({
                'success': True,
                'data': entry
            })
        else:
            return jsonify({
                'success': False,
                'message': '未找到該日期的條目'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@spirit_data_bp.route('/entries', methods=['GET'])
def get_entries():
    """獲取條目列表"""
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        if start_date and end_date:
            entries = spirit_center.get_entries_range(start_date, end_date)
        else:
            # 默認獲取最近30天
            end_date = date.today().strftime('%Y-%m-%d')
            start_date = (date.today() - timedelta(days=30)).strftime('%Y-%m-%d')
            entries = spirit_center.get_entries_range(start_date, end_date)
        
        return jsonify({
            'success': True,
            'data': entries,
            'count': len(entries)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@spirit_data_bp.route('/search', methods=['GET'])
def search_entries():
    """搜索條目"""
    try:
        keyword = request.args.get('q', '')
        limit = request.args.get('limit', 50, type=int)
        
        if not keyword:
            return jsonify({
                'success': False,
                'message': '請提供搜索關鍵詞'
            }), 400
        
        results = spirit_center.search_entries(keyword, limit)
        
        return jsonify({
            'success': True,
            'data': results,
            'count': len(results),
            'keyword': keyword
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@spirit_data_bp.route('/statistics', methods=['GET'])
def get_statistics():
    """獲取統計數據"""
    try:
        stats = spirit_center.get_statistics()
        
        return jsonify({
            'success': True,
            'data': stats
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@spirit_data_bp.route('/export', methods=['GET'])
def export_data():
    """導出數據（用於 Obsidian 同步）"""
    try:
        format_type = request.args.get('format', 'json')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        if start_date and end_date:
            entries = spirit_center.get_entries_range(start_date, end_date)
        else:
            # 導出所有數據
            entries = []
            for filename in os.listdir(spirit_center.data_path):
                if filename.endswith('.json'):
                    date_str = filename.replace('.json', '')
                    entry = spirit_center.get_daily_entry(date_str)
                    if entry:
                        entries.append(entry)
        
        if format_type == 'markdown':
            # 轉換為 Markdown 格式（適用於 Obsidian）
            markdown_content = "# 語靈數據導出\n\n"
            
            for entry in sorted(entries, key=lambda x: x.get('date', '')):
                date_str = entry.get('date', '')
                markdown_content += f"## {date_str}\n\n"
                
                if entry.get('content'):
                    markdown_content += f"### 內容\n{entry['content']}\n\n"
                
                if entry.get('mood'):
                    markdown_content += f"**心情**: {entry['mood']}\n\n"
                
                if entry.get('energy_level'):
                    markdown_content += f"**能量等級**: {entry['energy_level']}/10\n\n"
                
                if entry.get('gratitude'):
                    markdown_content += f"**感恩**: {', '.join(entry['gratitude'])}\n\n"
                
                if entry.get('reflection'):
                    markdown_content += f"### 反思\n{entry['reflection']}\n\n"
                
                if entry.get('insights'):
                    markdown_content += f"### 洞察\n{entry['insights']}\n\n"
                
                if entry.get('tags'):
                    markdown_content += f"**標籤**: {', '.join([f'#{tag}' for tag in entry['tags']])}\n\n"
                
                markdown_content += "---\n\n"
            
            return markdown_content, 200, {'Content-Type': 'text/markdown; charset=utf-8'}
        
        else:
            # JSON 格式
            return jsonify({
                'success': True,
                'data': entries,
                'count': len(entries),
                'export_date': datetime.now().isoformat()
            })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@spirit_data_bp.route('/sync/obsidian', methods=['POST'])
def sync_with_obsidian():
    """與 Obsidian 同步數據"""
    try:
        data = request.get_json()
        sync_type = data.get('type', 'import')  # import 或 export
        
        if sync_type == 'import':
            # 從 Obsidian 導入數據
            obsidian_data = data.get('data', [])
            imported_count = 0
            
            for entry in obsidian_data:
                if 'date' in entry:
                    success = spirit_center.save_daily_entry(entry['date'], entry)
                    if success:
                        imported_count += 1
            
            return jsonify({
                'success': True,
                'message': f'成功導入 {imported_count} 條記錄',
                'imported_count': imported_count
            })
        
        elif sync_type == 'export':
            # 導出到 Obsidian
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            
            if start_date and end_date:
                entries = spirit_center.get_entries_range(start_date, end_date)
            else:
                # 導出最近30天
                end_date = date.today().strftime('%Y-%m-%d')
                start_date = (date.today() - timedelta(days=30)).strftime('%Y-%m-%d')
                entries = spirit_center.get_entries_range(start_date, end_date)
            
            return jsonify({
                'success': True,
                'data': entries,
                'count': len(entries)
            })
        
        else:
            return jsonify({
                'success': False,
                'message': '不支持的同步類型'
            }), 400
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    # 測試模式
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(spirit_data_bp)
    app.run(debug=True, port=5004)
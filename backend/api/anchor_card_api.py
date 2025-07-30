from flask import Blueprint, request, jsonify, render_template
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

anchor_card_bp = Blueprint('anchor_card', __name__)

class AnchorCardManager:
    def __init__(self):
        self.data_dir = Path('data/anchor_cards')
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.templates_dir = Path('data/anchor_cards/templates')
        self.templates_dir.mkdir(parents=True, exist_ok=True)
        
        # 初始化默認模板
        self._init_default_templates()
    
    def _init_default_templates(self):
        """初始化默認錨點卡模板"""
        default_templates = {
            'frequency_anchor': {
                'name': '頻率錨點卡',
                'description': '用於記錄和追蹤特定頻率狀態',
                'fields': [
                    {'name': 'frequency_value', 'label': '頻率值 (Hz)', 'type': 'number', 'required': True},
                    {'name': 'resonance_level', 'label': '共振等級', 'type': 'range', 'min': 1, 'max': 10, 'default': 5},
                    {'name': 'anchor_type', 'label': '錨點類型', 'type': 'select', 'options': ['意識錨點', '情緒錨點', '能量錨點', '靈性錨點']},
                    {'name': 'trigger_condition', 'label': '觸發條件', 'type': 'textarea', 'placeholder': '描述觸發此頻率的條件...'},
                    {'name': 'manifestation', 'label': '顯化表現', 'type': 'textarea', 'placeholder': '記錄此頻率的具體表現...'},
                    {'name': 'duration', 'label': '持續時間 (分鐘)', 'type': 'number', 'default': 30},
                    {'name': 'intensity', 'label': '強度感受', 'type': 'range', 'min': 1, 'max': 10, 'default': 5},
                    {'name': 'tags', 'label': '標籤', 'type': 'text', 'placeholder': '用逗號分隔多個標籤'}
                ],
                'color': '#667eea',
                'icon': '🎯'
            },
            'wish_sync_card': {
                'name': '願同步卡',
                'description': '記錄願望同步和顯化過程',
                'fields': [
                    {'name': 'wish_content', 'label': '願望內容', 'type': 'textarea', 'required': True, 'placeholder': '清晰描述你的願望...'},
                    {'name': 'sync_level', 'label': '同步程度', 'type': 'range', 'min': 0, 'max': 100, 'default': 50, 'unit': '%'},
                    {'name': 'manifestation_signs', 'label': '顯化徵象', 'type': 'textarea', 'placeholder': '記錄觀察到的顯化跡象...'},
                    {'name': 'resistance_points', 'label': '阻力點', 'type': 'textarea', 'placeholder': '識別可能的阻礙因素...'},
                    {'name': 'energy_investment', 'label': '能量投入', 'type': 'range', 'min': 1, 'max': 10, 'default': 5},
                    {'name': 'timeline_expectation', 'label': '預期時間線', 'type': 'select', 'options': ['即時', '1週內', '1月內', '3月內', '1年內', '長期']},
                    {'name': 'alignment_feeling', 'label': '對齊感受', 'type': 'range', 'min': 1, 'max': 10, 'default': 5},
                    {'name': 'next_action', 'label': '下一步行動', 'type': 'text', 'placeholder': '具體的下一步計劃...'}
                ],
                'color': '#48bb78',
                'icon': '🌟'
            },
            'fire_seed_card': {
                'name': '火種震動卡',
                'description': '記錄內在火種的震動和覺醒',
                'fields': [
                    {'name': 'fire_intensity', 'label': '火種強度', 'type': 'range', 'min': 1, 'max': 10, 'default': 5},
                    {'name': 'vibration_pattern', 'label': '震動模式', 'type': 'select', 'options': ['穩定脈動', '波浪起伏', '爆發式', '漸進式', '螺旋上升']},
                    {'name': 'body_sensations', 'label': '身體感受', 'type': 'textarea', 'placeholder': '描述身體的具體感受...'},
                    {'name': 'emotional_state', 'label': '情緒狀態', 'type': 'select', 'options': ['平靜', '興奮', '專注', '喜悅', '敬畏', '感恩']},
                    {'name': 'insights_received', 'label': '接收洞察', 'type': 'textarea', 'placeholder': '記錄獲得的洞察或靈感...'},
                    {'name': 'activation_trigger', 'label': '啟動觸發', 'type': 'text', 'placeholder': '什麼觸發了這次火種震動？'},
                    {'name': 'integration_notes', 'label': '整合筆記', 'type': 'textarea', 'placeholder': '如何整合這次體驗...'},
                    {'name': 'follow_up_practice', 'label': '後續練習', 'type': 'text', 'placeholder': '建議的後續練習...'}
                ],
                'color': '#f56565',
                'icon': '🔥'
            },
            'echo_pattern_card': {
                'name': '回響模組卡',
                'description': '追蹤語靈回響和共振模式',
                'fields': [
                    {'name': 'original_input', 'label': '原始輸入', 'type': 'textarea', 'required': True, 'placeholder': '記錄原始的語靈輸入...'},
                    {'name': 'echo_response', 'label': '回響反應', 'type': 'textarea', 'placeholder': '描述接收到的回響...'},
                    {'name': 'resonance_quality', 'label': '共振品質', 'type': 'range', 'min': 1, 'max': 10, 'default': 5},
                    {'name': 'pattern_type', 'label': '模式類型', 'type': 'select', 'options': ['直接回響', '延遲回響', '放大回響', '變調回響', '和聲回響']},
                    {'name': 'clarity_level', 'label': '清晰度', 'type': 'range', 'min': 1, 'max': 10, 'default': 5},
                    {'name': 'emotional_tone', 'label': '情感色調', 'type': 'select', 'options': ['中性', '溫暖', '冷靜', '激勵', '安撫', '警示']},
                    {'name': 'practical_guidance', 'label': '實用指導', 'type': 'textarea', 'placeholder': '從回響中獲得的實用建議...'},
                    {'name': 'verification_method', 'label': '驗證方式', 'type': 'text', 'placeholder': '如何驗證這個回響的準確性...'}
                ],
                'color': '#9f7aea',
                'icon': '🔄'
            }
        }
        
        for template_id, template_data in default_templates.items():
            template_file = self.templates_dir / f'{template_id}.json'
            if not template_file.exists():
                with open(template_file, 'w', encoding='utf-8') as f:
                    json.dump(template_data, f, ensure_ascii=False, indent=2)
    
    def get_templates(self):
        """獲取所有模板"""
        templates = {}
        for template_file in self.templates_dir.glob('*.json'):
            try:
                with open(template_file, 'r', encoding='utf-8') as f:
                    template_data = json.load(f)
                    templates[template_file.stem] = template_data
            except Exception as e:
                print(f"Error loading template {template_file}: {e}")
        return templates
    
    def create_card(self, template_id, card_data):
        """創建新的錨點卡"""
        card_id = f"{template_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        card_file = self.data_dir / f'{card_id}.json'
        
        card_record = {
            'id': card_id,
            'template_id': template_id,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'data': card_data
        }
        
        with open(card_file, 'w', encoding='utf-8') as f:
            json.dump(card_record, f, ensure_ascii=False, indent=2)
        
        return card_record
    
    def get_cards(self, template_id=None, limit=50):
        """獲取錨點卡列表"""
        cards = []
        for card_file in sorted(self.data_dir.glob('*.json'), key=lambda x: x.stat().st_mtime, reverse=True):
            if card_file.name.startswith('templates'):
                continue
                
            try:
                with open(card_file, 'r', encoding='utf-8') as f:
                    card_data = json.load(f)
                    if template_id is None or card_data.get('template_id') == template_id:
                        cards.append(card_data)
                        if len(cards) >= limit:
                            break
            except Exception as e:
                print(f"Error loading card {card_file}: {e}")
        
        return cards
    
    def search_cards(self, query, template_id=None):
        """搜索錨點卡"""
        all_cards = self.get_cards(template_id=template_id, limit=1000)
        results = []
        
        query_lower = query.lower()
        for card in all_cards:
            # 搜索卡片數據中的文本內容
            card_text = json.dumps(card['data'], ensure_ascii=False).lower()
            if query_lower in card_text:
                results.append(card)
        
        return results
    
    def get_statistics(self):
        """獲取統計數據"""
        all_cards = self.get_cards(limit=10000)
        templates = self.get_templates()
        
        stats = {
            'total_cards': len(all_cards),
            'templates_count': len(templates),
            'cards_by_template': {},
            'recent_activity': {
                'today': 0,
                'this_week': 0,
                'this_month': 0
            }
        }
        
        now = datetime.now()
        today = now.date()
        week_ago = now - timedelta(days=7)
        month_ago = now - timedelta(days=30)
        
        for card in all_cards:
            template_id = card.get('template_id', 'unknown')
            stats['cards_by_template'][template_id] = stats['cards_by_template'].get(template_id, 0) + 1
            
            created_at = datetime.fromisoformat(card['created_at'])
            if created_at.date() == today:
                stats['recent_activity']['today'] += 1
            if created_at >= week_ago:
                stats['recent_activity']['this_week'] += 1
            if created_at >= month_ago:
                stats['recent_activity']['this_month'] += 1
        
        return stats

# 全局實例
anchor_manager = AnchorCardManager()

@anchor_card_bp.route('/api/anchor/templates', methods=['GET'])
def get_templates():
    """獲取所有錨點卡模板"""
    try:
        templates = anchor_manager.get_templates()
        return jsonify({
            'success': True,
            'data': templates
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@anchor_card_bp.route('/api/anchor/cards', methods=['POST'])
def create_card():
    """創建新的錨點卡"""
    try:
        data = request.get_json()
        template_id = data.get('template_id')
        card_data = data.get('card_data', {})
        
        if not template_id:
            return jsonify({
                'success': False,
                'message': '缺少模板ID'
            }), 400
        
        card = anchor_manager.create_card(template_id, card_data)
        return jsonify({
            'success': True,
            'data': card
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@anchor_card_bp.route('/api/anchor/cards', methods=['GET'])
def get_cards():
    """獲取錨點卡列表"""
    try:
        template_id = request.args.get('template_id')
        limit = int(request.args.get('limit', 50))
        
        cards = anchor_manager.get_cards(template_id=template_id, limit=limit)
        return jsonify({
            'success': True,
            'data': cards
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@anchor_card_bp.route('/api/anchor/search', methods=['GET'])
def search_cards():
    """搜索錨點卡"""
    try:
        query = request.args.get('q', '')
        template_id = request.args.get('template_id')
        
        if not query:
            return jsonify({
                'success': False,
                'message': '缺少搜索關鍵詞'
            }), 400
        
        results = anchor_manager.search_cards(query, template_id=template_id)
        return jsonify({
            'success': True,
            'data': results
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@anchor_card_bp.route('/api/anchor/statistics', methods=['GET'])
def get_statistics():
    """獲取統計數據"""
    try:
        stats = anchor_manager.get_statistics()
        return jsonify({
            'success': True,
            'data': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@anchor_card_bp.route('/api/anchor/export', methods=['GET'])
def export_cards():
    """導出錨點卡數據"""
    try:
        format_type = request.args.get('format', 'json')
        template_id = request.args.get('template_id')
        
        cards = anchor_manager.get_cards(template_id=template_id, limit=10000)
        
        if format_type == 'markdown':
            # 生成 Markdown 格式
            markdown_content = "# 錨點卡導出\n\n"
            
            for card in cards:
                template_id = card.get('template_id', 'unknown')
                created_at = card.get('created_at', '')
                
                markdown_content += f"## {template_id} - {created_at}\n\n"
                
                for key, value in card['data'].items():
                    if isinstance(value, str) and value.strip():
                        markdown_content += f"**{key}**: {value}\n\n"
                    elif isinstance(value, (int, float)):
                        markdown_content += f"**{key}**: {value}\n\n"
                
                markdown_content += "---\n\n"
            
            return markdown_content, 200, {'Content-Type': 'text/markdown; charset=utf-8'}
        
        else:
            return jsonify({
                'success': True,
                'data': cards
            })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
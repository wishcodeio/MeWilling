from flask import Blueprint, request, jsonify, current_app
import json
import os
from datetime import datetime, timedelta
import uuid
from collections import defaultdict
import random

card_learning_bp = Blueprint('card_learning', __name__)

class CardLearningSystem:
    def __init__(self):
        self.data_dir = 'data/card_learning'
        self.ensure_directories()
        
        # 中醫脈絡穴位映射
        self.meridian_points = {
            '心經': ['神門', '少海', '靈道', '通里', '陰郄'],
            '肝經': ['太衝', '行間', '大敦', '中封', '蠡溝'],
            '腎經': ['湧泉', '太溪', '復溜', '照海', '然谷'],
            '脾經': ['太白', '公孫', '三陰交', '陰陵泉', '血海'],
            '肺經': ['太淵', '魚際', '少商', '尺澤', '孔最'],
            '胃經': ['足三里', '豐隆', '解溪', '衝陽', '內庭'],
            '膽經': ['陽陵泉', '懸鐘', '丘墟', '足臨泣', '俠溪'],
            '膀胱經': ['委中', '崑崙', '申脈', '至陰', '束骨']
        }
        
        # 腦神經網路區域
        self.neural_regions = {
            '前額葉': {'功能': '執行控制', '關聯': ['決策', '計劃', '抽象思維']},
            '海馬體': {'功能': '記憶形成', '關聯': ['長期記憶', '空間記憶', '情景記憶']},
            '杏仁核': {'功能': '情緒處理', '關聯': ['恐懼', '愉悅', '情緒記憶']},
            '頂葉': {'功能': '感覺整合', '關聯': ['空間感知', '身體意識', '注意力']},
            '顳葉': {'功能': '語言處理', '關聯': ['語義記憶', '聽覺處理', '語言理解']},
            '枕葉': {'功能': '視覺處理', '關聯': ['視覺記憶', '圖像識別', '空間視覺']},
            '小腦': {'功能': '運動協調', '關聯': ['程序記憶', '平衡', '精細動作']},
            '腦幹': {'功能': '基本生命', '關聯': ['覺醒', '呼吸', '心跳']}
        }
        
    def ensure_directories(self):
        dirs = [
            self.data_dir,
            f'{self.data_dir}/cards',
            f'{self.data_dir}/learning_paths',
            f'{self.data_dir}/neural_maps',
            f'{self.data_dir}/meridian_flows'
        ]
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
    
    def create_learning_card(self, card_data):
        """創建學習卡片，結合中醫脈絡和神經網路"""
        card_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        # 自動分配脈絡穴位
        meridian = self._assign_meridian(card_data.get('content_type', 'general'))
        acupoint = self._select_acupoint(meridian, card_data.get('difficulty', 'medium'))
        
        # 自動分配神經區域
        neural_region = self._assign_neural_region(card_data.get('learning_type', 'conceptual'))
        
        card = {
            'id': card_id,
            'title': card_data.get('title', ''),
            'content': card_data.get('content', ''),
            'content_type': card_data.get('content_type', 'general'),
            'learning_type': card_data.get('learning_type', 'conceptual'),
            'difficulty': card_data.get('difficulty', 'medium'),
            'tags': card_data.get('tags', []),
            'meridian': {
                'channel': meridian,
                'acupoint': acupoint,
                'energy_flow': self._calculate_energy_flow(meridian, acupoint)
            },
            'neural_mapping': {
                'primary_region': neural_region,
                'connections': self._map_neural_connections(neural_region, card_data),
                'activation_pattern': self._generate_activation_pattern()
            },
            'memory_anchor': {
                'visual': card_data.get('visual_cue', ''),
                'auditory': card_data.get('auditory_cue', ''),
                'kinesthetic': card_data.get('kinesthetic_cue', ''),
                'emotional': card_data.get('emotional_weight', 5)
            },
            'learning_metrics': {
                'review_count': 0,
                'success_rate': 0,
                'last_reviewed': None,
                'next_review': self._calculate_next_review(datetime.now(), 0),
                'retention_strength': 0
            },
            'created_at': timestamp,
            'updated_at': timestamp
        }
        
        # 保存卡片
        file_path = f'{self.data_dir}/cards/{card_id}.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(card, f, ensure_ascii=False, indent=2)
        
        return card
    
    def _assign_meridian(self, content_type):
        """根據內容類型分配經絡"""
        meridian_mapping = {
            'emotional': '心經',
            'creative': '肝經',
            'foundational': '腎經',
            'analytical': '脾經',
            'communicative': '肺經',
            'practical': '胃經',
            'decisive': '膽經',
            'general': '膀胱經'
        }
        return meridian_mapping.get(content_type, '膀胱經')
    
    def _select_acupoint(self, meridian, difficulty):
        """根據難度選擇穴位"""
        points = self.meridian_points.get(meridian, ['通用穴'])
        difficulty_index = {'easy': 0, 'medium': len(points)//2, 'hard': -1}
        index = difficulty_index.get(difficulty, 0)
        return points[index] if points else '通用穴'
    
    def _assign_neural_region(self, learning_type):
        """根據學習類型分配神經區域"""
        neural_mapping = {
            'conceptual': '前額葉',
            'memory': '海馬體',
            'emotional': '杏仁核',
            'spatial': '頂葉',
            'linguistic': '顳葉',
            'visual': '枕葉',
            'procedural': '小腦',
            'basic': '腦幹'
        }
        return neural_mapping.get(learning_type, '前額葉')
    
    def _calculate_energy_flow(self, meridian, acupoint):
        """計算經絡能量流動"""
        base_flow = hash(f'{meridian}{acupoint}') % 100
        return {
            'intensity': base_flow,
            'direction': 'ascending' if base_flow > 50 else 'descending',
            'rhythm': 'steady' if base_flow % 3 == 0 else 'pulsing'
        }
    
    def _map_neural_connections(self, primary_region, card_data):
        """映射神經連接"""
        connections = [primary_region]
        
        # 根據卡片內容添加相關區域
        if card_data.get('has_visual'):
            connections.append('枕葉')
        if card_data.get('has_emotional'):
            connections.append('杏仁核')
        if card_data.get('requires_memory'):
            connections.append('海馬體')
        
        return list(set(connections))
    
    def _generate_activation_pattern(self):
        """生成神經激活模式"""
        import random
        patterns = ['alpha', 'beta', 'gamma', 'theta', 'delta']
        return {
            'dominant_wave': random.choice(patterns),
            'frequency': random.randint(8, 40),
            'amplitude': random.randint(10, 100)
        }
    
    def _calculate_next_review(self, last_review, success_count):
        """計算下次復習時間（間隔重複算法）"""
        intervals = [1, 3, 7, 14, 30, 90, 180]  # 天數
        interval_index = min(success_count, len(intervals) - 1)
        next_review = last_review + timedelta(days=intervals[interval_index])
        return next_review.isoformat()
    
    def get_learning_cards(self, filters=None):
        """獲取學習卡片列表"""
        cards = []
        cards_dir = f'{self.data_dir}/cards'
        
        if not os.path.exists(cards_dir):
            return cards
        
        for filename in os.listdir(cards_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(cards_dir, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        card = json.load(f)
                        
                    # 應用過濾器
                    if filters:
                        if not self._apply_filters(card, filters):
                            continue
                    
                    cards.append(card)
                except Exception as e:
                    continue
        
        return sorted(cards, key=lambda x: x['created_at'], reverse=True)
    
    def _apply_filters(self, card, filters):
        """應用過濾條件"""
        if 'meridian' in filters and card['meridian']['channel'] != filters['meridian']:
            return False
        if 'neural_region' in filters and card['neural_mapping']['primary_region'] != filters['neural_region']:
            return False
        if 'difficulty' in filters and card['difficulty'] != filters['difficulty']:
            return False
        if 'content_type' in filters and card['content_type'] != filters['content_type']:
            return False
        return True
    
    def update_learning_progress(self, card_id, success):
        """更新學習進度"""
        file_path = f'{self.data_dir}/cards/{card_id}.json'
        
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            card = json.load(f)
        
        # 更新學習指標
        metrics = card['learning_metrics']
        metrics['review_count'] += 1
        metrics['last_reviewed'] = datetime.now().isoformat()
        
        if success:
            success_count = getattr(self, '_get_success_count', lambda x: 0)(card_id) + 1
            metrics['success_rate'] = (metrics['success_rate'] * (metrics['review_count'] - 1) + 100) / metrics['review_count']
            metrics['retention_strength'] = min(100, metrics['retention_strength'] + 10)
        else:
            success_count = 0
            metrics['success_rate'] = (metrics['success_rate'] * (metrics['review_count'] - 1)) / metrics['review_count']
            metrics['retention_strength'] = max(0, metrics['retention_strength'] - 5)
        
        metrics['next_review'] = self._calculate_next_review(datetime.now(), success_count)
        card['updated_at'] = datetime.now().isoformat()
        
        # 保存更新
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(card, f, ensure_ascii=False, indent=2)
        
        return card
    
    def get_review_cards(self):
        """獲取需要復習的卡片"""
        now = datetime.now()
        review_cards = []
        
        for card in self.get_learning_cards():
            next_review = datetime.fromisoformat(card['learning_metrics']['next_review'])
            if next_review <= now:
                review_cards.append(card)
        
        return sorted(review_cards, key=lambda x: x['learning_metrics']['next_review'])
    
    def get_learning_statistics(self):
        """獲取學習統計"""
        cards = self.get_learning_cards()
        
        if not cards:
            return {
                'total_cards': 0,
                'meridian_distribution': {},
                'neural_distribution': {},
                'difficulty_distribution': {},
                'average_retention': 0,
                'cards_due_today': 0
            }
        
        # 統計分布
        meridian_dist = defaultdict(int)
        neural_dist = defaultdict(int)
        difficulty_dist = defaultdict(int)
        total_retention = 0
        cards_due_today = 0
        
        today = datetime.now().date()
        
        for card in cards:
            meridian_dist[card['meridian']['channel']] += 1
            neural_dist[card['neural_mapping']['primary_region']] += 1
            difficulty_dist[card['difficulty']] += 1
            total_retention += card['learning_metrics']['retention_strength']
            
            next_review = datetime.fromisoformat(card['learning_metrics']['next_review']).date()
            if next_review <= today:
                cards_due_today += 1
        
        return {
            'total_cards': len(cards),
            'meridian_distribution': dict(meridian_dist),
            'neural_distribution': dict(neural_dist),
            'difficulty_distribution': dict(difficulty_dist),
            'average_retention': total_retention / len(cards) if cards else 0,
            'cards_due_today': cards_due_today
        }
    
    def create_consciousness_duel(self, card_id, perspective_a, perspective_b):
        """創建意識對決機制"""
        duel_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        duel = {
            'id': duel_id,
            'card_id': card_id,
            'perspectives': {
                'a': {
                    'viewpoint': perspective_a,
                    'strength': 50,
                    'arguments': [],
                    'neural_activation': self._generate_activation_pattern()
                },
                'b': {
                    'viewpoint': perspective_b,
                    'strength': 50,
                    'arguments': [],
                    'neural_activation': self._generate_activation_pattern()
                }
            },
            'consciousness_state': {
                'awareness_level': 'emerging',
                'conflict_intensity': 'moderate',
                'resolution_tendency': 'balanced'
            },
            'created_at': timestamp,
            'status': 'active'
        }
        
        # 保存對決記錄
        file_path = f'{self.data_dir}/consciousness_duels/{duel_id}.json'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(duel, f, ensure_ascii=False, indent=2)
        
        return duel
    
    def create_ancient_text_card(self, text_data):
        """創建古籍卡片"""
        # 古籍特殊分類
        ancient_categories = {
            '經部': {'meridian': '心經', 'neural': '前額葉', 'type': 'foundational'},
            '史部': {'meridian': '腎經', 'neural': '海馬體', 'type': 'memory'},
            '子部': {'meridian': '肝經', 'neural': '前額葉', 'type': 'analytical'},
            '集部': {'meridian': '肺經', 'neural': '顳葉', 'type': 'creative'},
            '醫部': {'meridian': '脾經', 'neural': '前額葉', 'type': 'practical'},
            '道部': {'meridian': '腎經', 'neural': '杏仁核', 'type': 'emotional'},
            '佛部': {'meridian': '心經', 'neural': '前額葉', 'type': 'foundational'},
            '法本': {'meridian': '膽經', 'neural': '前額葉', 'type': 'decisive'}
        }
        
        category = text_data.get('category', '子部')
        category_info = ancient_categories.get(category, ancient_categories['子部'])
        
        card_data = {
            'title': text_data.get('title', ''),
            'content': text_data.get('content', ''),
            'content_type': category_info['type'],
            'learning_type': 'conceptual',
            'difficulty': text_data.get('difficulty', 'medium'),
            'tags': text_data.get('tags', []) + [category, '古籍', '手抄本'],
            'ancient_metadata': {
                'category': category,
                'dynasty': text_data.get('dynasty', ''),
                'author': text_data.get('author', ''),
                'source_library': text_data.get('source_library', ''),
                'manuscript_type': text_data.get('manuscript_type', '手抄本'),
                'preservation_level': text_data.get('preservation_level', 'good')
            }
        }
        
        return self.create_learning_card(card_data)
    
    def batch_import_ancient_texts(self, texts_list):
        """批量導入古籍"""
        results = {
            'success_count': 0,
            'failed_count': 0,
            'created_cards': [],
            'errors': []
        }
        
        for text_data in texts_list:
            try:
                card = self.create_ancient_text_card(text_data)
                results['created_cards'].append(card)
                results['success_count'] += 1
            except Exception as e:
                results['failed_count'] += 1
                results['errors'].append({
                    'title': text_data.get('title', 'Unknown'),
                    'error': str(e)
                })
        
        return results
    
    def get_ancient_texts_by_category(self, category=None):
        """按分類獲取古籍卡片"""
        cards = self.get_learning_cards()
        ancient_cards = []
        
        for card in cards:
            if 'ancient_metadata' in card:
                if category is None or card['ancient_metadata'].get('category') == category:
                    ancient_cards.append(card)
        
        return ancient_cards
    
    def get_ancient_text_statistics(self):
        """獲取古籍統計信息"""
        cards = self.get_learning_cards()
        ancient_cards = [card for card in cards if 'ancient_metadata' in card]
        
        stats = {
            'total_count': len(ancient_cards),
            'by_category': defaultdict(int),
            'by_dynasty': defaultdict(int),
            'by_source': defaultdict(int),
            'by_difficulty': defaultdict(int)
        }
        
        for card in ancient_cards:
            metadata = card.get('ancient_metadata', {})
            stats['by_category'][metadata.get('category', 'Unknown')] += 1
            stats['by_dynasty'][metadata.get('dynasty', 'Unknown')] += 1
            stats['by_source'][metadata.get('source_library', 'Unknown')] += 1
            stats['by_difficulty'][card.get('difficulty', 'medium')] += 1
        
        return dict(stats)
    
    def analyze_consciousness_state(self, card_id):
        """分析意識狀態"""
        # 獲取卡片信息
        file_path = f'{self.data_dir}/cards/{card_id}.json'
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            card = json.load(f)
        
        # 分析意識層次
        consciousness_analysis = {
            'awareness_depth': self._calculate_awareness_depth(card),
            'cognitive_complexity': self._assess_cognitive_complexity(card),
            'emotional_resonance': self._measure_emotional_resonance(card),
            'memory_integration': self._evaluate_memory_integration(card),
            'neural_coherence': self._analyze_neural_coherence(card),
            'meridian_harmony': self._assess_meridian_harmony(card),
            'consciousness_level': 'developing'
        }
        
        # 根據分析結果確定意識層次
        total_score = sum([
            consciousness_analysis['awareness_depth'],
            consciousness_analysis['cognitive_complexity'],
            consciousness_analysis['emotional_resonance'],
            consciousness_analysis['memory_integration']
        ]) / 4
        
        if total_score >= 80:
            consciousness_analysis['consciousness_level'] = 'transcendent'
        elif total_score >= 60:
            consciousness_analysis['consciousness_level'] = 'integrated'
        elif total_score >= 40:
            consciousness_analysis['consciousness_level'] = 'developing'
        else:
            consciousness_analysis['consciousness_level'] = 'emerging'
        
        return consciousness_analysis
    
    def deep_reflection_session(self, card_id, reflection_prompt):
        """深度反思功能"""
        session_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        # 獲取卡片和意識狀態
        consciousness_state = self.analyze_consciousness_state(card_id)
        if not consciousness_state:
            return None
        
        reflection_session = {
            'id': session_id,
            'card_id': card_id,
            'prompt': reflection_prompt,
            'consciousness_state': consciousness_state,
            'reflection_layers': {
                'surface': self._surface_reflection(reflection_prompt),
                'analytical': self._analytical_reflection(reflection_prompt, consciousness_state),
                'intuitive': self._intuitive_reflection(reflection_prompt, consciousness_state),
                'transcendent': self._transcendent_reflection(reflection_prompt, consciousness_state)
            },
            'insights': [],
            'transformation_potential': self._assess_transformation_potential(consciousness_state),
            'created_at': timestamp
        }
        
        # 保存反思記錄
        file_path = f'{self.data_dir}/reflections/{session_id}.json'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(reflection_session, f, ensure_ascii=False, indent=2)
        
        return reflection_session
    
    def _calculate_awareness_depth(self, card):
        """計算覺知深度"""
        base_score = card['learning_metrics']['retention_strength']
        complexity_bonus = len(card['tags']) * 5
        neural_bonus = len(card['neural_mapping']['connections']) * 10
        return min(100, base_score + complexity_bonus + neural_bonus)
    
    def _assess_cognitive_complexity(self, card):
        """評估認知複雜度"""
        difficulty_scores = {'easy': 30, 'medium': 60, 'hard': 90}
        base_score = difficulty_scores.get(card['difficulty'], 60)
        content_length_bonus = min(30, len(card['content']) // 50)
        return min(100, base_score + content_length_bonus)
    
    def _measure_emotional_resonance(self, card):
        """測量情緒共鳴"""
        emotional_weight = card['memory_anchor']['emotional']
        meridian_influence = self._get_meridian_emotional_influence(card['meridian']['channel'])
        return min(100, emotional_weight * 10 + meridian_influence)
    
    def _evaluate_memory_integration(self, card):
        """評估記憶整合度"""
        anchor_count = sum(1 for anchor in ['visual', 'auditory', 'kinesthetic'] 
                          if card['memory_anchor'][anchor])
        review_bonus = min(30, card['learning_metrics']['review_count'] * 5)
        success_bonus = card['learning_metrics']['success_rate'] * 0.3
        return min(100, anchor_count * 20 + review_bonus + success_bonus)
    
    def _analyze_neural_coherence(self, card):
        """分析神經一致性"""
        activation = card['neural_mapping']['activation_pattern']
        coherence_score = activation['frequency'] + activation['amplitude'] // 2
        return min(100, coherence_score)
    
    def _assess_meridian_harmony(self, card):
        """評估經絡和諧度"""
        energy_flow = card['meridian']['energy_flow']
        harmony_score = energy_flow['intensity']
        if energy_flow['rhythm'] == 'steady':
            harmony_score += 20
        return min(100, harmony_score)
    
    def _get_meridian_emotional_influence(self, meridian):
        """獲取經絡情緒影響"""
        emotional_influences = {
            '心經': 40, '肝經': 35, '腎經': 30, '脾經': 25,
            '肺經': 20, '胃經': 15, '膽經': 30, '膀胱經': 20
        }
        return emotional_influences.get(meridian, 20)
    
    def _surface_reflection(self, prompt):
        """表層反思"""
        return {
            'type': 'surface',
            'content': f'對於「{prompt}」的直觀反應和初步想法',
            'depth_level': 1
        }
    
    def _analytical_reflection(self, prompt, consciousness_state):
        """分析性反思"""
        return {
            'type': 'analytical',
            'content': f'基於意識層次「{consciousness_state["consciousness_level"]}」的邏輯分析',
            'depth_level': 2
        }
    
    def _intuitive_reflection(self, prompt, consciousness_state):
        """直覺性反思"""
        return {
            'type': 'intuitive',
            'content': f'超越邏輯的直覺洞察和內在智慧',
            'depth_level': 3
        }
    
    def _transcendent_reflection(self, prompt, consciousness_state):
        """超越性反思"""
        return {
            'type': 'transcendent',
            'content': f'整合所有層面的超越性理解',
            'depth_level': 4
        }
    
    def _assess_transformation_potential(self, consciousness_state):
        """評估轉化潛能"""
        level_scores = {
            'emerging': 25, 'developing': 50, 
            'integrated': 75, 'transcendent': 100
        }
        return level_scores.get(consciousness_state['consciousness_level'], 25)
    
    def create_hierarchical_card_system(self, book_data):
        """創建層級卡片系統"""
        hierarchy_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        # 創建主卡片（整本書概覽）
        master_card_data = {
            'title': f"【主卡片】{book_data.get('title', '')}",
            'content': book_data.get('overview', ''),
            'content_type': 'foundational',
            'learning_type': 'conceptual',
            'difficulty': book_data.get('difficulty', 'medium'),
            'tags': book_data.get('tags', []) + ['主卡片', '書籍概覽'],
            'hierarchy_metadata': {
                'hierarchy_id': hierarchy_id,
                'card_type': 'master',
                'level': 0,
                'parent_id': None,
                'child_ids': [],
                'book_info': {
                    'title': book_data.get('title', ''),
                    'author': book_data.get('author', ''),
                    'category': book_data.get('category', ''),
                    'total_chapters': len(book_data.get('chapters', [])),
                    'estimated_study_time': book_data.get('estimated_study_time', '未知')
                }
            }
        }
        
        master_card = self.create_learning_card(master_card_data)
        master_card_id = master_card['id']
        
        # 創建子卡片（各章節詳細內容）
        child_cards = []
        chapters = book_data.get('chapters', [])
        
        for i, chapter in enumerate(chapters):
            child_card_data = {
                'title': f"【第{i+1}章】{chapter.get('title', '')}",
                'content': chapter.get('content', ''),
                'content_type': chapter.get('content_type', 'analytical'),
                'learning_type': chapter.get('learning_type', 'conceptual'),
                'difficulty': chapter.get('difficulty', book_data.get('difficulty', 'medium')),
                'tags': chapter.get('tags', []) + ['子卡片', f'第{i+1}章', book_data.get('title', '')],
                'hierarchy_metadata': {
                    'hierarchy_id': hierarchy_id,
                    'card_type': 'child',
                    'level': 1,
                    'parent_id': master_card_id,
                    'child_ids': [],
                    'chapter_info': {
                        'chapter_number': i + 1,
                        'chapter_title': chapter.get('title', ''),
                        'key_concepts': chapter.get('key_concepts', []),
                        'learning_objectives': chapter.get('learning_objectives', [])
                    }
                }
            }
            
            child_card = self.create_learning_card(child_card_data)
            child_cards.append(child_card)
        
        # 更新主卡片的子卡片ID列表
        child_ids = [card['id'] for card in child_cards]
        self._update_card_hierarchy_metadata(master_card_id, {'child_ids': child_ids})
        
        # 創建層級關係記錄
        hierarchy_record = {
            'hierarchy_id': hierarchy_id,
            'master_card_id': master_card_id,
            'child_card_ids': child_ids,
            'book_title': book_data.get('title', ''),
            'total_cards': len(child_cards) + 1,
            'created_at': timestamp,
            'learning_path': self._generate_learning_path(master_card_id, child_ids),
            'progress_tracking': {
                'master_completed': False,
                'chapters_completed': [False] * len(child_cards),
                'overall_progress': 0
            }
        }
        
        # 保存層級關係
        hierarchy_file = f'{self.data_dir}/hierarchies/{hierarchy_id}.json'
        os.makedirs(os.path.dirname(hierarchy_file), exist_ok=True)
        with open(hierarchy_file, 'w', encoding='utf-8') as f:
            json.dump(hierarchy_record, f, ensure_ascii=False, indent=2)
        
        return {
            'hierarchy_id': hierarchy_id,
            'master_card': master_card,
            'child_cards': child_cards,
            'hierarchy_record': hierarchy_record
        }
    
    def _update_card_hierarchy_metadata(self, card_id, metadata_updates):
        """更新卡片的層級元數據"""
        file_path = f'{self.data_dir}/cards/{card_id}.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                card = json.load(f)
            
            card['hierarchy_metadata'].update(metadata_updates)
            card['updated_at'] = datetime.now().isoformat()
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(card, f, ensure_ascii=False, indent=2)
    
    def _generate_learning_path(self, master_card_id, child_ids):
        """生成學習路徑"""
        return {
            'recommended_order': [master_card_id] + child_ids,
            'learning_strategy': 'sequential',
            'estimated_completion_time': len(child_ids) * 30 + 60,  # 分鐘
            'difficulty_progression': 'gradual'
        }
    
    def get_hierarchical_cards(self, hierarchy_id=None):
        """獲取層級卡片"""
        if hierarchy_id:
            # 獲取特定層級的卡片
            hierarchy_file = f'{self.data_dir}/hierarchies/{hierarchy_id}.json'
            if os.path.exists(hierarchy_file):
                with open(hierarchy_file, 'r', encoding='utf-8') as f:
                    hierarchy = json.load(f)
                
                # 獲取主卡片和子卡片
                master_card = self._get_card_by_id(hierarchy['master_card_id'])
                child_cards = [self._get_card_by_id(card_id) for card_id in hierarchy['child_card_ids']]
                
                return {
                    'hierarchy': hierarchy,
                    'master_card': master_card,
                    'child_cards': [card for card in child_cards if card is not None]
                }
        else:
            # 獲取所有層級卡片系統
            hierarchies_dir = f'{self.data_dir}/hierarchies'
            if not os.path.exists(hierarchies_dir):
                return []
            
            hierarchies = []
            for filename in os.listdir(hierarchies_dir):
                if filename.endswith('.json'):
                    hierarchy_id = filename[:-5]  # 移除.json後綴
                    hierarchy_data = self.get_hierarchical_cards(hierarchy_id)
                    if hierarchy_data:
                        hierarchies.append(hierarchy_data)
            
            return hierarchies
    
    def _get_card_by_id(self, card_id):
        """根據ID獲取卡片"""
        file_path = f'{self.data_dir}/cards/{card_id}.json'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def update_hierarchy_progress(self, hierarchy_id, card_id, completed=True):
        """更新層級學習進度"""
        hierarchy_file = f'{self.data_dir}/hierarchies/{hierarchy_id}.json'
        if not os.path.exists(hierarchy_file):
            return None
        
        with open(hierarchy_file, 'r', encoding='utf-8') as f:
            hierarchy = json.load(f)
        
        progress = hierarchy['progress_tracking']
        
        # 更新進度
        if card_id == hierarchy['master_card_id']:
            progress['master_completed'] = completed
        elif card_id in hierarchy['child_card_ids']:
            chapter_index = hierarchy['child_card_ids'].index(card_id)
            progress['chapters_completed'][chapter_index] = completed
        
        # 計算總體進度
        completed_chapters = sum(progress['chapters_completed'])
        total_cards = len(hierarchy['child_card_ids']) + 1
        master_weight = 0.3  # 主卡片佔30%權重
        chapters_weight = 0.7  # 章節卡片佔70%權重
        
        overall_progress = 0
        if progress['master_completed']:
            overall_progress += master_weight * 100
        
        if hierarchy['child_card_ids']:
            chapter_progress = (completed_chapters / len(hierarchy['child_card_ids'])) * chapters_weight * 100
            overall_progress += chapter_progress
        
        progress['overall_progress'] = round(overall_progress, 1)
        hierarchy['updated_at'] = datetime.now().isoformat()
        
        # 保存更新
        with open(hierarchy_file, 'w', encoding='utf-8') as f:
            json.dump(hierarchy, f, ensure_ascii=False, indent=2)
        
        return hierarchy
    
    def get_hierarchy_statistics(self):
        """獲取層級卡片統計"""
        hierarchies = self.get_hierarchical_cards()
        
        stats = {
            'total_hierarchies': len(hierarchies),
            'total_books': len(hierarchies),
            'total_master_cards': len(hierarchies),
            'total_child_cards': 0,
            'completion_rates': [],
            'average_completion': 0,
            'by_category': defaultdict(int),
            'by_difficulty': defaultdict(int)
        }
        
        for hierarchy_data in hierarchies:
            hierarchy = hierarchy_data['hierarchy']
            master_card = hierarchy_data['master_card']
            child_cards = hierarchy_data['child_cards']
            
            stats['total_child_cards'] += len(child_cards)
            stats['completion_rates'].append(hierarchy['progress_tracking']['overall_progress'])
            
            # 統計分類
            if master_card and 'hierarchy_metadata' in master_card:
                book_info = master_card['hierarchy_metadata'].get('book_info', {})
                category = book_info.get('category', 'Unknown')
                stats['by_category'][category] += 1
                
                difficulty = master_card.get('difficulty', 'medium')
                stats['by_difficulty'][difficulty] += 1
        
        if stats['completion_rates']:
            stats['average_completion'] = sum(stats['completion_rates']) / len(stats['completion_rates'])
        
        return dict(stats)

# 創建全局實例
card_learning_system = CardLearningSystem()

@card_learning_bp.route('/api/card_learning/create', methods=['POST'])
def create_learning_card():
    """創建學習卡片"""
    try:
        data = request.get_json()
        card = card_learning_system.create_learning_card(data)
        return jsonify({
            'success': True,
            'card': card,
            'message': '學習卡片創建成功'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/cards', methods=['GET'])
def get_learning_cards():
    """獲取學習卡片列表"""
    try:
        filters = {
            'meridian': request.args.get('meridian'),
            'neural_region': request.args.get('neural_region'),
            'difficulty': request.args.get('difficulty'),
            'content_type': request.args.get('content_type')
        }
        # 移除空值
        filters = {k: v for k, v in filters.items() if v}
        
        cards = card_learning_system.get_learning_cards(filters)
        return jsonify({
            'success': True,
            'cards': cards
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/review', methods=['GET'])
def get_review_cards():
    """獲取需要復習的卡片"""
    try:
        cards = card_learning_system.get_review_cards()
        return jsonify({
            'success': True,
            'cards': cards
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/progress', methods=['POST'])
def update_progress():
    """更新學習進度"""
    try:
        data = request.get_json()
        card_id = data.get('card_id')
        success = data.get('success', False)
        
        card = card_learning_system.update_learning_progress(card_id, success)
        if card:
            return jsonify({
                'success': True,
                'card': card,
                'message': '學習進度更新成功'
            })
        else:
            return jsonify({
                'success': False,
                'error': '卡片不存在'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/statistics', methods=['GET'])
def get_statistics():
    """獲取學習統計"""
    try:
        stats = card_learning_system.get_learning_statistics()
        return jsonify({
            'success': True,
            'statistics': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/meridians', methods=['GET'])
def get_meridian_info():
    """獲取經絡信息"""
    try:
        return jsonify({
            'success': True,
            'meridians': card_learning_system.meridian_points,
            'neural_regions': card_learning_system.neural_regions
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/consciousness/duel', methods=['POST'])
def create_consciousness_duel():
    """創建意識對決"""
    try:
        data = request.get_json()
        card_id = data.get('card_id')
        perspective_a = data.get('perspective_a')
        perspective_b = data.get('perspective_b')
        
        duel = card_learning_system.create_consciousness_duel(card_id, perspective_a, perspective_b)
        return jsonify({
            'success': True,
            'duel': duel,
            'message': '意識對決創建成功'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/consciousness/analyze/<card_id>', methods=['GET'])
def analyze_consciousness():
    """分析意識狀態"""
    try:
        card_id = request.view_args['card_id']
        analysis = card_learning_system.analyze_consciousness_state(card_id)
        
        if analysis:
            return jsonify({
                'success': True,
                'analysis': analysis
            })
        else:
            return jsonify({
                'success': False,
                'error': '卡片不存在'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/reflection', methods=['POST'])
def create_reflection_session():
    """創建深度反思會話"""
    try:
        data = request.get_json()
        card_id = data.get('card_id')
        reflection_prompt = data.get('prompt')
        
        session = card_learning_system.deep_reflection_session(card_id, reflection_prompt)
        
        if session:
            return jsonify({
                'success': True,
                'session': session,
                'message': '深度反思會話創建成功'
            })
        else:
            return jsonify({
                'success': False,
                'error': '卡片不存在'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/ancient_text', methods=['POST'])
def create_ancient_text():
    """創建古籍卡片"""
    try:
        data = request.get_json()
        card = card_learning_system.create_ancient_text_card(data)
        return jsonify({
            'success': True,
            'card': card,
            'message': '古籍卡片創建成功'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/batch_import', methods=['POST'])
def batch_import_ancient_texts():
    """批量導入古籍"""
    try:
        data = request.get_json()
        texts_list = data.get('texts', [])
        result = card_learning_system.batch_import_ancient_texts(texts_list)
        return jsonify({
            'success': True,
            'result': result,
            'message': f'批量導入完成，成功 {result["success_count"]} 個，失敗 {result["failed_count"]} 個'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/ancient_texts', methods=['GET'])
def get_ancient_texts():
    """獲取古籍卡片"""
    try:
        category = request.args.get('category')
        cards = card_learning_system.get_ancient_texts_by_category(category)
        return jsonify({
            'success': True,
            'cards': cards
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/ancient_statistics', methods=['GET'])
def get_ancient_statistics():
    """獲取古籍統計"""
    try:
        stats = card_learning_system.get_ancient_text_statistics()
        return jsonify({
            'success': True,
            'statistics': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/hierarchy/create', methods=['POST'])
def create_hierarchical_system():
    """創建層級卡片系統"""
    try:
        data = request.get_json()
        result = card_learning_system.create_hierarchical_card_system(data)
        return jsonify({
            'success': True,
            'result': result,
            'message': f'層級卡片系統創建成功，包含1個主卡片和{len(result["child_cards"])}個子卡片'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/hierarchy/list', methods=['GET'])
def get_hierarchical_systems():
    """獲取層級卡片系統列表"""
    try:
        hierarchies = card_learning_system.get_hierarchical_cards()
        return jsonify({
            'success': True,
            'hierarchies': hierarchies
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/hierarchy/<hierarchy_id>', methods=['GET'])
def get_hierarchical_system():
    """獲取特定層級卡片系統"""
    try:
        hierarchy_id = request.view_args['hierarchy_id']
        hierarchy_data = card_learning_system.get_hierarchical_cards(hierarchy_id)
        
        if hierarchy_data:
            return jsonify({
                'success': True,
                'hierarchy_data': hierarchy_data
            })
        else:
            return jsonify({
                'success': False,
                'error': '層級卡片系統不存在'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/hierarchy/progress', methods=['POST'])
def update_hierarchy_progress():
    """更新層級學習進度"""
    try:
        data = request.get_json()
        hierarchy_id = data.get('hierarchy_id')
        card_id = data.get('card_id')
        completed = data.get('completed', True)
        
        result = card_learning_system.update_hierarchy_progress(hierarchy_id, card_id, completed)
        
        if result:
            return jsonify({
                'success': True,
                'hierarchy': result,
                'message': '學習進度更新成功'
            })
        else:
            return jsonify({
                'success': False,
                'error': '層級卡片系統不存在'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@card_learning_bp.route('/api/card_learning/hierarchy/statistics', methods=['GET'])
def get_hierarchy_statistics():
    """獲取層級卡片統計"""
    try:
        stats = card_learning_system.get_hierarchy_statistics()
        return jsonify({
            'success': True,
            'statistics': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
古籍JSON文件生成器
為典藏司提供古籍數據生成和學習卡片創建功能
"""

import json
import os
import uuid
from datetime import datetime
from typing import List, Dict, Any

class AncientTextGenerator:
    """古籍文本生成器"""
    
    def __init__(self, data_dir="data/ancient_texts"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        
        # 古籍分類體系
        self.categories = {
            '經部': {
                'description': '儒家經典',
                'subcategories': ['易類', '書類', '詩類', '禮類', '春秋類', '孝經類', '四書類'],
                'meridian': '心經',
                'neural_region': '前額葉',
                'learning_type': 'foundational'
            },
            '史部': {
                'description': '史學典籍',
                'subcategories': ['正史', '編年', '紀事本末', '別史', '雜史', '詔令奏議', '傳記'],
                'meridian': '腎經',
                'neural_region': '海馬體',
                'learning_type': 'memory'
            },
            '子部': {
                'description': '諸子百家',
                'subcategories': ['儒家', '兵家', '法家', '農家', '醫家', '天文算法', '術數', '藝術'],
                'meridian': '肝經',
                'neural_region': '前額葉',
                'learning_type': 'analytical'
            },
            '集部': {
                'description': '文學作品',
                'subcategories': ['楚辭', '別集', '總集', '詩文評', '詞曲'],
                'meridian': '肺經',
                'neural_region': '顳葉',
                'learning_type': 'creative'
            },
            '醫部': {
                'description': '醫學典籍',
                'subcategories': ['醫經', '經方', '諸家', '針灸', '本草'],
                'meridian': '脾經',
                'neural_region': '前額葉',
                'learning_type': 'practical'
            },
            '道部': {
                'description': '道教典籍',
                'subcategories': ['道德經', '莊子', '列子', '抱朴子', '太平經'],
                'meridian': '腎經',
                'neural_region': '杏仁核',
                'learning_type': 'emotional'
            },
            '佛部': {
                'description': '佛教典籍',
                'subcategories': ['經藏', '律藏', '論藏', '禪宗', '淨土'],
                'meridian': '心經',
                'neural_region': '前額葉',
                'learning_type': 'foundational'
            },
            '法本': {
                'description': '法術典籍',
                'subcategories': ['符咒', '占卜', '風水', '奇門遁甲', '太乙神數'],
                'meridian': '膽經',
                'neural_region': '前額葉',
                'learning_type': 'decisive'
            }
        }
        
        # 朝代信息
        self.dynasties = {
            '先秦': {'period': '公元前2070年-公元前221年', 'characteristics': '百家爭鳴'},
            '秦漢': {'period': '公元前221年-公元220年', 'characteristics': '大一統思想'},
            '魏晉南北朝': {'period': '公元220年-公元589年', 'characteristics': '玄學興起'},
            '隋唐': {'period': '公元581年-公元907年', 'characteristics': '文化繁榮'},
            '宋元': {'period': '公元960年-公元1368年', 'characteristics': '理學發展'},
            '明清': {'period': '公元1368年-公元1912年', 'characteristics': '考據學興盛'}
        }
        
        # 預設古籍模板
        self.ancient_text_templates = self._load_templates()
    
    def _load_templates(self) -> List[Dict]:
        """載入古籍模板"""
        return [
            {
                'title': '道德經第一章',
                'category': '道部',
                'dynasty': '先秦',
                'author': '老子',
                'content': '道可道，非常道。名可名，非常名。無名天地之始，有名萬物之母。故常無欲，以觀其妙；常有欲，以觀其徼。此兩者，同出而異名，同謂之玄。玄之又玄，眾妙之門。',
                'source_library': '國家圖書館',
                'manuscript_type': '手抄本',
                'preservation_level': 'excellent',
                'difficulty': 'hard',
                'tags': ['道家', '哲學', '宇宙觀']
            },
            {
                'title': '論語·學而第一',
                'category': '經部',
                'dynasty': '先秦',
                'author': '孔子',
                'content': '子曰：「學而時習之，不亦說乎？有朋自遠方來，不亦樂乎？人不知而不慍，不亦君子乎？」',
                'source_library': '故宮博物院',
                'manuscript_type': '刻本',
                'preservation_level': 'good',
                'difficulty': 'medium',
                'tags': ['儒家', '教育', '修身']
            },
            {
                'title': '心經',
                'category': '佛部',
                'dynasty': '唐',
                'author': '玄奘',
                'content': '觀自在菩薩，行深般若波羅蜜多時，照見五蘊皆空，度一切苦厄。舍利子，色不異空，空不異色，色即是空，空即是色，受想行識，亦復如是。',
                'source_library': '敦煌研究院',
                'manuscript_type': '寫經',
                'preservation_level': 'excellent',
                'difficulty': 'hard',
                'tags': ['佛教', '般若', '空性']
            },
            {
                'title': '黃帝內經·素問',
                'category': '醫部',
                'dynasty': '先秦',
                'author': '黃帝',
                'content': '昔在黃帝，生而神靈，弱而能言，幼而徇齊，長而敦敏，成而登天。乃問於天師曰：余聞上古之人，春秋皆度百歲，而動作不衰；今時之人，年半百而動作皆衰者，時世異耶？人將失之耶？',
                'source_library': '中醫科學院',
                'manuscript_type': '刻本',
                'preservation_level': 'good',
                'difficulty': 'hard',
                'tags': ['中醫', '養生', '經典']
            },
            {
                'title': '易經·乾卦',
                'category': '經部',
                'dynasty': '先秦',
                'author': '伏羲',
                'content': '乾：元，亨，利，貞。初九：潛龍勿用。九二：見龍在田，利見大人。九三：君子終日乾乾，夕惕若厲，無咎。九四：或躍在淵，無咎。九五：飛龍在天，利見大人。上九：亢龍有悔。',
                'source_library': '北京大學圖書館',
                'manuscript_type': '手抄本',
                'preservation_level': 'excellent',
                'difficulty': 'hard',
                'tags': ['易學', '占卜', '哲學']
            },
            {
                'title': '莊子·逍遙遊',
                'category': '子部',
                'dynasty': '先秦',
                'author': '莊子',
                'content': '南璃有火，其名為鳳。鳳之大，不知其幾千里也。化而為鳥，其名為鵬。鵬之背，不知其幾千里也；怒而飛，其翼若垂天之雲。',
                'source_library': '清華大學圖書館',
                'manuscript_type': '刻本',
                'preservation_level': 'good',
                'difficulty': 'medium',
                'tags': ['道家', '寓言', '自由']
            }
        ]
    
    def generate_ancient_text_json(self, custom_texts: List[Dict] = None) -> str:
        """生成古籍JSON文件"""
        texts = custom_texts if custom_texts else self.ancient_text_templates
        
        # 為每個文本添加元數據
        enhanced_texts = []
        for text in texts:
            enhanced_text = self._enhance_text_metadata(text)
            enhanced_texts.append(enhanced_text)
        
        # 生成JSON文件
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'ancient_texts_{timestamp}.json'
        filepath = os.path.join(self.data_dir, filename)
        
        json_data = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_count': len(enhanced_texts),
                'generator_version': '1.0.0',
                'description': '典藏司古籍數據集'
            },
            'ancient_texts': enhanced_texts
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        
        return filepath
    
    def _enhance_text_metadata(self, text: Dict) -> Dict:
        """增強文本元數據"""
        category = text.get('category', '子部')
        category_info = self.categories.get(category, self.categories['子部'])
        
        enhanced = {
            'id': str(uuid.uuid4()),
            'title': text.get('title', ''),
            'content': text.get('content', ''),
            'category': category,
            'subcategory': text.get('subcategory', ''),
            'dynasty': text.get('dynasty', ''),
            'author': text.get('author', ''),
            'source_library': text.get('source_library', ''),
            'manuscript_type': text.get('manuscript_type', '手抄本'),
            'preservation_level': text.get('preservation_level', 'good'),
            'difficulty': text.get('difficulty', 'medium'),
            'tags': text.get('tags', []) + [category, '古籍'],
            'learning_metadata': {
                'meridian': category_info['meridian'],
                'neural_region': category_info['neural_region'],
                'learning_type': category_info['learning_type'],
                'estimated_study_time': self._estimate_study_time(text),
                'complexity_score': self._calculate_complexity(text)
            },
            'cultural_context': {
                'historical_period': self.dynasties.get(text.get('dynasty', ''), {}),
                'philosophical_school': self._identify_philosophical_school(text),
                'literary_style': self._analyze_literary_style(text)
            },
            'created_at': datetime.now().isoformat()
        }
        
        return enhanced
    
    def _estimate_study_time(self, text: Dict) -> int:
        """估算學習時間（分鐘）"""
        content_length = len(text.get('content', ''))
        difficulty_multiplier = {'easy': 1, 'medium': 1.5, 'hard': 2}
        base_time = content_length // 10  # 每10字約1分鐘
        multiplier = difficulty_multiplier.get(text.get('difficulty', 'medium'), 1.5)
        return int(base_time * multiplier)
    
    def _calculate_complexity(self, text: Dict) -> int:
        """計算複雜度分數（1-100）"""
        content_length = len(text.get('content', ''))
        difficulty_scores = {'easy': 30, 'medium': 60, 'hard': 90}
        
        base_score = difficulty_scores.get(text.get('difficulty', 'medium'), 60)
        length_bonus = min(20, content_length // 50)
        tag_bonus = len(text.get('tags', [])) * 2
        
        return min(100, base_score + length_bonus + tag_bonus)
    
    def _identify_philosophical_school(self, text: Dict) -> str:
        """識別哲學流派"""
        category = text.get('category', '')
        author = text.get('author', '').lower()
        content = text.get('content', '').lower()
        
        if category == '道部' or '老子' in author or '莊子' in author:
            return '道家'
        elif category == '經部' or '孔子' in author or '孟子' in author:
            return '儒家'
        elif category == '佛部':
            return '佛教'
        elif '墨子' in author:
            return '墨家'
        elif '韓非' in author or '商鞅' in author:
            return '法家'
        else:
            return '其他'
    
    def _analyze_literary_style(self, text: Dict) -> str:
        """分析文學風格"""
        content = text.get('content', '')
        category = text.get('category', '')
        
        if category == '集部':
            if '詩' in content or '韻' in content:
                return '詩歌'
            elif '賦' in content:
                return '賦體'
            else:
                return '散文'
        elif category == '史部':
            return '史傳體'
        elif '子曰' in content or '曰：' in content:
            return '語錄體'
        elif '。' in content and len(content.split('。')) > 3:
            return '論說體'
        else:
            return '經典體'
    
    def create_learning_cards_from_json(self, json_file_path: str) -> List[Dict]:
        """從JSON文件創建學習卡片"""
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        cards = []
        for text in data.get('ancient_texts', []):
            card = self._convert_to_learning_card(text)
            cards.append(card)
        
        return cards
    
    def _convert_to_learning_card(self, text: Dict) -> Dict:
        """將古籍文本轉換為學習卡片格式"""
        learning_metadata = text.get('learning_metadata', {})
        
        card = {
            'id': text.get('id', str(uuid.uuid4())),
            'title': text.get('title', ''),
            'content': text.get('content', ''),
            'content_type': learning_metadata.get('learning_type', 'conceptual'),
            'learning_type': 'conceptual',
            'difficulty': text.get('difficulty', 'medium'),
            'tags': text.get('tags', []),
            'meridian': {
                'channel': learning_metadata.get('meridian', '心經'),
                'acupoint': self._select_acupoint(learning_metadata.get('meridian', '心經')),
                'energy_flow': 'balanced'
            },
            'neural_mapping': {
                'primary_region': learning_metadata.get('neural_region', '前額葉'),
                'secondary_regions': [],
                'connections': []
            },
            'memory_anchor': {
                'visual': True,
                'auditory': True,
                'kinesthetic': False,
                'emotional': 70
            },
            'learning_metrics': {
                'retention_strength': 0,
                'review_count': 0,
                'success_rate': 0,
                'last_reviewed': None
            },
            'ancient_metadata': {
                'category': text.get('category', ''),
                'dynasty': text.get('dynasty', ''),
                'author': text.get('author', ''),
                'source_library': text.get('source_library', ''),
                'manuscript_type': text.get('manuscript_type', ''),
                'preservation_level': text.get('preservation_level', ''),
                'cultural_context': text.get('cultural_context', {})
            },
            'created_at': datetime.now().isoformat()
        }
        
        return card
    
    def _select_acupoint(self, meridian: str) -> str:
        """根據經絡選擇穴位"""
        acupoint_map = {
            '心經': '神門',
            '腎經': '湧泉',
            '肝經': '太衝',
            '肺經': '太淵',
            '脾經': '太白',
            '膽經': '風池'
        }
        return acupoint_map.get(meridian, '神門')
    
    def export_sample_json(self) -> str:
        """導出示例JSON文件"""
        return self.generate_ancient_text_json()
    
    def get_categories_info(self) -> Dict:
        """獲取分類信息"""
        return self.categories
    
    def get_dynasties_info(self) -> Dict:
        """獲取朝代信息"""
        return self.dynasties

# 使用示例
if __name__ == '__main__':
    generator = AncientTextGenerator()
    
    # 生成示例JSON文件
    json_file = generator.export_sample_json()
    print(f"古籍JSON文件已生成: {json_file}")
    
    # 從JSON創建學習卡片
    cards = generator.create_learning_cards_from_json(json_file)
    print(f"已生成 {len(cards)} 張學習卡片")
    
    # 顯示分類信息
    print("\n古籍分類體系:")
    for category, info in generator.get_categories_info().items():
        print(f"- {category}: {info['description']}")
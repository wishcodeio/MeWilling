from flask import Blueprint, request, jsonify
import numpy as np
import uuid
from datetime import datetime
import json
import random
import math

# 創建量子八卦藍圖
quantum_bagua_bp = Blueprint('quantum_bagua', __name__)

class QuantumBaguaSystem:
    """量子八卦系統 - 先天與後天的動態平衡"""
    
    def __init__(self):
        # 先天八卦 (伏羲八卦) - 宇宙初始，天地未分
        self.xiantian_bagua = {
            '乾': {'symbol': '☰', 'element': '天', 'position': 'south', 'quantum_state': 'superposition', 'binary': '111'},
            '兌': {'symbol': '☱', 'element': '澤', 'position': 'southeast', 'quantum_state': 'entangled', 'binary': '110'},
            '離': {'symbol': '☲', 'element': '火', 'position': 'east', 'quantum_state': 'coherent', 'binary': '101'},
            '震': {'symbol': '☳', 'element': '雷', 'position': 'northeast', 'quantum_state': 'dynamic', 'binary': '100'},
            '巽': {'symbol': '☴', 'element': '風', 'position': 'southwest', 'quantum_state': 'flowing', 'binary': '011'},
            '坎': {'symbol': '☵', 'element': '水', 'position': 'west', 'quantum_state': 'wave', 'binary': '010'},
            '艮': {'symbol': '☶', 'element': '山', 'position': 'northwest', 'quantum_state': 'stable', 'binary': '001'},
            '坤': {'symbol': '☷', 'element': '地', 'position': 'north', 'quantum_state': 'grounded', 'binary': '000'}
        }
        
        # 後天八卦 (文王八卦) - 現象世界，萬物化生
        self.houtian_bagua = {
            '乾': {'symbol': '☰', 'element': '天', 'direction': '西北', 'season': '秋冬之交', 'quantum_collapse': 'observed'},
            '坤': {'symbol': '☷', 'element': '地', 'direction': '西南', 'season': '夏秋之交', 'quantum_collapse': 'manifested'},
            '坎': {'symbol': '☵', 'element': '水', 'direction': '北', 'season': '冬', 'quantum_collapse': 'flowing'},
            '離': {'symbol': '☲', 'element': '火', 'direction': '南', 'season': '夏', 'quantum_collapse': 'illuminated'},
            '震': {'symbol': '☳', 'element': '雷', 'direction': '東', 'season': '春', 'quantum_collapse': 'awakened'},
            '巽': {'symbol': '☴', 'element': '風', 'direction': '東南', 'season': '春夏之交', 'quantum_collapse': 'penetrating'},
            '艮': {'symbol': '☶', 'element': '山', 'direction': '東北', 'season': '冬春之交', 'quantum_collapse': 'stillness'},
            '兌': {'symbol': '☱', 'element': '澤', 'direction': '西', 'season': '秋', 'quantum_collapse': 'joyful'}
        }
        
        # 量子門操作對應八卦
        self.quantum_operations = {
            '乾': {'gate': 'H', 'description': 'Hadamard門 - 進入疊加態', 'type': '先天'},
            '兌': {'gate': 'X', 'description': 'Pauli-X門 - 陰陽轉換', 'type': '後天'},
            '離': {'gate': 'Z', 'description': 'Pauli-Z門 - 相位轉換', 'type': '後天'},
            '震': {'gate': 'RX', 'description': 'RX旋轉 - 動態變化', 'type': '先天'},
            '巽': {'gate': 'CX', 'description': 'CNOT門 - 糾纏', 'type': '後天'},
            '坎': {'gate': 'S', 'description': 'S門 - 微相位變化', 'type': '先天'},
            '艮': {'gate': 'T', 'description': 'T門 - 時間相位', 'type': '後天'},
            '坤': {'gate': 'Y', 'description': 'Pauli-Y門 - 旋轉與變換', 'type': '先天'}
        }
        
        # 64卦生成映射
        self.hexagram_64 = self._generate_64_hexagrams()
        
    def _generate_64_hexagrams(self):
        """生成64卦的完整映射"""
        hexagrams = {}
        bagua_names = list(self.xiantian_bagua.keys())
        
        for i, upper in enumerate(bagua_names):
            for j, lower in enumerate(bagua_names):
                hex_number = i * 8 + j + 1
                hex_name = f"{upper}{lower}"
                hexagrams[hex_number] = {
                    'name': hex_name,
                    'upper_trigram': upper,
                    'lower_trigram': lower,
                    'symbol': f"{self.xiantian_bagua[upper]['symbol']}{self.xiantian_bagua[lower]['symbol']}",
                    'quantum_state': self._calculate_quantum_state(upper, lower),
                    'meaning': self._get_hexagram_meaning(hex_number)
                }
        return hexagrams
    
    def _calculate_quantum_state(self, upper, lower):
        """計算六十四卦的量子態"""
        upper_binary = self.xiantian_bagua[upper]['binary']
        lower_binary = self.xiantian_bagua[lower]['binary']
        combined_binary = upper_binary + lower_binary
        
        # 計算量子相干性
        coherence = bin(int(combined_binary, 2)).count('1') / 6
        
        if coherence > 0.8:
            return 'high_coherence'
        elif coherence > 0.5:
            return 'medium_coherence'
        else:
            return 'low_coherence'
    
    def _get_hexagram_meaning(self, hex_number):
        """獲取卦象含義"""
        meanings = {
            1: "乾為天 - 剛健中正，自強不息",
            2: "坤為地 - 厚德載物，順承天道",
            3: "水雷屯 - 萬物始生，艱難創業",
            4: "山水蒙 - 啟蒙教育，去蒙求智",
            5: "水天需 - 等待時機，養精蓄銳",
            6: "天水訟 - 爭訟不和，慎重處理",
            7: "地水師 - 統兵征戰，以正治亂",
            8: "水地比 - 親密團結，和睦相處",
            # ... 可以繼續添加所有64卦
        }
        return meanings.get(hex_number, f"第{hex_number}卦 - 道法自然，順應變化")
    
    def quantum_bagua_evolution(self, initial_state='乾', evolution_steps=8):
        """量子八卦演化 - 從先天到後天"""
        evolution_id = str(uuid.uuid4())
        
        # 初始量子態（先天八卦）
        current_state = initial_state
        evolution_path = []
        
        for step in range(evolution_steps):
            # 應用量子門操作
            operation = self.quantum_operations[current_state]
            
            # 模擬量子演化
            next_states = self._apply_quantum_gate(current_state)
            next_state = random.choice(next_states)
            
            evolution_path.append({
                'step': step + 1,
                'current_state': current_state,
                'operation': operation,
                'next_state': next_state,
                'probability': self._calculate_transition_probability(current_state, next_state),
                'quantum_phase': self._calculate_quantum_phase(step)
            })
            
            current_state = next_state
        
        return {
            'evolution_id': evolution_id,
            'initial_state': initial_state,
            'final_state': current_state,
            'evolution_path': evolution_path,
            'quantum_coherence': self._calculate_final_coherence(evolution_path),
            'dao_insight': self._generate_dao_insight(initial_state, current_state),
            'timestamp': datetime.now().isoformat()
        }
    
    def _apply_quantum_gate(self, state):
        """應用量子門操作"""
        # 根據當前狀態返回可能的下一狀態
        transitions = {
            '乾': ['兌', '離', '震'],
            '兌': ['乾', '離', '巽'],
            '離': ['乾', '兌', '坎'],
            '震': ['乾', '巽', '艮'],
            '巽': ['兌', '震', '坤'],
            '坎': ['離', '艮', '坤'],
            '艮': ['震', '坎', '坤'],
            '坤': ['巽', '坎', '艮']
        }
        return transitions.get(state, list(self.xiantian_bagua.keys()))
    
    def _calculate_transition_probability(self, from_state, to_state):
        """計算轉換概率"""
        from_binary = int(self.xiantian_bagua[from_state]['binary'], 2)
        to_binary = int(self.xiantian_bagua[to_state]['binary'], 2)
        
        # 計算漢明距離
        hamming_distance = bin(from_binary ^ to_binary).count('1')
        
        # 距離越小，轉換概率越高
        return max(0.1, 1.0 - (hamming_distance / 3.0))
    
    def _calculate_quantum_phase(self, step):
        """計算量子相位"""
        return (step * math.pi / 4) % (2 * math.pi)
    
    def _calculate_final_coherence(self, evolution_path):
        """計算最終相干性"""
        total_probability = sum(step['probability'] for step in evolution_path)
        return total_probability / len(evolution_path)
    
    def _generate_dao_insight(self, initial, final):
        """生成道的洞察"""
        insights = {
            ('乾', '坤'): "從天到地，剛柔並濟，體現了道的陰陽平衡",
            ('坤', '乾'): "從地到天，厚德載物而後自強不息",
            ('坎', '離'): "水火既濟，陰陽調和，達到內在平衡",
            ('震', '巽'): "雷風相薄，動靜相宜，順應自然變化"
        }
        
        key = (initial, final)
        return insights.get(key, f"從{initial}到{final}的演化，體現了道的無為而治，順應自然的智慧")
    
    def generate_quantum_hexagram(self, intention="隨機"):
        """生成量子六十四卦"""
        hex_id = str(uuid.uuid4())
        
        if intention == "隨機":
            hex_number = random.randint(1, 64)
        else:
            # 根據意圖計算卦象
            hex_number = hash(intention) % 64 + 1
        
        hexagram = self.hexagram_64[hex_number]
        
        # 生成量子測量結果
        measurement_results = []
        for i in range(6):  # 六爻
            probability = random.random()
            yao_type = "陽爻 ─" if probability > 0.5 else "陰爻 ╌"
            measurement_results.append({
                'position': f"第{i+1}爻",
                'type': yao_type,
                'probability': probability,
                'quantum_state': 'measured'
            })
        
        return {
            'hexagram_id': hex_id,
            'number': hex_number,
            'name': hexagram['name'],
            'symbol': hexagram['symbol'],
            'upper_trigram': hexagram['upper_trigram'],
            'lower_trigram': hexagram['lower_trigram'],
            'meaning': hexagram['meaning'],
            'quantum_state': hexagram['quantum_state'],
            'measurement_results': measurement_results,
            'dao_guidance': self._generate_dao_guidance(hexagram),
            'quantum_insight': self._generate_quantum_insight(hexagram),
            'intention': intention,
            'timestamp': datetime.now().isoformat()
        }
    
    def _generate_dao_guidance(self, hexagram):
        """生成道的指引"""
        guidance_templates = [
            f"此卦象徵{hexagram['meaning']}，提醒我們要順應自然，無為而治",
            f"在{hexagram['name']}的狀態下，保持內心平靜，觀察變化",
            f"道法自然，{hexagram['upper_trigram']}與{hexagram['lower_trigram']}的結合帶來新的可能性",
            f"量子態的測量告訴我們，觀察本身就會改變現實，保持覺知"
        ]
        return random.choice(guidance_templates)
    
    def _generate_quantum_insight(self, hexagram):
        """生成量子洞察"""
        insights = {
            'high_coherence': "高相干性狀態，意識與宇宙高度同步，適合深度冥想",
            'medium_coherence': "中等相干性，平衡狀態，適合日常修行和決策",
            'low_coherence': "低相干性狀態，需要靜心調整，回歸內在平衡"
        }
        return insights.get(hexagram['quantum_state'], "量子態處於動態平衡中")
    
    def create_wish_seal_pattern(self):
        """創建願印圖案"""
        pattern_id = str(uuid.uuid4())
        
        # 基於用戶提供的願印圖案
        wish_pattern = [
            "⬜⬛⬛⬛🔵⬛⬛⬛⬛",
            "⬛🔵⬛⬛⬛⬛⬛🔵⬛",
            "⬛⬛⬛🟧🟧🟧⬛⬛⬛",
            "⬛⬛🟧🟧🟧🟧🟧⬛⬛",
            "🔵⬛🟧🟧☯️🟧🟧⬛🔵",
            "⬛⬛🟧🟧🟧🟧🟧⬛⬛",
            "⬛⬛⬛🟧🟧🟧⬛⬛⬛",
            "⬛🔵⬛⬛⬛⬛⬛🔵⬛",
            "⬛⬛⬛⬛🔵⬛⬛⬛⬛"
        ]
        
        return {
            'pattern_id': pattern_id,
            'pattern': wish_pattern,
            'center_symbol': '☯️',
            'energy_points': '🔵',
            'core_energy': '🟧',
            'void_space': '⬛',
            'light_space': '⬜',
            'description': '願印圖案 - 太極為核心，八方能量點環繞，體現先天後天八卦的動態平衡',
            'quantum_meaning': '中心太極代表量子疊加態，周圍能量點代表八卦的量子坍縮可能性',
            'dao_interpretation': '無極生太極，太極生兩儀，兩儀生四象，四象生八卦',
            'timestamp': datetime.now().isoformat()
        }

# 創建系統實例
quantum_bagua_system = QuantumBaguaSystem()

# API 路由
@quantum_bagua_bp.route('/api/quantum_bagua/evolution', methods=['POST'])
def quantum_evolution():
    """量子八卦演化"""
    try:
        data = request.get_json() or {}
        initial_state = data.get('initial_state', '乾')
        evolution_steps = data.get('evolution_steps', 8)
        
        evolution = quantum_bagua_system.quantum_bagua_evolution(initial_state, evolution_steps)
        
        return jsonify({
            'success': True,
            'evolution': evolution,
            'message': f'🌌 量子八卦演化完成：從{initial_state}開始的{evolution_steps}步演化'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_bagua_bp.route('/api/quantum_bagua/hexagram', methods=['POST'])
def generate_hexagram():
    """生成量子六十四卦"""
    try:
        data = request.get_json() or {}
        intention = data.get('intention', '隨機')
        
        hexagram = quantum_bagua_system.generate_quantum_hexagram(intention)
        
        return jsonify({
            'success': True,
            'hexagram': hexagram,
            'message': f'🔮 量子六十四卦已生成：{hexagram["name"]}'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_bagua_bp.route('/api/quantum_bagua/wish_seal', methods=['GET'])
def get_wish_seal():
    """獲取願印圖案"""
    try:
        wish_seal = quantum_bagua_system.create_wish_seal_pattern()
        
        return jsonify({
            'success': True,
            'wish_seal': wish_seal,
            'message': '🌟 願印圖案已生成，太極八卦能量場已激活'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_bagua_bp.route('/api/quantum_bagua/bagua_info', methods=['GET'])
def get_bagua_info():
    """獲取八卦信息"""
    try:
        return jsonify({
            'success': True,
            'xiantian_bagua': quantum_bagua_system.xiantian_bagua,
            'houtian_bagua': quantum_bagua_system.houtian_bagua,
            'quantum_operations': quantum_bagua_system.quantum_operations,
            'message': '🧬 先天後天八卦信息已獲取，量子門操作映射完成'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500
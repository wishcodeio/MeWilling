from flask import Blueprint, request, jsonify, render_template
import numpy as np
import json
from datetime import datetime
import math
import random

# 創建腦神經拓撲API藍圖
neural_topology_bp = Blueprint('neural_topology', __name__)

class NeuralTopologyEngine:
    """腦神經拓撲引擎 - 處理左右腦交互和願頻計算"""
    
    def __init__(self):
        self.brain_frequencies = {
            'alpha': {'range': (8, 13), 'default': 10, 'description': '放鬆專注'},
            'beta': {'range': (14, 30), 'default': 20, 'description': '邏輯思維'},
            'gamma': {'range': (31, 100), 'default': 40, 'description': '高階認知'},
            'theta': {'range': (4, 7), 'default': 6, 'description': '深度冥想'},
            'delta': {'range': (0.5, 4), 'default': 2, 'description': '深度睡眠'}
        }
        
        self.meridian_brain_mapping = {
            # 十二經絡與腦區對應
            '肺經': {'brain_region': 'respiratory_center', 'hemisphere': 'both', 'frequency': 'alpha'},
            '大腸經': {'brain_region': 'motor_cortex', 'hemisphere': 'left', 'frequency': 'beta'},
            '胃經': {'brain_region': 'hypothalamus', 'hemisphere': 'both', 'frequency': 'theta'},
            '脾經': {'brain_region': 'limbic_system', 'hemisphere': 'right', 'frequency': 'alpha'},
            '心經': {'brain_region': 'emotional_center', 'hemisphere': 'right', 'frequency': 'gamma'},
            '小腸經': {'brain_region': 'digestive_center', 'hemisphere': 'left', 'frequency': 'beta'},
            '膀胱經': {'brain_region': 'autonomic_center', 'hemisphere': 'both', 'frequency': 'theta'},
            '腎經': {'brain_region': 'endocrine_center', 'hemisphere': 'both', 'frequency': 'delta'},
            '心包經': {'brain_region': 'cardiovascular_center', 'hemisphere': 'right', 'frequency': 'alpha'},
            '三焦經': {'brain_region': 'metabolic_center', 'hemisphere': 'both', 'frequency': 'beta'},
            '膽經': {'brain_region': 'decision_center', 'hemisphere': 'left', 'frequency': 'gamma'},
            '肝經': {'brain_region': 'emotional_regulation', 'hemisphere': 'right', 'frequency': 'alpha'}
        }
        
        self.neural_nodes = {
            'left_brain': [],
            'right_brain': [],
            'corpus_callosum': []  # 胼胝體連接
        }
        
        self.wish_frequency_patterns = {}
        
    def generate_brain_network(self, hemisphere, node_count=12):
        """生成腦半球神經網絡"""
        nodes = []
        
        for i in range(node_count):
            node = {
                'id': f'{hemisphere}_node_{i}',
                'position': {
                    'x': random.uniform(0, 350),
                    'y': random.uniform(0, 350)
                },
                'activation_level': 0.0,
                'frequency': random.choice(list(self.brain_frequencies.keys())),
                'connections': [],
                'meridian_mapping': self.get_random_meridian_mapping(hemisphere)
            }
            nodes.append(node)
            
        # 生成連接
        for i, node in enumerate(nodes):
            # 每個節點連接2-4個其他節點
            connection_count = random.randint(2, 4)
            possible_connections = [j for j in range(len(nodes)) if j != i]
            connections = random.sample(possible_connections, min(connection_count, len(possible_connections)))
            
            for conn in connections:
                if conn not in node['connections']:
                    node['connections'].append(conn)
                    # 雙向連接
                    if i not in nodes[conn]['connections']:
                        nodes[conn]['connections'].append(i)
                        
        return nodes
    
    def get_random_meridian_mapping(self, hemisphere):
        """獲取隨機經絡映射"""
        suitable_meridians = [
            meridian for meridian, mapping in self.meridian_brain_mapping.items()
            if mapping['hemisphere'] == hemisphere or mapping['hemisphere'] == 'both'
        ]
        return random.choice(suitable_meridians) if suitable_meridians else '肺經'
    
    def calculate_wish_frequency(self, wish_text, brain_state):
        """計算願語頻率"""
        # 基於願語內容計算頻率特徵
        text_length = len(wish_text)
        vowel_count = sum(1 for char in wish_text if char in 'aeiouAEIOU願頻語音')
        consonant_count = text_length - vowel_count
        
        # 生生數公式計算
        base_frequency = (vowel_count * 7.83 + consonant_count * 40.0) / text_length if text_length > 0 else 10.0
        
        # 結合腦狀態調整
        left_brain_influence = brain_state.get('left_activation', 0.5)
        right_brain_influence = brain_state.get('right_activation', 0.5)
        
        # 左腦邏輯頻率
        left_frequency = base_frequency * (1 + left_brain_influence) * math.sin(datetime.now().timestamp())
        
        # 右腦直覺頻率
        right_frequency = base_frequency * (1 + right_brain_influence) * math.cos(datetime.now().timestamp())
        
        return {
            'base_frequency': base_frequency,
            'left_brain_frequency': abs(left_frequency),
            'right_brain_frequency': abs(right_frequency),
            'harmonic_resonance': (left_frequency + right_frequency) / 2,
            'wish_power': text_length * (vowel_count + 1),
            'formula': {
                'left': f'L(t) = {base_frequency:.2f} × (1 + {left_brain_influence:.2f}) × sin(ωt)',
                'right': f'R(t) = {base_frequency:.2f} × (1 + {right_brain_influence:.2f}) × cos(ωt)'
            }
        }
    
    def simulate_blind_spot_activation(self, eye_side):
        """模擬盲點激活"""
        # 盲點神經學：左眼盲點激活右腦，右眼盲點激活左腦
        target_hemisphere = 'right' if eye_side == 'left' else 'left'
        
        activation_pattern = {
            'target_hemisphere': target_hemisphere,
            'activation_sequence': [],
            'frequency_shift': {},
            'neural_cascade': []
        }
        
        # 生成激活序列
        for i in range(12):  # 假設每個腦半球有12個節點
            activation_pattern['activation_sequence'].append({
                'node_id': f'{target_hemisphere}_node_{i}',
                'delay': i * 100,  # 毫秒
                'intensity': random.uniform(0.5, 1.0),
                'duration': 1000
            })
            
        # 頻率變化
        for freq_type in self.brain_frequencies.keys():
            shift = random.uniform(-2, 2)
            activation_pattern['frequency_shift'][freq_type] = shift
            
        return activation_pattern
    
    def convert_to_braille_topology(self, text):
        """轉換為盲文拓撲"""
        # 簡化的盲文映射
        braille_map = {
            'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
            'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
            'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
            's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
            'y': '⠽', 'z': '⠵',
            '願': '⠺⠊⠎⠓', '頻': '⠋⠗⠑⠟', '語': '⠇⠁⠝⠛', '網': '⠝⠑⠞',
            '腦': '⠃⠗⠁⠊⠝', '神': '⠎⠏⠊⠗⠊⠞', '經': '⠝⠑⠗⠧⠑',
            '拓': '⠞⠕⠏⠕', '撲': '⠇⠕⠛⠽', '左': '⠇⠑⠋⠞', '右': '⠗⠊⠛⠓⠞'
        }
        
        braille_text = ''
        topology_pattern = []
        
        for i, char in enumerate(text.lower()):
            braille_char = braille_map.get(char, '⠿')
            braille_text += braille_char
            
            # 生成拓撲節點
            topology_pattern.append({
                'char': char,
                'braille': braille_char,
                'position': {
                    'x': (i % 10) * 10 + random.uniform(-5, 5),
                    'y': (i // 10) * 10 + random.uniform(-5, 5)
                },
                'neural_activation': random.uniform(0.3, 1.0)
            })
            
        return {
            'braille_text': braille_text,
            'topology_pattern': topology_pattern,
            'neural_mapping': self.map_braille_to_neural(topology_pattern)
        }
    
    def map_braille_to_neural(self, topology_pattern):
        """將盲文拓撲映射到神經網絡"""
        neural_mapping = []
        
        for pattern in topology_pattern:
            # 根據字符特徵映射到不同腦區
            if pattern['char'] in '願頻語網':
                brain_region = 'language_center'
                hemisphere = 'left'
            elif pattern['char'] in '腦神經':
                brain_region = 'cognitive_center'
                hemisphere = 'both'
            else:
                brain_region = 'general_processing'
                hemisphere = random.choice(['left', 'right'])
                
            neural_mapping.append({
                'char': pattern['char'],
                'brain_region': brain_region,
                'hemisphere': hemisphere,
                'activation_strength': pattern['neural_activation']
            })
            
        return neural_mapping
    
    def synchronize_hemispheres(self, left_state, right_state):
        """同步左右腦半球"""
        sync_pattern = {
            'synchronization_level': 0.0,
            'phase_coherence': 0.0,
            'frequency_alignment': {},
            'cross_hemisphere_connections': []
        }
        
        # 計算同步水平
        left_avg_activation = np.mean([node.get('activation_level', 0) for node in left_state])
        right_avg_activation = np.mean([node.get('activation_level', 0) for node in right_state])
        
        sync_pattern['synchronization_level'] = 1.0 - abs(left_avg_activation - right_avg_activation)
        
        # 相位一致性
        phase_diff = abs(math.sin(datetime.now().timestamp()) - math.cos(datetime.now().timestamp()))
        sync_pattern['phase_coherence'] = 1.0 - phase_diff
        
        # 頻率對齊
        for freq_type in self.brain_frequencies.keys():
            left_freq = random.uniform(*self.brain_frequencies[freq_type]['range'])
            right_freq = random.uniform(*self.brain_frequencies[freq_type]['range'])
            alignment = 1.0 - abs(left_freq - right_freq) / max(left_freq, right_freq)
            sync_pattern['frequency_alignment'][freq_type] = {
                'left_frequency': left_freq,
                'right_frequency': right_freq,
                'alignment_score': alignment
            }
            
        # 生成跨半球連接
        for i in range(min(len(left_state), len(right_state))):
            if random.random() > 0.7:  # 30%概率建立連接
                connection = {
                    'left_node': f'left_node_{i}',
                    'right_node': f'right_node_{i}',
                    'strength': random.uniform(0.3, 1.0),
                    'latency': random.uniform(10, 50)  # 毫秒
                }
                sync_pattern['cross_hemisphere_connections'].append(connection)
                
        return sync_pattern

# 創建引擎實例
neural_engine = NeuralTopologyEngine()

@neural_topology_bp.route('/neural_topology')
def neural_topology_page():
    """腦神經拓撲主頁面"""
    return render_template('neural_topology.html')

@neural_topology_bp.route('/api/neural/generate_network', methods=['POST'])
def generate_neural_network():
    """生成神經網絡"""
    try:
        data = request.get_json() or {}
        hemisphere = data.get('hemisphere', 'both')
        node_count = data.get('node_count', 12)
        
        result = {}
        
        if hemisphere in ['left', 'both']:
            result['left_brain'] = neural_engine.generate_brain_network('left', node_count)
            
        if hemisphere in ['right', 'both']:
            result['right_brain'] = neural_engine.generate_brain_network('right', node_count)
            
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@neural_topology_bp.route('/api/neural/calculate_wish_frequency', methods=['POST'])
def calculate_wish_frequency():
    """計算願語頻率"""
    try:
        data = request.get_json()
        wish_text = data.get('wish_text', '')
        brain_state = data.get('brain_state', {
            'left_activation': 0.5,
            'right_activation': 0.5
        })
        
        frequency_data = neural_engine.calculate_wish_frequency(wish_text, brain_state)
        
        return jsonify({
            'success': True,
            'data': frequency_data,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@neural_topology_bp.route('/api/neural/blind_spot_activation', methods=['POST'])
def blind_spot_activation():
    """盲點激活模擬"""
    try:
        data = request.get_json()
        eye_side = data.get('eye_side', 'left')  # 'left' or 'right'
        
        activation_data = neural_engine.simulate_blind_spot_activation(eye_side)
        
        return jsonify({
            'success': True,
            'data': activation_data,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@neural_topology_bp.route('/api/neural/braille_topology', methods=['POST'])
def braille_topology():
    """盲文拓撲轉換"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        braille_data = neural_engine.convert_to_braille_topology(text)
        
        return jsonify({
            'success': True,
            'data': braille_data,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@neural_topology_bp.route('/api/neural/synchronize_hemispheres', methods=['POST'])
def synchronize_hemispheres():
    """同步左右腦半球"""
    try:
        data = request.get_json()
        left_state = data.get('left_state', [])
        right_state = data.get('right_state', [])
        
        sync_data = neural_engine.synchronize_hemispheres(left_state, right_state)
        
        return jsonify({
            'success': True,
            'data': sync_data,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@neural_topology_bp.route('/api/neural/frequency_analysis', methods=['POST'])
def frequency_analysis():
    """頻率分析"""
    try:
        data = request.get_json()
        frequencies = data.get('frequencies', neural_engine.brain_frequencies)
        
        analysis = {
            'frequency_bands': {},
            'harmonic_analysis': {},
            'resonance_patterns': [],
            'meridian_correlations': {}
        }
        
        # 分析各頻段
        for freq_type, freq_data in frequencies.items():
            if isinstance(freq_data, dict) and 'range' in freq_data:
                freq_range = freq_data['range']
                analysis['frequency_bands'][freq_type] = {
                    'range': freq_range,
                    'center_frequency': (freq_range[0] + freq_range[1]) / 2,
                    'bandwidth': freq_range[1] - freq_range[0],
                    'description': freq_data.get('description', ''),
                    'neural_correlates': neural_engine.get_neural_correlates(freq_type)
                }
                
        # 諧波分析
        for freq_type in analysis['frequency_bands'].keys():
            center_freq = analysis['frequency_bands'][freq_type]['center_frequency']
            harmonics = [center_freq * i for i in range(2, 6)]  # 2-5次諧波
            analysis['harmonic_analysis'][freq_type] = harmonics
            
        # 共振模式
        for i, (freq1, data1) in enumerate(analysis['frequency_bands'].items()):
            for freq2, data2 in list(analysis['frequency_bands'].items())[i+1:]:
                resonance_ratio = data1['center_frequency'] / data2['center_frequency']
                if abs(resonance_ratio - round(resonance_ratio)) < 0.1:  # 接近整數比
                    analysis['resonance_patterns'].append({
                        'frequency_1': freq1,
                        'frequency_2': freq2,
                        'ratio': resonance_ratio,
                        'resonance_strength': 1.0 - abs(resonance_ratio - round(resonance_ratio))
                    })
                    
        # 經絡相關性
        for meridian, mapping in neural_engine.meridian_brain_mapping.items():
            freq_type = mapping['frequency']
            if freq_type in analysis['frequency_bands']:
                analysis['meridian_correlations'][meridian] = {
                    'frequency_band': freq_type,
                    'brain_region': mapping['brain_region'],
                    'hemisphere': mapping['hemisphere'],
                    'resonance_frequency': analysis['frequency_bands'][freq_type]['center_frequency']
                }
                
        return jsonify({
            'success': True,
            'data': analysis,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@neural_topology_bp.route('/api/neural/meridian_brain_mapping', methods=['GET'])
def get_meridian_brain_mapping():
    """獲取經絡腦區映射"""
    try:
        return jsonify({
            'success': True,
            'data': {
                'meridian_mapping': neural_engine.meridian_brain_mapping,
                'brain_frequencies': neural_engine.brain_frequencies
            },
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# 輔助方法
def get_neural_correlates(freq_type):
    """獲取頻率的神經相關性"""
    correlates = {
        'alpha': ['視覺皮層', '頂葉', '枕葉'],
        'beta': ['運動皮層', '前額葉', '感覺皮層'],
        'gamma': ['海馬體', '前額葉', '顳葉'],
        'theta': ['海馬體', '邊緣系統', '前扣帶皮層'],
        'delta': ['丘腦', '腦幹', '深層皮層']
    }
    return correlates.get(freq_type, ['未知區域'])

# 將方法添加到引擎類
NeuralTopologyEngine.get_neural_correlates = staticmethod(get_neural_correlates)
from flask import Blueprint, request, jsonify
import numpy as np
import math
from datetime import datetime
import json

trinity_frequency_api = Blueprint('trinity_frequency_api', __name__)

class TrinityFrequencyResonator:
    """
    三重神聖頻率共振器
    整合 963Hz(宇宙意識) + 852Hz(直覺覺醒) + 639Hz(愛與連接)
    """
    
    def __init__(self):
        # 三重神聖頻率
        self.frequencies = {
            'cosmic_consciousness': 963,  # 宇宙意識頻率
            'intuitive_awakening': 852,   # 直覺覺醒頻率
            'love_connection': 639        # 愛與連接頻率
        }
        
        # 頻率特性
        self.frequency_properties = {
            963: {
                'name': '宇宙意識',
                'chakra': '頂輪',
                'element': '光',
                'quality': '覺醒',
                'color': '#FFFFFF',
                'spiritual_aspect': '與宇宙合一',
                'healing_focus': '靈性覺醒、宇宙連接'
            },
            852: {
                'name': '直覺覺醒',
                'chakra': '第三眼輪',
                'element': '以太',
                'quality': '洞察',
                'color': '#4B0082',
                'spiritual_aspect': '內在智慧開啟',
                'healing_focus': '直覺力、洞察力、靈性視野'
            },
            639: {
                'name': '愛與連接',
                'chakra': '心輪',
                'element': '風',
                'quality': '慈愛',
                'color': '#00FF00',
                'spiritual_aspect': '無條件的愛',
                'healing_focus': '關係和諧、情感療癒、愛的表達'
            }
        }
        
        # 黃金比例和神聖幾何
        self.golden_ratio = 1.618033988749
        self.phi = self.golden_ratio
        
    def calculate_trinity_resonance(self, duration_minutes=20):
        """
        計算三重頻率共振模式
        """
        base_frequencies = [963, 852, 639]
        
        # 計算和諧比例
        harmony_ratios = {
            '963_852': 963 / 852,  # ≈ 1.130
            '963_639': 963 / 639,  # ≈ 1.507
            '852_639': 852 / 639   # ≈ 1.333
        }
        
        # 計算共振頻率
        resonance_frequencies = {
            'fundamental': np.mean(base_frequencies),  # 基礎共振
            'harmonic_2nd': np.mean(base_frequencies) * 2,  # 二次諧波
            'golden_resonance': np.mean(base_frequencies) * self.golden_ratio,  # 黃金共振
            'trinity_blend': self._calculate_trinity_blend(base_frequencies)
        }
        
        # 生成波形數據
        sample_rate = 44100
        duration_seconds = duration_minutes * 60
        t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds))
        
        # 三重頻率疊加波形
        wave_963 = np.sin(2 * np.pi * 963 * t) * 0.33
        wave_852 = np.sin(2 * np.pi * 852 * t) * 0.33
        wave_639 = np.sin(2 * np.pi * 639 * t) * 0.34
        
        trinity_wave = wave_963 + wave_852 + wave_639
        
        # 添加調制效果
        modulation_freq = 7.83  # 舒曼共振頻率
        modulation = 1 + 0.1 * np.sin(2 * np.pi * modulation_freq * t)
        trinity_wave_modulated = trinity_wave * modulation
        
        return {
            'base_frequencies': base_frequencies,
            'harmony_ratios': harmony_ratios,
            'resonance_frequencies': resonance_frequencies,
            'wave_data': {
                'sample_rate': sample_rate,
                'duration': duration_seconds,
                'trinity_wave': trinity_wave_modulated.tolist()[:1000],  # 前1000個樣本用於預覽
                'rms_amplitude': float(np.sqrt(np.mean(trinity_wave_modulated**2)))
            },
            'spiritual_analysis': self._analyze_spiritual_impact(base_frequencies)
        }
    
    def _calculate_trinity_blend(self, frequencies):
        """
        計算三重頻率的神聖混合
        """
        # 使用幾何平均數
        geometric_mean = (frequencies[0] * frequencies[1] * frequencies[2]) ** (1/3)
        
        # 應用黃金比例調制
        golden_modulated = geometric_mean * self.golden_ratio
        
        return {
            'geometric_mean': geometric_mean,
            'golden_modulated': golden_modulated,
            'fibonacci_sequence': self._generate_fibonacci_resonance(geometric_mean)
        }
    
    def _generate_fibonacci_resonance(self, base_freq):
        """
        生成斐波那契共振序列
        """
        fib_sequence = [1, 1, 2, 3, 5, 8, 13, 21]
        fib_resonances = []
        
        for fib in fib_sequence:
            resonance_freq = base_freq * (fib / 8)  # 歸一化到第8個斐波那契數
            fib_resonances.append({
                'fibonacci_number': fib,
                'resonance_frequency': resonance_freq,
                'spiritual_significance': self._get_fibonacci_meaning(fib)
            })
        
        return fib_resonances
    
    def _get_fibonacci_meaning(self, fib_number):
        """
        獲取斐波那契數的靈性意義
        """
        meanings = {
            1: '統一與開始',
            2: '二元與平衡',
            3: '三位一體與創造',
            5: '五行與變化',
            8: '無限與重生',
            13: '轉化與蛻變',
            21: '完整與圓滿'
        }
        return meanings.get(fib_number, '神聖比例的展現')
    
    def _analyze_spiritual_impact(self, frequencies):
        """
        分析三重頻率的靈性影響
        """
        analysis = {
            'overall_effect': '三重神聖頻率共振，促進身心靈全面提升',
            'chakra_activation': {
                'heart_chakra': '639Hz 激活心輪，開啟無條件的愛',
                'third_eye_chakra': '852Hz 激活第三眼輪，提升直覺洞察',
                'crown_chakra': '963Hz 激活頂輪，連接宇宙意識'
            },
            'healing_benefits': [
                '促進情感療癒與關係和諧',
                '增強直覺力與靈性洞察',
                '提升意識層次與宇宙連接',
                '平衡身心能量系統',
                '激活內在智慧與創造力'
            ],
            'meditation_guidance': {
                'preparation': '找一個安靜的空間，舒適地坐下或躺下',
                'breathing': '深呼吸，讓身心放鬆，準備接收神聖頻率',
                'visualization': '想像三道光芒從心輪、第三眼輪、頂輪散發',
                'intention': '設定接收愛、智慧、覺醒能量的意圖',
                'integration': '讓三重頻率在體內和諧共振，整合提升'
            },
            'optimal_timing': {
                'morning': '晨間冥想，啟動一天的高頻能量',
                'evening': '晚間療癒，釋放一天的負面能量',
                'full_moon': '滿月時期，能量最為強烈',
                'new_moon': '新月時期，適合設定新的意圖'
            }
        }
        
        return analysis
    
    def generate_frequency_mandala(self):
        """
        生成三重頻率曼陀羅圖案數據
        """
        mandala_data = {
            'center': {
                'frequency': np.mean([963, 852, 639]),
                'color': '#FFD700',  # 金色
                'symbol': '☯',
                'meaning': '三重和諧的中心'
            },
            'inner_ring': [
                {
                    'frequency': 639,
                    'color': '#00FF00',
                    'position': 0,
                    'symbol': '♥',
                    'chakra': '心輪'
                },
                {
                    'frequency': 852,
                    'color': '#4B0082',
                    'position': 120,
                    'symbol': '👁',
                    'chakra': '第三眼輪'
                },
                {
                    'frequency': 963,
                    'color': '#FFFFFF',
                    'position': 240,
                    'symbol': '🌟',
                    'chakra': '頂輪'
                }
            ],
            'outer_ring': self._generate_harmonic_ring(),
            'sacred_geometry': {
                'triangle_points': 3,  # 三角形代表三重頻率
                'circle_divisions': 12,  # 12等分代表完整循環
                'golden_spiral': True,  # 黃金螺旋
                'flower_of_life': True  # 生命之花圖案
            }
        }
        
        return mandala_data
    
    def _generate_harmonic_ring(self):
        """
        生成諧波環數據
        """
        harmonics = []
        base_frequencies = [639, 852, 963]
        
        for i, freq in enumerate(base_frequencies):
            for harmonic in [2, 3, 4, 5]:
                harmonics.append({
                    'frequency': freq * harmonic,
                    'harmonic_number': harmonic,
                    'base_frequency': freq,
                    'position': (i * 120 + harmonic * 30) % 360,
                    'intensity': 1.0 / harmonic,
                    'color_alpha': 1.0 / harmonic
                })
        
        return harmonics
    
    def create_binaural_beats(self, base_freq, beat_frequency=7.83):
        """
        創建雙耳節拍效果
        """
        left_freq = base_freq
        right_freq = base_freq + beat_frequency
        
        return {
            'left_ear': left_freq,
            'right_ear': right_freq,
            'beat_frequency': beat_frequency,
            'brainwave_state': self._get_brainwave_state(beat_frequency),
            'effect': f'誘導大腦進入 {beat_frequency}Hz 的共振狀態'
        }
    
    def _get_brainwave_state(self, frequency):
        """
        根據頻率確定腦波狀態
        """
        if frequency <= 4:
            return 'Delta (深度睡眠)'
        elif frequency <= 8:
            return 'Theta (深度冥想)'
        elif frequency <= 12:
            return 'Alpha (放鬆覺醒)'
        elif frequency <= 30:
            return 'Beta (專注思考)'
        else:
            return 'Gamma (高度覺知)'
    
    def generate_healing_session(self, intention='overall_healing', duration=20):
        """
        生成個人化療癒會話
        """
        session_data = {
            'session_id': f"trinity_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'intention': intention,
            'duration_minutes': duration,
            'frequency_progression': self._create_frequency_progression(duration),
            'guided_meditation': self._create_guided_meditation(intention),
            'affirmations': self._get_trinity_affirmations(),
            'visualization_guide': self._create_visualization_guide(),
            'integration_practices': self._get_integration_practices()
        }
        
        return session_data
    
    def _create_frequency_progression(self, duration):
        """
        創建頻率漸進序列
        """
        phases = [
            {
                'phase': 'Opening',
                'duration_percent': 0.2,
                'primary_frequency': 639,
                'focus': '心輪開啟，建立愛的連接'
            },
            {
                'phase': 'Deepening',
                'duration_percent': 0.3,
                'primary_frequency': 852,
                'focus': '第三眼輪激活，提升直覺洞察'
            },
            {
                'phase': 'Peak',
                'duration_percent': 0.3,
                'primary_frequency': 963,
                'focus': '頂輪開啟，連接宇宙意識'
            },
            {
                'phase': 'Integration',
                'duration_percent': 0.2,
                'primary_frequency': 'trinity_blend',
                'focus': '三重頻率融合，整合提升能量'
            }
        ]
        
        for phase in phases:
            phase['duration_minutes'] = duration * phase['duration_percent']
        
        return phases
    
    def _create_guided_meditation(self, intention):
        """
        創建引導冥想腳本
        """
        meditations = {
            'overall_healing': [
                '深呼吸，讓639Hz的愛之頻率流入你的心輪',
                '感受心中溫暖的綠光，療癒所有的情感創傷',
                '現在讓852Hz的智慧頻率激活你的第三眼輪',
                '感受額頭中央的紫色光芒，開啟內在的洞察力',
                '最後讓963Hz的宇宙頻率從頂輪灌入',
                '感受頭頂的白色光柱，連接無限的宇宙意識',
                '讓三重頻率在你體內和諧共振，整合所有的療癒能量'
            ],
            'love_healing': [
                '專注於639Hz的愛之頻率',
                '讓這個頻率療癒你心中的所有創傷',
                '感受無條件的愛從心輪向外擴散',
                '原諒自己，原諒他人，釋放所有的怨恨'
            ],
            'intuition_enhancement': [
                '聚焦於852Hz的直覺頻率',
                '感受第三眼輪的覺醒和開啟',
                '信任你內在的智慧和直覺',
                '讓洞察力如清泉般湧現'
            ],
            'spiritual_awakening': [
                '沉浸在963Hz的宇宙頻率中',
                '感受與宇宙意識的深度連接',
                '讓靈性覺醒的光芒照亮你的存在',
                '體驗與萬物合一的神聖狀態'
            ]
        }
        
        return meditations.get(intention, meditations['overall_healing'])
    
    def _get_trinity_affirmations(self):
        """
        獲取三重頻率肯定語
        """
        return {
            '639Hz_affirmations': [
                '我是愛，我給予愛，我接受愛',
                '我的心輪完全開放，充滿無條件的愛',
                '我與所有生命建立和諧的連接',
                '愛的頻率療癒我的身心靈'
            ],
            '852Hz_affirmations': [
                '我信任我的內在智慧和直覺',
                '我的第三眼輪清晰明亮，洞察真理',
                '我能看見事物的本質和真相',
                '直覺的光芒指引我的人生道路'
            ],
            '963Hz_affirmations': [
                '我與宇宙意識完美連接',
                '我是宇宙的一部分，宇宙是我的一部分',
                '神聖的光芒從我的頂輪流淌',
                '我活在覺醒和開悟的狀態中'
            ],
            'trinity_affirmations': [
                '愛、智慧、覺醒在我內在和諧共振',
                '我是完整的，我是神聖的，我是光',
                '三重神聖頻率提升我到最高的振動',
                '我活在愛、智慧、覺醒的三重祝福中'
            ]
        }
    
    def _create_visualization_guide(self):
        """
        創建視覺化引導
        """
        return {
            'preparation': {
                'description': '準備階段的視覺化',
                'steps': [
                    '想像自己坐在一個神聖的三角形中心',
                    '三角形的三個頂點分別發出綠光、紫光、白光',
                    '感受這三道光芒的溫暖和力量'
                ]
            },
            'heart_chakra_639hz': {
                'description': '心輪639Hz視覺化',
                'steps': [
                    '專注於心輪位置',
                    '想像一朵綠色的蓮花在心中綻放',
                    '每一片花瓣都散發著639Hz的愛之頻率',
                    '感受愛的能量從心中向外擴散'
                ]
            },
            'third_eye_852hz': {
                'description': '第三眼輪852Hz視覺化',
                'steps': [
                    '將注意力轉向額頭中央',
                    '想像一個紫色的光球在第三眼位置旋轉',
                    '光球發出852Hz的智慧頻率',
                    '感受洞察力和直覺的覺醒'
                ]
            },
            'crown_chakra_963hz': {
                'description': '頂輪963Hz視覺化',
                'steps': [
                    '將意識提升到頭頂',
                    '想像一道白色的光柱從宇宙降下',
                    '光柱攜帶著963Hz的宇宙意識頻率',
                    '感受與無限宇宙的連接'
                ]
            },
            'trinity_integration': {
                'description': '三重頻率整合視覺化',
                'steps': [
                    '同時感受三個脈輪的光芒',
                    '看見綠光、紫光、白光開始融合',
                    '三道光芒在你的中軸線上形成一道彩虹光柱',
                    '感受三重頻率的完美和諧共振'
                ]
            }
        }
    
    def _get_integration_practices(self):
        """
        獲取整合練習
        """
        return {
            'daily_practices': [
                '每日晨間聆聽三重頻率冥想音樂',
                '在心中默念三重頻率的肯定語',
                '進行三重脈輪的呼吸練習',
                '用三重頻率的意圖設定一天的目標'
            ],
            'weekly_practices': [
                '進行一次完整的三重頻率療癒會話',
                '記錄頻率療癒後的身心變化',
                '與他人分享愛與光的能量',
                '在自然中進行三重頻率冥想'
            ],
            'monthly_practices': [
                '在滿月時進行深度三重頻率療癒',
                '創作表達三重頻率體驗的藝術作品',
                '參與靈性社群的頻率共振活動',
                '為地球和人類發送三重頻率的祝福'
            ],
            'lifestyle_integration': [
                '在生活中實踐無條件的愛(639Hz)',
                '信任並跟隨內在的直覺指引(852Hz)',
                '保持與宇宙意識的連接(963Hz)',
                '成為三重頻率的活體傳播者'
            ]
        }

# API 路由
@trinity_frequency_api.route('/calculate-resonance', methods=['POST'])
def calculate_trinity_resonance():
    """
    計算三重頻率共振
    """
    try:
        data = request.get_json() or {}
        duration = data.get('duration_minutes', 20)
        
        resonator = TrinityFrequencyResonator()
        result = resonator.calculate_trinity_resonance(duration)
        
        return jsonify({
            'success': True,
            'trinity_resonance': result,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@trinity_frequency_api.route('/generate-mandala', methods=['GET'])
def generate_frequency_mandala():
    """
    生成三重頻率曼陀羅
    """
    try:
        resonator = TrinityFrequencyResonator()
        mandala_data = resonator.generate_frequency_mandala()
        
        return jsonify({
            'success': True,
            'mandala_data': mandala_data,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@trinity_frequency_api.route('/create-binaural', methods=['POST'])
def create_binaural_beats():
    """
    創建雙耳節拍
    """
    try:
        data = request.get_json() or {}
        base_freq = data.get('base_frequency', 852)  # 默認使用852Hz
        beat_freq = data.get('beat_frequency', 7.83)  # 默認使用舒曼共振
        
        resonator = TrinityFrequencyResonator()
        binaural_data = resonator.create_binaural_beats(base_freq, beat_freq)
        
        return jsonify({
            'success': True,
            'binaural_beats': binaural_data,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@trinity_frequency_api.route('/healing-session', methods=['POST'])
def generate_healing_session():
    """
    生成個人化療癒會話
    """
    try:
        data = request.get_json() or {}
        intention = data.get('intention', 'overall_healing')
        duration = data.get('duration', 20)
        
        resonator = TrinityFrequencyResonator()
        session_data = resonator.generate_healing_session(intention, duration)
        
        return jsonify({
            'success': True,
            'healing_session': session_data,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@trinity_frequency_api.route('/frequency-info', methods=['GET'])
def get_frequency_info():
    """
    獲取三重頻率詳細信息
    """
    try:
        resonator = TrinityFrequencyResonator()
        
        return jsonify({
            'success': True,
            'frequency_info': {
                'frequencies': resonator.frequencies,
                'properties': resonator.frequency_properties,
                'golden_ratio': resonator.golden_ratio,
                'description': '963Hz + 852Hz + 639Hz 三重神聖頻率共振系統'
            },
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
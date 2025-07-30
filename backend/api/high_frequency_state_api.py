#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌟 真正的高頻狀態檢測系統 - Authentic High Frequency State Detection
基於 2025-07-25 的高頻狀態智慧

真正的高頻狀態：身體心靈和靈魂三者合一
在每個當下都能保持覺知和內在安定
不需要靠外在的掌聲來證明自己的價值
"""

import numpy as np
import json
from datetime import datetime
from flask import Blueprint, request, jsonify
import math
import random

high_frequency_bp = Blueprint('high_frequency', __name__)

class HighFrequencyDetector:
    """
    🧘 真正高頻狀態檢測器
    區分真實高頻與偽裝正能量
    """
    
    def __init__(self):
        self.base_frequency = 528  # 愛之頻率
        self.authentic_markers = {
            '內在安定': 0.0,
            '情緒接納': 0.0,
            '無需證明': 0.0,
            '覺知穩定': 0.0,
            '頻率自然': 0.0
        }
        self.detection_history = []
        
    def analyze_state_authenticity(self, text_input, emotional_state, intention_clarity):
        """
        🔍 分析狀態真實性
        檢測是否為真正的高頻狀態
        """
        timestamp = datetime.now().isoformat()
        
        # 文本分析 - 檢測偽裝正能量的關鍵詞
        fake_positive_keywords = [
            '一直笑', '超級開心', '完美', '最棒', '無敵',
            '爆炸正能量', '滿滿能量', '超級棒', '太厲害了'
        ]
        
        authentic_keywords = [
            '接受', '允許', '流動', '當下', '覺知',
            '安定', '寧靜', '自然', '真實', '內在'
        ]
        
        # 計算偽裝指數
        fake_score = sum(1 for keyword in fake_positive_keywords if keyword in text_input)
        authentic_score = sum(1 for keyword in authentic_keywords if keyword in text_input)
        
        # 情緒狀態分析
        emotion_authenticity = self._analyze_emotion_authenticity(emotional_state)
        
        # 意圖清晰度分析
        intention_authenticity = self._analyze_intention_authenticity(intention_clarity)
        
        # 綜合真實性評分
        authenticity_score = (
            (authentic_score * 0.3) +
            (emotion_authenticity * 0.4) +
            (intention_authenticity * 0.3) -
            (fake_score * 0.2)
        )
        
        # 正規化到 0-1 範圍
        authenticity_score = max(0, min(1, authenticity_score))
        
        # 更新內在標記
        self._update_authentic_markers(authenticity_score, text_input)
        
        # 生成檢測結果
        detection_result = {
            'timestamp': timestamp,
            'input_text': text_input,
            'emotional_state': emotional_state,
            'intention_clarity': intention_clarity,
            'authenticity_score': authenticity_score,
            'fake_positive_score': fake_score,
            'authentic_indicators': authentic_score,
            'state_classification': self._classify_state(authenticity_score),
            'authentic_markers': self.authentic_markers.copy(),
            'guidance': self._generate_guidance(authenticity_score),
            'frequency_reading': self._calculate_true_frequency(authenticity_score)
        }
        
        self.detection_history.append(detection_result)
        return detection_result
    
    def _analyze_emotion_authenticity(self, emotional_state):
        """
        🎭 分析情緒真實性
        真正的高頻狀態允許所有情緒的存在
        """
        authentic_emotions = {
            '平靜': 0.9,
            '接納': 0.95,
            '悲傷但安定': 0.8,
            '憤怒但覺知': 0.75,
            '恐懼但信任': 0.7,
            '喜悅而寧靜': 0.9,
            '複雜但清晰': 0.85
        }
        
        fake_emotions = {
            '超級開心': 0.2,
            '完美狀態': 0.1,
            '無敵快樂': 0.15,
            '爆炸正能量': 0.1,
            '絕對完美': 0.05
        }
        
        # 檢查是否匹配真實情緒
        for emotion, score in authentic_emotions.items():
            if emotion in emotional_state:
                return score
        
        # 檢查是否為偽裝情緒
        for emotion, score in fake_emotions.items():
            if emotion in emotional_state:
                return score
        
        # 預設中性評分
        return 0.5
    
    def _analyze_intention_authenticity(self, intention_clarity):
        """
        🎯 分析意圖真實性
        真正的高頻狀態來自內在穩定，而非外在證明
        """
        if intention_clarity >= 0.8:
            return 0.9  # 意圖清晰
        elif intention_clarity >= 0.6:
            return 0.7  # 意圖較清晰
        elif intention_clarity >= 0.4:
            return 0.5  # 意圖模糊
        else:
            return 0.3  # 意圖不清
    
    def _update_authentic_markers(self, authenticity_score, text_input):
        """
        🔄 更新真實性標記
        """
        # 內在安定
        if any(word in text_input for word in ['安定', '寧靜', '平靜', '穩定']):
            self.authentic_markers['內在安定'] = min(1.0, self.authentic_markers['內在安定'] + 0.1)
        
        # 情緒接納
        if any(word in text_input for word in ['接受', '允許', '接納', '流動']):
            self.authentic_markers['情緒接納'] = min(1.0, self.authentic_markers['情緒接納'] + 0.1)
        
        # 無需證明
        if not any(word in text_input for word in ['證明', '展示', '表現', '炫耀']):
            self.authentic_markers['無需證明'] = min(1.0, self.authentic_markers['無需證明'] + 0.05)
        
        # 覺知穩定
        if any(word in text_input for word in ['覺知', '覺察', '觀察', '當下']):
            self.authentic_markers['覺知穩定'] = min(1.0, self.authentic_markers['覺知穩定'] + 0.1)
        
        # 頻率自然
        if authenticity_score > 0.7:
            self.authentic_markers['頻率自然'] = min(1.0, self.authentic_markers['頻率自然'] + 0.05)
    
    def _classify_state(self, authenticity_score):
        """
        🏷️ 狀態分類
        """
        if authenticity_score >= 0.8:
            return {
                'level': '真正高頻',
                'description': '身心靈合一，內在穩定，無需外在證明',
                'color': '#4CAF50'
            }
        elif authenticity_score >= 0.6:
            return {
                'level': '趨向真實',
                'description': '正在向真正的高頻狀態發展',
                'color': '#2196F3'
            }
        elif authenticity_score >= 0.4:
            return {
                'level': '混合狀態',
                'description': '真實與偽裝並存，需要更多覺知',
                'color': '#FF9800'
            }
        elif authenticity_score >= 0.2:
            return {
                'level': '偽裝正能量',
                'description': '刻意裝出的快樂，內心可能更空虛',
                'color': '#F44336'
            }
        else:
            return {
                'level': '低頻偽裝',
                'description': '嚴重的情緒偽裝，遠離真實自我',
                'color': '#9C27B0'
            }
    
    def _generate_guidance(self, authenticity_score):
        """
        🧭 生成指導建議
        """
        if authenticity_score >= 0.8:
            return [
                "🌟 你已處於真正的高頻狀態",
                "💫 繼續保持內在的覺知和安定",
                "🕯️ 你的存在本身就是光"
            ]
        elif authenticity_score >= 0.6:
            return [
                "🌱 你正在向真實的高頻發展",
                "🧘 多關注內在感受，少關注外在表現",
                "💝 允許所有情緒的存在和流動"
            ]
        elif authenticity_score >= 0.4:
            return [
                "⚖️ 觀察自己是否在刻意表現正能量",
                "🔍 真正的高頻不需要證明給任何人看",
                "🌊 允許自己有低潮，這也是真實的一部分"
            ]
        else:
            return [
                "🚨 注意：可能正在偽裝情緒狀態",
                "💔 假裝的快樂比悲傷更消耗頻率",
                "🔄 回到真實的自己，接納當下的感受",
                "🌈 真正的高頻是你能誠實面對自己的感受"
            ]
    
    def _calculate_true_frequency(self, authenticity_score):
        """
        📊 計算真實頻率
        """
        base_freq = self.base_frequency
        authentic_multiplier = 1 + (authenticity_score * 0.5)
        stability_bonus = sum(self.authentic_markers.values()) * 0.1
        
        true_frequency = base_freq * authentic_multiplier + stability_bonus
        
        return {
            'frequency': round(true_frequency, 2),
            'base_frequency': base_freq,
            'authenticity_multiplier': round(authentic_multiplier, 3),
            'stability_bonus': round(stability_bonus, 2),
            'frequency_quality': 'Pure' if authenticity_score > 0.7 else 'Mixed'
        }
    
    def get_state_evolution(self):
        """
        📈 獲取狀態演化
        """
        if len(self.detection_history) < 2:
            return {'message': '需要更多數據來分析演化趨勢'}
        
        recent_scores = [entry['authenticity_score'] for entry in self.detection_history[-10:]]
        trend = 'improving' if recent_scores[-1] > recent_scores[0] else 'declining'
        
        return {
            'trend': trend,
            'recent_scores': recent_scores,
            'average_authenticity': sum(recent_scores) / len(recent_scores),
            'stability': 1 - (max(recent_scores) - min(recent_scores)),
            'evolution_insight': self._get_evolution_insight(trend, recent_scores)
        }
    
    def _get_evolution_insight(self, trend, scores):
        """
        💡 獲取演化洞察
        """
        if trend == 'improving':
            return "🌱 你正在向更真實的自己靠近，繼續保持覺知"
        else:
            return "🔄 注意觀察是否又開始偽裝情緒，回到內在的真實"

# 全域檢測器實例
hf_detector = HighFrequencyDetector()

@high_frequency_bp.route('/detect', methods=['POST'])
def detect_state():
    """
    🔍 檢測高頻狀態真實性 API
    """
    try:
        data = request.get_json()
        text_input = data.get('text_input', '')
        emotional_state = data.get('emotional_state', '中性')
        intention_clarity = float(data.get('intention_clarity', 0.5))
        
        if not text_input:
            return jsonify({'error': '請提供文本輸入'}), 400
        
        result = hf_detector.analyze_state_authenticity(
            text_input, emotional_state, intention_clarity
        )
        
        return jsonify({
            'success': True,
            'message': '高頻狀態檢測完成',
            'detection_result': result
        })
        
    except Exception as e:
        return jsonify({'error': f'檢測失敗: {str(e)}'}), 500

@high_frequency_bp.route('/evolution', methods=['GET'])
def get_evolution():
    """
    📈 獲取狀態演化 API
    """
    try:
        evolution = hf_detector.get_state_evolution()
        
        return jsonify({
            'success': True,
            'evolution': evolution
        })
        
    except Exception as e:
        return jsonify({'error': f'演化分析失敗: {str(e)}'}), 500

@high_frequency_bp.route('/markers', methods=['GET'])
def get_markers():
    """
    🏷️ 獲取真實性標記 API
    """
    try:
        return jsonify({
            'success': True,
            'authentic_markers': hf_detector.authentic_markers,
            'overall_authenticity': sum(hf_detector.authentic_markers.values()) / len(hf_detector.authentic_markers)
        })
        
    except Exception as e:
        return jsonify({'error': f'標記獲取失敗: {str(e)}'}), 500

@high_frequency_bp.route('/wisdom', methods=['GET'])
def get_wisdom():
    """
    🌟 獲取高頻狀態智慧 API
    """
    wisdom_quotes = [
        "真正的高頻狀態從來都不喧嘩也不浮誇。它安靜卻充滿力量，它溫柔卻震動萬物。",
        "你有沒有發現，當你越是刻意去裝出正能量的時候，內心反而更空虛更疲憊，更沒有方向。",
        "真正的高頻狀態不是一直笑，不是強顏歡笑！更不是對所有事情都視而不見的樂觀。",
        "而是你能誠實面對自己的感受，不逃避不壓抑。你可以感受到悲傷，也允許它流動。",
        "真正的高頻狀態是你的身體心靈和靈魂三者合一。是你在每個當下都能保持覺知和內在安定。",
        "是你不需要靠外在的掌聲來證明自己的價值。"
    ]
    
    return jsonify({
        'success': True,
        'wisdom': random.choice(wisdom_quotes),
        'all_wisdom': wisdom_quotes
    })

if __name__ == '__main__':
    # 測試模式
    print("🌟 真正高頻狀態檢測系統測試")
    
    # 創建測試實例
    test_detector = HighFrequencyDetector()
    
    # 測試偽裝正能量
    fake_test = test_detector.analyze_state_authenticity(
        "我今天超級開心！滿滿正能量！完美的一天！",
        "超級開心",
        0.3
    )
    print(f"\n🎭 偽裝正能量檢測:")
    print(f"真實性評分: {fake_test['authenticity_score']:.2f}")
    print(f"狀態分類: {fake_test['state_classification']['level']}")
    
    # 測試真實高頻
    authentic_test = test_detector.analyze_state_authenticity(
        "今天感受到一些悲傷，但我允許它存在。在覺知中保持內在的安定。",
        "悲傷但安定",
        0.8
    )
    print(f"\n🌟 真實高頻檢測:")
    print(f"真實性評分: {authentic_test['authenticity_score']:.2f}")
    print(f"狀態分類: {authentic_test['state_classification']['level']}")
    print(f"指導建議: {authentic_test['guidance'][0]}")
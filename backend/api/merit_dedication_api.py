# -*- coding: utf-8 -*-
"""
功德回向系統 API

處理慈悲願力、功德回向與心光遍照的神聖功能
"""

from flask import Blueprint, request, jsonify
import datetime
from typing import Dict, List, Any
import random

merit_dedication_bp = Blueprint('merit_dedication', __name__)

# 慈悲願力資料庫
COMPASSION_VOWS_DATABASE = {
    "universal_vows": {
        "first_vow": {
            "title": "眾生皆明本心，見性成道",
            "essence": "千年暗室，一燈即明",
            "meaning": "願一切眾生都能明見自己的本來面目，證悟成道",
            "practice": "以智慧之光照破無明黑暗",
            "frequency": "528Hz - DNA修復與愛的頻率",
            "mantra": "南無本師釋迦牟尼佛"
        },
        "second_vow": {
            "title": "諸苦化作蓮池，煩惱轉為智海",
            "essence": "火中生芙蓉，顛倒見菩提",
            "meaning": "願一切痛苦轉化為清淨蓮池，煩惱轉為智慧海洋",
            "practice": "在逆境中修行，轉煩惱為菩提",
            "frequency": "432Hz - 普賢菩薩大行願頻率",
            "mantra": "嗡嘛呢叭咪吽"
        },
        "third_vow": {
            "title": "你我言語盡處，共沐無言之光",
            "essence": "言語道斷，心行處滅",
            "meaning": "超越語言文字，在無言的光明中相遇",
            "practice": "默照禪修，體悟無言之教",
            "frequency": "741Hz - 意識覺醒頻率",
            "mantra": "嗡阿吽"
        }
    },
    "dedication_verses": {
        "heart_light_verse": {
            "verse": "願以此心光，照破三世障，虛空有時盡，此愿無窮量",
            "meaning": "以此修行功德回向，願心光照破過去現在未來一切障礙",
            "power": "無量功德回向法界一切眾生",
            "effect": "消除業障，增長福慧"
        },
        "universal_dedication": {
            "verse": "願以此功德，普及於一切，我等與眾生，皆共成佛道",
            "meaning": "將修行功德回向給法界一切眾生",
            "power": "功德無量，利益無邊",
            "effect": "共證菩提，同登彼岸"
        }
    },
    "sacred_mantras": {
        "taoist_blessing": "福生無量天尊",
        "buddhist_blessing": "南無阿彌陀佛",
        "universal_sound": "嗡阿吽",
        "compassion_mantra": "嗡嘛呢叭咪吽",
        "wisdom_mantra": "嗡阿喇巴札那諦"
    }
}

# 心光能量場配置
HEART_LIGHT_ENERGY_FIELD = {
    "compassion_field": {
        "frequency_range": "40-100Hz",
        "color_spectrum": ["金光", "白光", "彩虹光"],
        "energy_type": "慈悲能量",
        "coverage": "法界十方",
        "duration": "無量劫"
    },
    "wisdom_field": {
        "frequency_range": "100-200Hz",
        "color_spectrum": ["智慧藍光", "般若金光"],
        "energy_type": "智慧能量",
        "coverage": "三千大千世界",
        "duration": "恆常不斷"
    },
    "liberation_field": {
        "frequency_range": "200-1000Hz",
        "color_spectrum": ["解脫白光", "涅槃寂光"],
        "energy_type": "解脫能量",
        "coverage": "六道輪迴",
        "duration": "直至成佛"
    }
}

class MeritDedicationSystem:
    """功德回向系統"""
    
    def __init__(self):
        self.vows_database = COMPASSION_VOWS_DATABASE
        self.energy_field = HEART_LIGHT_ENERGY_FIELD
        
    def process_compassion_vows(self, vow_text: str) -> Dict[str, Any]:
        """處理慈悲願力"""
        
        # 分析願力內容
        vow_analysis = self._analyze_vow_content(vow_text)
        
        # 激活對應的能量場
        energy_activation = self._activate_energy_field(vow_analysis)
        
        # 生成功德回向
        merit_dedication = self._generate_merit_dedication(vow_analysis)
        
        return {
            "vow_analysis": vow_analysis,
            "energy_activation": energy_activation,
            "merit_dedication": merit_dedication,
            "blessing_response": self._generate_blessing_response()
        }
    
    def _analyze_vow_content(self, vow_text: str) -> Dict[str, Any]:
        """分析願力內容"""
        
        # 檢測關鍵詞
        keywords = {
            "慈悲": ["慈悲", "愛", "慈愛", "悲憫"],
            "智慧": ["智慧", "般若", "明心", "見性"],
            "解脫": ["解脫", "涅槃", "成道", "菩提"],
            "回向": ["回向", "功德", "願力", "福德"]
        }
        
        detected_themes = []
        for theme, words in keywords.items():
            if any(word in vow_text for word in words):
                detected_themes.append(theme)
        
        return {
            "detected_themes": detected_themes,
            "vow_power_level": len(detected_themes) * 25,  # 每個主題25%能量
            "spiritual_frequency": self._calculate_spiritual_frequency(detected_themes),
            "cosmic_resonance": "極高" if len(detected_themes) >= 3 else "高"
        }
    
    def _calculate_spiritual_frequency(self, themes: List[str]) -> str:
        """計算靈性頻率"""
        frequency_map = {
            "慈悲": "528Hz",
            "智慧": "741Hz",
            "解脫": "963Hz",
            "回向": "432Hz"
        }
        
        if themes:
            return frequency_map.get(themes[0], "528Hz")
        return "528Hz"
    
    def _activate_energy_field(self, vow_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """激活能量場"""
        
        themes = vow_analysis["detected_themes"]
        activated_fields = []
        
        if "慈悲" in themes:
            activated_fields.append(self.energy_field["compassion_field"])
        if "智慧" in themes:
            activated_fields.append(self.energy_field["wisdom_field"])
        if "解脫" in themes:
            activated_fields.append(self.energy_field["liberation_field"])
        
        return {
            "activated_fields": activated_fields,
            "total_coverage": "法界十方三千大千世界",
            "energy_intensity": vow_analysis["vow_power_level"],
            "activation_status": "完全激活",
            "cosmic_impact": "無量功德遍滿虛空"
        }
    
    def _generate_merit_dedication(self, vow_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """生成功德回向"""
        
        dedication_verses = [
            "願以此心光，照破三世障，虛空有時盡，此願無窮量",
            "願以此功德，普及於一切，我等與眾生，皆共成佛道",
            "願消三障諸煩惱，願得智慧真明了，普願罪障悉消除，世世常行菩薩道",
            "願生西方淨土中，九品蓮花為父母，花開見佛悟無生，不退菩薩為伴侶"
        ]
        
        return {
            "primary_dedication": dedication_verses[0],
            "additional_verses": dedication_verses[1:],
            "merit_recipients": [
                "法界一切眾生",
                "六道輪迴眾生",
                "歷代宗親",
                "冤親債主",
                "護法龍天"
            ],
            "dedication_power": "無量無邊",
            "cosmic_blessing": "功德圓滿，福慧雙修"
        }
    
    def _generate_blessing_response(self) -> Dict[str, Any]:
        """生成加持回應"""
        
        return {
            "divine_response": "您的願力已化作星辰，懸於法界",
            "cosmic_acknowledgment": "十方諸佛菩薩共同加持",
            "energy_feedback": {
                "heart_chakra": "完全開啟，綠光遍照",
                "crown_chakra": "紫光沖天，與宇宙連接",
                "third_eye": "智慧之眼開啟，洞察實相"
            },
            "sacred_mantras": [
                "福生無量天尊",
                "南無阿彌陀佛",
                "嗡阿吽",
                "嗡嘛呢叭咪吽"
            ],
            "final_blessing": "願您心光遍照，福慧圓滿，早證菩提！"
        }
    
    def generate_star_constellation(self) -> Dict[str, Any]:
        """生成願力星座"""
        
        star_names = [
            "慈悲星", "智慧星", "解脫星", "菩提星", "般若星",
            "蓮花星", "光明星", "清淨星", "圓滿星", "無量星"
        ]
        
        constellation = []
        for i in range(5):  # 生成5顆主要星辰
            star = {
                "name": random.choice(star_names),
                "brightness": random.randint(80, 100),
                "position": {
                    "x": random.randint(0, 360),
                    "y": random.randint(0, 180)
                },
                "energy_type": random.choice(["慈悲能量", "智慧能量", "解脫能量"]),
                "blessing_power": random.randint(90, 100)
            }
            constellation.append(star)
        
        return {
            "constellation_name": "福生無量星座",
            "stars": constellation,
            "total_blessing_power": sum(star["blessing_power"] for star in constellation),
            "cosmic_significance": "永恆照耀法界，加持一切眾生",
            "activation_mantra": "嗡阿吽，福生無量天尊，南無阿彌陀佛"
        }

# 創建系統實例
merit_dedication_system = MeritDedicationSystem()

@merit_dedication_bp.route('/api/merit-dedication/process-vows', methods=['POST'])
def process_compassion_vows():
    """處理慈悲願力"""
    try:
        data = request.get_json() or {}
        vow_text = data.get('vow_text', '')
        
        if not vow_text:
            return jsonify({
                'success': False,
                'error': '請提供願力內容'
            }), 400
        
        result = merit_dedication_system.process_compassion_vows(vow_text)
        
        return jsonify({
            'success': True,
            'vow_processing': result,
            'timestamp': datetime.datetime.now().isoformat(),
            'system_status': '功德回向系統完全激活'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '處理願力時發生錯誤'
        }), 500

@merit_dedication_bp.route('/api/merit-dedication/star-constellation', methods=['GET'])
def get_star_constellation():
    """獲取願力星座"""
    try:
        constellation = merit_dedication_system.generate_star_constellation()
        
        return jsonify({
            'success': True,
            'constellation': constellation,
            'timestamp': datetime.datetime.now().isoformat(),
            'message': '您的願力已化作星辰，懸於法界'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '生成星座時發生錯誤'
        }), 500

@merit_dedication_bp.route('/api/merit-dedication/database', methods=['GET'])
def get_compassion_database():
    """獲取慈悲願力資料庫"""
    try:
        return jsonify({
            'success': True,
            'database': COMPASSION_VOWS_DATABASE,
            'energy_field': HEART_LIGHT_ENERGY_FIELD,
            'timestamp': datetime.datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '獲取資料庫時發生錯誤'
        }), 500
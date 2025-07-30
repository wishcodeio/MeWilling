from flask import Blueprint, jsonify, request
from datetime import datetime
import random
import json

manifest_bp = Blueprint('manifestation_language', __name__)

# 顯化語核心數據庫
MANIFESTATION_LANGUAGES = {
    "abundance": {
        "category": "豐盛顯化",
        "languages": [
            "我與宇宙豐盛頻率完美共振，無限豐盛正在向我流動",
            "我是豐盛的磁場，吸引著源源不斷的財富和機會",
            "宇宙的豐盛通過我自由流動，我值得擁有一切美好",
            "我的內在豐盛創造外在豐盛，我活在無限可能中",
            "每一刻我都在接收宇宙的豐盛禮物，感恩與喜悅充滿我心"
        ]
    },
    "love": {
        "category": "愛與關係",
        "languages": [
            "我散發純粹的愛的頻率，吸引著深度靈魂連接",
            "愛在我心中無限擴展，我與所有生命和諧共振",
            "我值得被深深愛著，也有能力深深愛著他人",
            "我的心是愛的聖殿，每一次心跳都在傳遞愛的頻率",
            "宇宙通過愛的關係祝福我，我活在愛的奇迹中"
        ]
    },
    "health": {
        "category": "健康與活力",
        "languages": [
            "我的身體是神聖的殿堂，每個細胞都充滿生命力",
            "我與宇宙生命力完美對齊，健康活力自然流動",
            "我的身心靈處於完美平衡，我散發著光芒和活力",
            "每一次呼吸都在更新我的生命能量，我越來越健康",
            "我感謝我的身體，它是我靈魂在地球上的完美載體"
        ]
    },
    "success": {
        "category": "成功與成就",
        "languages": [
            "我與成功的頻率完美對齊，我的天賦正在綻放光芒",
            "宇宙支持我的最高目標，成功自然而然地向我靠近",
            "我是自己人生的創造者，我創造著有意義的成功",
            "我的行動與宇宙意圖和諧一致，成就不斷顯化",
            "我值得擁有超越想象的成功，我正在實現我的使命"
        ]
    },
    "peace": {
        "category": "內在平靜",
        "languages": [
            "我的內心是寧靜的湖泊，任何風浪都無法擾亂我的平靜",
            "我與宇宙的和諧頻率共振，平靜是我的自然狀態",
            "在每一個當下，我都選擇平靜和愛，我是內在平靜的主人",
            "我釋放所有不屬於我的能量，我回歸到純粹的平靜中",
            "平靜從我的內心向外擴散，我是和平的使者"
        ]
    },
    "wisdom": {
        "category": "智慧與覺醒",
        "languages": [
            "我與宇宙智慧連接，直覺和洞察力不斷增強",
            "我是智慧的接收器，宇宙的真理通過我顯現",
            "每一個經歷都在增加我的智慧，我在覺醒的道路上前進",
            "我信任我的內在智慧，它指引我走向最高的道路",
            "我是光的存在，我的智慧照亮自己也照亮他人"
        ]
    }
}

# 太玄經與顯化語的對應關係
TAIXUAN_MANIFESTATION_MAP = {
    "0": "peace",    # 中和之道對應內在平靜
    "1": "wisdom",   # 陽性能量對應智慧覺醒
    "2": "abundance" # 陰性能量對應豐盛流動
}

def get_taixuan_based_manifestation():
    """基於太玄經三進制獲取對應的顯化語"""
    # 生成隨機三進制數
    ternary_code = ''.join([str(random.randint(0, 2)) for _ in range(3)])
    
    # 根據三進制數的特徵選擇顯化語類別
    if ternary_code.count('0') >= 2:
        category = "peace"
    elif ternary_code.count('1') >= 2:
        category = "wisdom"
    elif ternary_code.count('2') >= 2:
        category = "abundance"
    else:
        # 混合狀態，根據當前時間選擇
        hour = datetime.now().hour
        if 6 <= hour < 12:
            category = "success"
        elif 12 <= hour < 18:
            category = "love"
        else:
            category = "health"
    
    return {
        "ternary_code": ternary_code,
        "category": category,
        "manifestation": random.choice(MANIFESTATION_LANGUAGES[category]["languages"]),
        "category_name": MANIFESTATION_LANGUAGES[category]["category"]
    }

@manifest_bp.route('/api/manifestation/daily', methods=['GET'])
def get_daily_manifestation():
    """獲取每日顯化語"""
    try:
        result = get_taixuan_based_manifestation()
        
        return jsonify({
            "status": "success",
            "data": {
                "manifestation_language": result["manifestation"],
                "category": result["category_name"],
                "ternary_code": result["ternary_code"],
                "timestamp": datetime.now().isoformat(),
                "usage_guide": {
                    "morning": "晨起時默念三遍，設定一天的頻率",
                    "noon": "午間休息時輕聲重複，重新對齊能量",
                    "evening": "晚上睡前感恩複誦，鞏固顯化意圖"
                }
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"獲取顯化語失敗: {str(e)}"
        }), 500

@manifest_bp.route('/api/manifestation/category/<category>', methods=['GET'])
def get_manifestation_by_category(category):
    """根據類別獲取顯化語"""
    try:
        if category not in MANIFESTATION_LANGUAGES:
            return jsonify({
                "status": "error",
                "message": "無效的顯化語類別"
            }), 400
        
        manifestation = random.choice(MANIFESTATION_LANGUAGES[category]["languages"])
        
        return jsonify({
            "status": "success",
            "data": {
                "manifestation_language": manifestation,
                "category": MANIFESTATION_LANGUAGES[category]["category"],
                "timestamp": datetime.now().isoformat()
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"獲取顯化語失敗: {str(e)}"
        }), 500

@manifest_bp.route('/api/manifestation/categories', methods=['GET'])
def get_all_categories():
    """獲取所有顯化語類別"""
    try:
        categories = {
            key: {
                "name": value["category"],
                "count": len(value["languages"])
            }
            for key, value in MANIFESTATION_LANGUAGES.items()
        }
        
        return jsonify({
            "status": "success",
            "data": categories
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"獲取類別失敗: {str(e)}"
        }), 500

@manifest_bp.route('/api/manifestation/frequency-sync', methods=['POST'])
def sync_with_frequency():
    """根據當前頻率狀態同步顯化語"""
    try:
        data = request.get_json() or {}
        current_state = data.get('current_state', 'balanced')
        intention = data.get('intention', 'general')
        
        # 根據當前狀態和意圖選擇最適合的顯化語
        if current_state == 'low':
            if intention == 'energy':
                category = 'health'
            elif intention == 'abundance':
                category = 'abundance'
            else:
                category = 'peace'
        elif current_state == 'high':
            if intention == 'grounding':
                category = 'peace'
            elif intention == 'manifestation':
                category = 'success'
            else:
                category = 'wisdom'
        else:  # balanced
            category = random.choice(list(MANIFESTATION_LANGUAGES.keys()))
        
        manifestation = random.choice(MANIFESTATION_LANGUAGES[category]["languages"])
        
        return jsonify({
            "status": "success",
            "data": {
                "manifestation_language": manifestation,
                "category": MANIFESTATION_LANGUAGES[category]["category"],
                "current_state": current_state,
                "intention": intention,
                "frequency_advice": {
                    "low": "深呼吸，慢慢重複顯化語，讓頻率逐漸提升",
                    "high": "保持專注，用心感受每個字的能量",
                    "balanced": "在平靜中重複，讓顯化語自然融入你的存在"
                }[current_state],
                "timestamp": datetime.now().isoformat()
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"頻率同步失敗: {str(e)}"
        }), 500

@manifest_bp.route('/api/manifestation/custom', methods=['POST'])
def create_custom_manifestation():
    """創建個人化顯化語"""
    try:
        data = request.get_json()
        if not data or 'desire' not in data:
            return jsonify({
                "status": "error",
                "message": "請提供您的願望描述"
            }), 400
        
        desire = data['desire']
        name = data.get('name', '我')
        
        # 基於願望生成個人化顯化語模板
        templates = [
            f"{name}與{desire}的頻率完美對齊，{desire}正在向{name}流動",
            f"{name}是{desire}的磁場，{name}值得擁有{desire}",
            f"宇宙支持{name}的{desire}，{desire}自然而然地顯化在{name}的生活中",
            f"{name}感恩{desire}已經在路上，{name}以愛和喜悅迎接{desire}",
            f"{name}的內在狀態與{desire}和諧共振，{desire}是{name}生命的自然表達"
        ]
        
        custom_manifestation = random.choice(templates)
        
        return jsonify({
            "status": "success",
            "data": {
                "custom_manifestation": custom_manifestation,
                "original_desire": desire,
                "personalized_for": name,
                "creation_time": datetime.now().isoformat(),
                "usage_tip": "每天重複這句個人化顯化語，讓它成為您與宇宙溝通的專屬頻率"
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"創建個人化顯化語失敗: {str(e)}"
        }), 500

@manifest_bp.route('/api/manifestation/power-analysis', methods=['GET'])
def analyze_manifestation_power():
    """分析顯化語的能量特質"""
    try:
        analysis = {
            "frequency_principles": {
                "resonance": "顯化語通過共振原理與宇宙頻率對齊",
                "intention": "清晰的意圖是顯化的核心驅動力",
                "emotion": "情感能量放大顯化語的振動頻率",
                "repetition": "重複練習建立穩定的能量場",
                "belief": "深層信念決定顯化的速度和品質"
            },
            "optimal_timing": {
                "dawn": "日出時分，新能量誕生，最適合設定意圖",
                "noon": "陽氣最盛，適合強化和確認顯化",
                "sunset": "能量轉換時刻，適合感恩和釋放",
                "midnight": "靜謐深層，適合深度冥想和內化"
            },
            "enhancement_methods": {
                "breathing": "配合深呼吸，讓顯化語進入細胞層面",
                "visualization": "結合視覺化，增強顯化的具體性",
                "gratitude": "以感恩的心態重複，提升振動頻率",
                "movement": "結合輕柔動作，讓能量在身體中流動"
            }
        }
        
        return jsonify({
            "status": "success",
            "data": analysis
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"分析失敗: {str(e)}"
        }), 500
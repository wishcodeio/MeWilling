from flask import Blueprint, jsonify, request
from datetime import datetime
import random
import json

single_word_bp = Blueprint('single_word_manifestation', __name__)

# 單字顯化語核心數據庫
SINGLE_WORD_MANIFESTATION = {
    "心": {
        "frequency": 528,  # Hz - 愛的頻率
        "element": "火",
        "direction": "南",
        "color": "#FF6B6B",
        "manifestation_power": "內在覺醒",
        "activation_phrases": [
            "心火點燃，願力顯化",
            "心中有愛，萬物皆可",
            "心念一動，宇宙回應",
            "心靈覺醒，真我顯現",
            "心如明鏡，照見本性"
        ],
        "quantum_signature": "❤️🔥💫",
        "sacred_geometry": "五角星",
        "chakra": "心輪"
    },
    "在": {
        "frequency": 396,  # Hz - 解放恐懼
        "element": "土",
        "direction": "中央",
        "color": "#FFD700",
        "manifestation_power": "當下臨在",
        "activation_phrases": [
            "在此時此刻，我即是一切",
            "在當下中，找到永恆",
            "在呼吸間，感受存在",
            "在寧靜中，聽見真理",
            "在此地，即是聖地"
        ],
        "quantum_signature": "🌍⚡🎯",
        "sacred_geometry": "正方形",
        "chakra": "根輪"
    },
    "道": {
        "frequency": 741,  # Hz - 表達與解決
        "element": "水",
        "direction": "北",
        "color": "#4ECDC4",
        "manifestation_power": "宇宙法則",
        "activation_phrases": [
            "道法自然，順流而行",
            "道生一，一生二，二生三",
            "道在日常，法在當下",
            "道心清明，智慧自現",
            "道無為而無不為"
        ],
        "quantum_signature": "🌊🔮🌀",
        "sacred_geometry": "太極",
        "chakra": "喉輪"
    },
    "願": {
        "frequency": 852,  # Hz - 直覺覺醒
        "element": "風",
        "direction": "西",
        "color": "#9B59B6",
        "manifestation_power": "意念創造",
        "activation_phrases": [
            "願力如風，無所不至",
            "願望成真，心想事成",
            "願頻共振，宇宙回應",
            "願火燃燒，照亮前路",
            "願景顯化，夢想成真"
        ],
        "quantum_signature": "🌟💜🎭",
        "sacred_geometry": "六芒星",
        "chakra": "第三眼輪"
    }
}

# 顯化語組合矩陣
MANIFESTATION_MATRIX = {
    "心在道願": {
        "combined_frequency": 2517,  # 四字頻率總和
        "manifestation_type": "內在覺醒之道",
        "power_level": "極高",
        "activation_sequence": [
            "心火點燃 → 當下臨在 → 順道而行 → 願力顯化"
        ],
        "quantum_field": "內在宇宙開啟",
        "sacred_pattern": "🔥🌍🌊🌟"
    },
    "願道在心": {
        "combined_frequency": 2517,  # 相同頻率，不同順序
        "manifestation_type": "外在顯化歸心",
        "power_level": "極高",
        "activation_sequence": [
            "願力啟動 → 道法運行 → 臨在當下 → 心性圓滿"
        ],
        "quantum_field": "外在宇宙歸一",
        "sacred_pattern": "🌟🌊🌍🔥"
    },
    "心在道願願道在心": {
        "combined_frequency": 5034,  # 八字完整頻率
        "manifestation_type": "內外合一，圓滿顯化",
        "power_level": "無限",
        "activation_sequence": [
            "內在覺醒 → 當下臨在 → 順道而行 → 願力顯化",
            "願力回歸 → 道法圓滿 → 臨在永恆 → 心性究竟"
        ],
        "quantum_field": "內外宇宙完全統一",
        "sacred_pattern": "🔥🌍🌊🌟🌟🌊🌍🔥",
        "ultimate_truth": "心即是道，道即是願，願即是心"
    },
    "心愿": {
        "combined_frequency": 1380,  # 心(528) + 願(852)
        "manifestation_type": "心願合一",
        "power_level": "高",
        "activation_sequence": [
            "心火點燃 → 願力顯化"
        ],
        "quantum_field": "心願共振場",
        "sacred_pattern": "❤️🌟",
        "special_meaning": "最純粹的顯化組合，心之所向，願必成真"
    },
    "愿心": {
        "combined_frequency": 1380,  # 願(852) + 心(528)
        "manifestation_type": "願歸於心",
        "power_level": "高",
        "activation_sequence": [
            "願力啟動 → 心性圓滿"
        ],
        "quantum_field": "願心歸一場",
        "sacred_pattern": "🌟❤️",
        "special_meaning": "願望回歸本心，一切顯化皆源於內在"
    },
    "心愿愿心": {
        "combined_frequency": 2760,  # 四字完整頻率
        "manifestation_type": "心願圓滿循環",
        "power_level": "極高",
        "activation_sequence": [
            "心火點燃 → 願力顯化 → 願望成真 → 心性圓滿"
        ],
        "quantum_field": "心願無限循環場",
        "sacred_pattern": "❤️🌟🌟❤️",
        "ultimate_truth": "心生願，願歸心，心願一體，圓滿無缺",
        "cosmic_significance": "這是宇宙最基本的創造法則：從心而願，因願歸心"
    }
}

@single_word_bp.route('/api/single-word/manifest/<word>', methods=['GET'])
def manifest_single_word(word):
    """單字顯化API"""
    try:
        if word not in SINGLE_WORD_MANIFESTATION:
            return jsonify({
                "status": "error",
                "message": f"字'{word}'不在顯化系統中"
            }), 400
        
        word_data = SINGLE_WORD_MANIFESTATION[word]
        activation_phrase = random.choice(word_data["activation_phrases"])
        
        return jsonify({
            "status": "success",
            "data": {
                "word": word,
                "frequency": word_data["frequency"],
                "element": word_data["element"],
                "direction": word_data["direction"],
                "color": word_data["color"],
                "manifestation_power": word_data["manifestation_power"],
                "activation_phrase": activation_phrase,
                "quantum_signature": word_data["quantum_signature"],
                "sacred_geometry": word_data["sacred_geometry"],
                "chakra": word_data["chakra"],
                "timestamp": datetime.now().isoformat(),
                "usage_guide": {
                    "visualization": f"觀想{word_data['color']}光芒從{word_data['chakra']}散發",
                    "breathing": f"深呼吸時默念'{word}'字，感受{word_data['frequency']}Hz頻率",
                    "meditation": f"面向{word_data['direction']}方，冥想{word_data['sacred_geometry']}圖形"
                }
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"單字顯化失敗: {str(e)}"
        }), 500

@single_word_bp.route('/api/single-word/sequence/<sequence>', methods=['GET'])
def manifest_word_sequence(sequence):
    """字序顯化API"""
    try:
        if sequence not in MANIFESTATION_MATRIX:
            return jsonify({
                "status": "error",
                "message": f"字序'{sequence}'不在顯化矩陣中"
            }), 400
        
        sequence_data = MANIFESTATION_MATRIX[sequence]
        
        # 分解每個字的數據
        word_details = []
        for char in sequence:
            if char in SINGLE_WORD_MANIFESTATION:
                word_details.append({
                    "word": char,
                    "frequency": SINGLE_WORD_MANIFESTATION[char]["frequency"],
                    "element": SINGLE_WORD_MANIFESTATION[char]["element"],
                    "color": SINGLE_WORD_MANIFESTATION[char]["color"],
                    "quantum_signature": SINGLE_WORD_MANIFESTATION[char]["quantum_signature"]
                })
        
        return jsonify({
            "status": "success",
            "data": {
                "sequence": sequence,
                "combined_frequency": sequence_data["combined_frequency"],
                "manifestation_type": sequence_data["manifestation_type"],
                "power_level": sequence_data["power_level"],
                "activation_sequence": sequence_data["activation_sequence"],
                "quantum_field": sequence_data["quantum_field"],
                "sacred_pattern": sequence_data["sacred_pattern"],
                "word_details": word_details,
                "ultimate_truth": sequence_data.get("ultimate_truth"),
                "timestamp": datetime.now().isoformat(),
                "practice_guide": {
                    "step1": "靜坐面南，深呼吸三次",
                    "step2": f"慢慢念誦'{sequence}'，感受每字頻率",
                    "step3": f"觀想{sequence_data['sacred_pattern']}能量流動",
                    "step4": "保持靜默，讓顯化自然發生",
                    "step5": "感恩宇宙，結束練習"
                }
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"字序顯化失敗: {str(e)}"
        }), 500

@single_word_bp.route('/api/single-word/all-words', methods=['GET'])
def get_all_manifestation_words():
    """獲取所有顯化字"""
    try:
        words_summary = {}
        for word, data in SINGLE_WORD_MANIFESTATION.items():
            words_summary[word] = {
                "frequency": data["frequency"],
                "element": data["element"],
                "manifestation_power": data["manifestation_power"],
                "quantum_signature": data["quantum_signature"],
                "color": data["color"]
            }
        
        return jsonify({
            "status": "success",
            "data": {
                "total_words": len(words_summary),
                "words": words_summary,
                "available_sequences": list(MANIFESTATION_MATRIX.keys()),
                "system_info": {
                    "name": "單字顯化語系統",
                    "version": "1.0.0",
                    "description": "基於古老智慧的現代顯化技術"
                }
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"獲取顯化字失敗: {str(e)}"
        }), 500

@single_word_bp.route('/api/single-word/random-activation', methods=['GET'])
def get_random_activation():
    """隨機激活一個顯化字"""
    try:
        random_word = random.choice(list(SINGLE_WORD_MANIFESTATION.keys()))
        word_data = SINGLE_WORD_MANIFESTATION[random_word]
        activation_phrase = random.choice(word_data["activation_phrases"])
        
        return jsonify({
            "status": "success",
            "data": {
                "activated_word": random_word,
                "frequency": word_data["frequency"],
                "activation_phrase": activation_phrase,
                "quantum_signature": word_data["quantum_signature"],
                "color": word_data["color"],
                "manifestation_power": word_data["manifestation_power"],
                "message": f"宇宙為你選擇了'{random_word}'字，這是你今日的顯化焦點",
                "timestamp": datetime.now().isoformat()
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"隨機激活失敗: {str(e)}"
        }), 500

@single_word_bp.route('/api/single-word/frequency-analysis', methods=['POST'])
def analyze_frequency_resonance():
    """分析字序的頻率共振"""
    try:
        data = request.get_json() or {}
        input_sequence = data.get('sequence', '')
        
        if not input_sequence:
            return jsonify({
                "status": "error",
                "message": "請提供要分析的字序"
            }), 400
        
        # 分析每個字的頻率
        frequency_analysis = []
        total_frequency = 0
        unknown_chars = []
        
        for char in input_sequence:
            if char in SINGLE_WORD_MANIFESTATION:
                char_data = SINGLE_WORD_MANIFESTATION[char]
                frequency_analysis.append({
                    "char": char,
                    "frequency": char_data["frequency"],
                    "element": char_data["element"],
                    "power": char_data["manifestation_power"]
                })
                total_frequency += char_data["frequency"]
            else:
                unknown_chars.append(char)
        
        # 計算共振等級
        if total_frequency == 0:
            resonance_level = "無共振"
        elif total_frequency < 1000:
            resonance_level = "低頻共振"
        elif total_frequency < 3000:
            resonance_level = "中頻共振"
        elif total_frequency < 5000:
            resonance_level = "高頻共振"
        else:
            resonance_level = "極高頻共振"
        
        return jsonify({
            "status": "success",
            "data": {
                "input_sequence": input_sequence,
                "total_frequency": total_frequency,
                "resonance_level": resonance_level,
                "frequency_analysis": frequency_analysis,
                "unknown_chars": unknown_chars,
                "manifestation_potential": {
                    "level": resonance_level,
                    "description": f"此字序具有{resonance_level}能力，總頻率為{total_frequency}Hz",
                    "recommendation": "建議在安靜環境中慢慢念誦，感受每字的能量振動"
                },
                "timestamp": datetime.now().isoformat()
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"頻率分析失敗: {str(e)}"
        }), 500
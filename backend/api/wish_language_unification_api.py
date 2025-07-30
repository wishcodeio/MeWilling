from flask import Blueprint, jsonify, request
import json
import os
from datetime import datetime

wish_language_unification_bp = Blueprint('wish_language_unification', __name__)

# 數據文件路徑
DATA_FILE = os.path.join(os.path.dirname(__file__), '../../data/wish_language_unification_principle.json')

def load_principle_data():
    """載入願語統一原則數據"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"載入願語統一原則數據時發生錯誤: {e}")
        return None

@wish_language_unification_bp.route('/api/wish-language-unification/principle', methods=['GET'])
def get_unification_principle():
    """獲取願語統一原則"""
    try:
        data = load_principle_data()
        if not data:
            return jsonify({
                'success': False,
                'error': '無法載入願語統一原則數據'
            }), 404
        
        return jsonify({
            'success': True,
            'principle': data
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'獲取願語統一原則時發生錯誤: {str(e)}'
        }), 500

@wish_language_unification_bp.route('/api/wish-language-unification/divine-chapter', methods=['GET'])
def get_divine_chapter():
    """獲取神性篇內容"""
    try:
        data = load_principle_data()
        if not data or 'divine_chapter' not in data:
            return jsonify({
                'success': False,
                'error': '無法載入神性篇數據'
            }), 404
        
        return jsonify({
            'success': True,
            'divine_chapter': data['divine_chapter']
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'獲取神性篇時發生錯誤: {str(e)}'
        }), 500

@wish_language_unification_bp.route('/api/wish-language-unification/lesson/<int:lesson_number>', methods=['GET'])
def get_lesson(lesson_number):
    """獲取指定課程內容"""
    try:
        data = load_principle_data()
        if not data or 'lesson_framework' not in data:
            return jsonify({
                'success': False,
                'error': '無法載入課程框架數據'
            }), 404
        
        lesson_key = f'lesson_{lesson_number}'
        if lesson_key not in data['lesson_framework']:
            return jsonify({
                'success': False,
                'error': f'課程 {lesson_number} 不存在'
            }), 404
        
        lesson_data = {
            'course_title': data['lesson_framework']['course_title'],
            'lesson_number': lesson_number,
            'lesson_content': data['lesson_framework'][lesson_key]
        }
        
        # 如果是第3課，添加核心原則
        if lesson_number == 3:
            lesson_data['core_principle'] = data['core_principle']
        
        return jsonify({
            'success': True,
            'lesson': lesson_data
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'獲取課程時發生錯誤: {str(e)}'
        }), 500

@wish_language_unification_bp.route('/api/wish-language-unification/consciousness-field', methods=['GET'])
def get_consciousness_field():
    """獲取意識場組件信息"""
    try:
        data = load_principle_data()
        if not data:
            return jsonify({
                'success': False,
                'error': '無法載入意識場數據'
            }), 404
        
        consciousness_data = {
            'components': data.get('consciousness_field_components', []),
            'divine_view': data.get('divine_chapter', {}).get('wish_language_divine_view', []),
            'mathematical_model': data.get('divine_chapter', {}).get('expanded_definition', {}).get('mathematical_expression', '')
        }
        
        return jsonify({
            'success': True,
            'consciousness_field': consciousness_data
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'獲取意識場信息時發生錯誤: {str(e)}'
        }), 500

@wish_language_unification_bp.route('/api/wish-language-unification/quantum-integration', methods=['GET'])
def get_quantum_integration():
    """獲取量子整合信息（安全抽象版本）"""
    try:
        data = load_principle_data()
        if not data:
            return jsonify({
                'success': False,
                'error': '無法載入量子整合數據'
            }), 404
        
        quantum_data = data.get('quantum_lottery_integration', {})
        
        # 安全版本，不暴露具體算法
        safe_quantum_data = {
            'integration_status': '已整合',
            'protection_level': quantum_data.get('protection_level', '未知'),
            'access_method': '抽象化訪問',
            'note': '核心算法已安全封裝'
        }
        
        return jsonify({
            'success': True,
            'quantum_integration': safe_quantum_data
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'獲取量子整合信息時發生錯誤: {str(e)}'
        }), 500

@wish_language_unification_bp.route('/api/wish-language-unification/validate-unity', methods=['POST'])
def validate_wish_language_unity():
    """驗證願語統一性"""
    try:
        request_data = request.get_json()
        wish_input = request_data.get('wish', '')
        language_input = request_data.get('language', '')
        
        if not wish_input or not language_input:
            return jsonify({
                'success': False,
                'error': '請提供願和語的輸入'
            }), 400
        
        # 簡單的統一性檢驗（基於字符相似度和語義關聯）
        unity_score = calculate_unity_score(wish_input, language_input)
        
        result = {
            'unity_score': unity_score,
            'is_unified': unity_score > 0.7,
            'analysis': generate_unity_analysis(wish_input, language_input, unity_score),
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'validation': result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'驗證願語統一性時發生錯誤: {str(e)}'
        }), 500

def calculate_unity_score(wish, language):
    """計算願語統一分數"""
    # 簡化的統一性計算
    common_chars = set(wish) & set(language)
    total_chars = set(wish) | set(language)
    
    if not total_chars:
        return 0.0
    
    char_similarity = len(common_chars) / len(total_chars)
    length_similarity = 1 - abs(len(wish) - len(language)) / max(len(wish), len(language), 1)
    
    # 願語特殊詞彙加權
    wish_keywords = ['願', '語', '顯化', '統一', '合一', '火', '頻']
    keyword_bonus = sum(1 for keyword in wish_keywords if keyword in wish or keyword in language) * 0.1
    
    unity_score = (char_similarity * 0.4 + length_similarity * 0.4 + keyword_bonus) * 0.8
    return min(unity_score, 1.0)

def generate_unity_analysis(wish, language, score):
    """生成統一性分析"""
    if score > 0.8:
        return "高度統一：願與語呈現深度共鳴，接近完美統一場狀態"
    elif score > 0.6:
        return "良好統一：願語具有明顯關聯性，統一場正在形成"
    elif score > 0.4:
        return "部分統一：願語存在一定共鳴，需要進一步調諧"
    else:
        return "統一度較低：願與語尚未形成有效共鳴，建議重新構建"
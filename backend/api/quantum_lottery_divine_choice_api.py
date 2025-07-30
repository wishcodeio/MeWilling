from flask import Blueprint, jsonify, request
import json
import os
import random
import math
from datetime import datetime, timedelta
import numpy as np
from collections import Counter

quantum_lottery_divine_choice_bp = Blueprint('quantum_lottery_divine_choice', __name__)

# 載入理論數據
def load_theory_data():
    """載入量子彩票與神性選擇理論數據"""
    try:
        theory_file = os.path.join(os.path.dirname(__file__), '../../data/quantum_lottery_divine_choice_theory.json')
        with open(theory_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return {"error": f"無法載入理論數據: {str(e)}"}

@quantum_lottery_divine_choice_bp.route('/api/quantum-lottery-divine-choice/theory', methods=['GET'])
def get_theory():
    """獲取量子彩票與神性選擇理論"""
    try:
        theory_data = load_theory_data()
        return jsonify({
            "success": True,
            "data": theory_data
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@quantum_lottery_divine_choice_bp.route('/api/quantum-lottery-divine-choice/divine-choice-detector', methods=['POST'])
def detect_divine_choice():
    """檢測彩票結果中的神性選擇痕跡"""
    try:
        data = request.get_json()
        lottery_numbers = data.get('numbers', [])
        
        if not lottery_numbers or len(lottery_numbers) < 6:
            return jsonify({
                "success": False,
                "error": "請提供至少6個彩票號碼"
            }), 400
        
        # 計算神性干預指標
        analysis = analyze_divine_intervention(lottery_numbers)
        
        return jsonify({
            "success": True,
            "data": {
                "numbers": lottery_numbers,
                "divine_intervention_score": analysis['score'],
                "analysis": analysis,
                "interpretation": get_divine_interpretation(analysis['score'])
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

def analyze_divine_intervention(numbers):
    """分析數字中的神性干預痕跡"""
    analysis = {
        "pattern_complexity": calculate_pattern_complexity(numbers),
        "sacred_geometry_score": calculate_sacred_geometry_score(numbers),
        "synchronicity_strength": calculate_synchronicity_strength(numbers),
        "archetypal_significance": calculate_archetypal_significance(numbers),
        "fibonacci_resonance": calculate_fibonacci_resonance(numbers),
        "golden_ratio_alignment": calculate_golden_ratio_alignment(numbers)
    }
    
    # 計算總體神性干預評分
    weights = {
        "pattern_complexity": 0.2,
        "sacred_geometry_score": 0.15,
        "synchronicity_strength": 0.25,
        "archetypal_significance": 0.15,
        "fibonacci_resonance": 0.15,
        "golden_ratio_alignment": 0.1
    }
    
    total_score = sum(analysis[key] * weights[key] for key in weights)
    analysis['score'] = min(total_score, 1.0)
    
    return analysis

def calculate_pattern_complexity(numbers):
    """計算數字模式複雜度"""
    # 檢查數字間的關係
    differences = [abs(numbers[i+1] - numbers[i]) for i in range(len(numbers)-1)]
    
    # 計算差值的變異係數
    if len(differences) > 1:
        mean_diff = np.mean(differences)
        std_diff = np.std(differences)
        cv = std_diff / mean_diff if mean_diff > 0 else 0
        complexity = min(cv / 2, 1.0)  # 標準化到0-1
    else:
        complexity = 0.5
    
    return complexity

def calculate_sacred_geometry_score(numbers):
    """計算神聖幾何評分"""
    score = 0
    
    # 檢查特殊數字（質數、完全數等）
    special_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}  # 質數
    perfect_numbers = {6, 28}  # 完全數
    
    for num in numbers:
        if num in special_numbers:
            score += 0.1
        if num in perfect_numbers:
            score += 0.2
        
        # 檢查數字根（數字學）
        digital_root = get_digital_root(num)
        if digital_root in {1, 3, 7, 9}:  # 神聖數字根
            score += 0.05
    
    return min(score, 1.0)

def calculate_synchronicity_strength(numbers):
    """計算同步性強度"""
    # 基於當前時間和數字的關聯
    now = datetime.now()
    
    score = 0
    
    # 檢查與日期的關聯
    date_numbers = [now.day, now.month, now.year % 100]
    for num in numbers:
        if num in date_numbers:
            score += 0.2
    
    # 檢查數字和（生命數字學）
    total_sum = sum(numbers)
    life_path_number = get_digital_root(total_sum)
    
    # 特殊生命路徑數字
    if life_path_number in {11, 22, 33}:  # 大師數字
        score += 0.3
    elif life_path_number in {1, 7, 9}:  # 靈性數字
        score += 0.2
    
    return min(score, 1.0)

def calculate_archetypal_significance(numbers):
    """計算原型意義"""
    # 榮格原型數字
    archetypal_numbers = {
        1: "自我",
        2: "陰影",
        3: "三位一體",
        4: "穩定",
        7: "完整",
        8: "無限",
        9: "完成",
        12: "完美",
        13: "轉化",
        21: "世界",
        22: "愚者的旅程"
    }
    
    score = 0
    for num in numbers:
        if num in archetypal_numbers:
            score += 0.15
    
    return min(score, 1.0)

def calculate_fibonacci_resonance(numbers):
    """計算斐波那契共鳴"""
    # 斐波那契數列前20項
    fib_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    
    score = 0
    for num in numbers:
        if num in fib_sequence:
            score += 0.2
        
        # 檢查是否接近斐波那契數
        for fib_num in fib_sequence:
            if abs(num - fib_num) <= 2 and num != fib_num:
                score += 0.1
                break
    
    return min(score, 1.0)

def calculate_golden_ratio_alignment(numbers):
    """計算黃金比例對齊度"""
    golden_ratio = 1.618033988749
    
    score = 0
    for i in range(len(numbers) - 1):
        if numbers[i] > 0:
            ratio = numbers[i+1] / numbers[i]
            # 檢查是否接近黃金比例或其倒數
            if abs(ratio - golden_ratio) < 0.1 or abs(ratio - 1/golden_ratio) < 0.1:
                score += 0.3
    
    return min(score, 1.0)

def get_digital_root(number):
    """計算數字根"""
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number

def get_divine_interpretation(score):
    """根據評分獲取神性解釋"""
    if score >= 0.8:
        return {
            "level": "極高神性干預",
            "description": "這組數字顯示出極強的神性選擇痕跡，可能承載著重要的宇宙信息。",
            "recommendation": "深入冥想這組數字的意義，它們可能是來自更高維度的指引。"
        }
    elif score >= 0.6:
        return {
            "level": "顯著神性干預",
            "description": "這組數字包含明顯的非隨機模式，暗示著某種神性意圖。",
            "recommendation": "關注這組數字出現的時機和背景，可能與你的生命課題相關。"
        }
    elif score >= 0.4:
        return {
            "level": "中等神性干預",
            "description": "這組數字顯示出一定的模式性，可能包含微妙的神性信息。",
            "recommendation": "保持開放的心態，觀察這組數字是否與你的生活產生共鳴。"
        }
    elif score >= 0.2:
        return {
            "level": "輕微神性干預",
            "description": "這組數字主要呈現隨機性，但仍有微弱的模式痕跡。",
            "recommendation": "這可能是純粹的隨機結果，但也要保持對同步性的敏感。"
        }
    else:
        return {
            "level": "純粹隨機性",
            "description": "這組數字符合純隨機分佈，沒有明顯的神性干預痕跡。",
            "recommendation": "這支持了上帝不做選擇的宇宙模型，隨機性是宇宙的本質特性。"
        }

@quantum_lottery_divine_choice_bp.route('/api/quantum-lottery-divine-choice/consciousness-lottery', methods=['POST'])
def consciousness_influenced_lottery():
    """基於意識狀態的彩票生成"""
    try:
        data = request.get_json()
        consciousness_state = data.get('consciousness_state', 'neutral')
        intention = data.get('intention', '')
        
        # 根據意識狀態生成數字
        numbers = generate_consciousness_numbers(consciousness_state, intention)
        
        return jsonify({
            "success": True,
            "data": {
                "numbers": numbers,
                "consciousness_state": consciousness_state,
                "intention": intention,
                "generation_method": "consciousness_influenced",
                "divine_resonance": calculate_consciousness_resonance(numbers, consciousness_state)
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

def generate_consciousness_numbers(consciousness_state, intention):
    """根據意識狀態生成數字"""
    # 設定隨機種子基於意識狀態
    seed_base = hash(consciousness_state + intention + str(datetime.now().microsecond))
    random.seed(seed_base % (2**32))
    
    numbers = []
    
    # 根據不同意識狀態調整生成策略
    if consciousness_state == 'meditative':
        # 冥想狀態：偏向神聖數字
        sacred_numbers = [1, 3, 7, 9, 11, 13, 21, 33]
        for _ in range(6):
            if random.random() < 0.4:  # 40%機率選擇神聖數字
                numbers.append(random.choice(sacred_numbers))
            else:
                numbers.append(random.randint(1, 49))
    
    elif consciousness_state == 'grateful':
        # 感恩狀態：偏向和諧數字
        for _ in range(6):
            num = random.randint(1, 49)
            # 調整為更和諧的數字（避免極端值）
            if num < 10 or num > 40:
                num = random.randint(10, 40)
            numbers.append(num)
    
    elif consciousness_state == 'loving':
        # 愛的狀態：偏向心形數字模式
        heart_numbers = [6, 14, 22, 28, 36, 44]  # 形似心形的數字
        for i in range(6):
            if i < 3 and random.random() < 0.5:
                numbers.append(heart_numbers[i])
            else:
                numbers.append(random.randint(1, 49))
    
    else:  # neutral 或其他狀態
        # 中性狀態：純隨機
        numbers = [random.randint(1, 49) for _ in range(6)]
    
    # 確保沒有重複並排序
    numbers = sorted(list(set(numbers)))
    
    # 如果數字不足6個，補充隨機數字
    while len(numbers) < 6:
        new_num = random.randint(1, 49)
        if new_num not in numbers:
            numbers.append(new_num)
    
    return sorted(numbers[:6])

def calculate_consciousness_resonance(numbers, consciousness_state):
    """計算意識共鳴度"""
    base_resonance = 0.5
    
    # 根據意識狀態調整共鳴度
    state_multipliers = {
        'meditative': 1.2,
        'grateful': 1.1,
        'loving': 1.15,
        'neutral': 1.0,
        'anxious': 0.8,
        'angry': 0.7
    }
    
    multiplier = state_multipliers.get(consciousness_state, 1.0)
    
    # 基於數字特性調整
    harmony_score = calculate_number_harmony(numbers)
    
    resonance = base_resonance * multiplier * (1 + harmony_score)
    
    return min(resonance, 1.0)

def calculate_number_harmony(numbers):
    """計算數字和諧度"""
    if len(numbers) < 2:
        return 0
    
    # 計算數字間距的標準差
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    std_dev = np.std(differences)
    
    # 標準差越小，和諧度越高
    harmony = 1 / (1 + std_dev / 10)
    
    return harmony

@quantum_lottery_divine_choice_bp.route('/api/quantum-lottery-divine-choice/philosophical-analysis', methods=['GET'])
def get_philosophical_analysis():
    """獲取哲學分析"""
    try:
        theory_data = load_theory_data()
        
        analysis = {
            "core_question": "上帝創造宇宙時是否做選擇？",
            "paradigms": {
                "deterministic_god": theory_data.get('theoretical_framework', {}).get('divine_choice_paradigm', {}).get('deterministic_god', {}),
                "non_choosing_god": theory_data.get('theoretical_framework', {}).get('divine_choice_paradigm', {}).get('non_choosing_god', {})
            },
            "implications": theory_data.get('philosophical_implications', {}),
            "experimental_approach": theory_data.get('experimental_design', {})
        }
        
        return jsonify({
            "success": True,
            "data": analysis
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
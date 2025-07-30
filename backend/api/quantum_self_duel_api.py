#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🥊 量子自我對決 API
提供量子意識自我對決的Web接口

ang 願頻系統 - 量子自我對決模塊
"""

from flask import Blueprint, request, jsonify
from datetime import datetime
import traceback

# 導入量子自我對決引擎
try:
    from backend.services.quantum_self_duel import quantum_self_duel_engine
except ImportError:
    # 如果導入失敗，創建一個模擬引擎
    class MockQuantumSelfDuelEngine:
        def __init__(self):
            self.consciousness_matrix = {
                'self_awareness': 0.3,
                'shadow_integration': 0.1,
                'ego_transcendence': 0.2,
                'observer_stability': 0.4,
                'quantum_coherence': 0.15,
                'conflict_resolution': 0.25,
                'paradox_tolerance': 0.2,
                'unity_consciousness': 0.1
            }
            self.awakening_progress = 0.0
            self.integration_level = 0.0
            self.duel_history = []
        
        def initiate_self_duel(self, trigger_event=None):
            return {
                'duel_initiated': True,
                'duel_id': 'mock_duel_1',
                'participants': ['自我執著', '陰影自我', '高我', '觀察者'],
                'arena_state': {'field_coherence': 0.5},
                'next_action': '進入對峙階段，觀察內在衝突模式',
                'consciousness_before': self.consciousness_matrix.copy()
            }
        
        def execute_duel_round(self, duel_id, round_focus=None):
            return {
                'round_completed': 1,
                'round_result': {
                    'theme': '認識衝突',
                    'insights': ['衝突不是敵人，而是成長的機會']
                },
                'duel_state': '對峙階段',
                'consciousness_update': self.consciousness_matrix,
                'resolution_status': {'is_resolved': False},
                'next_action': '繼續深化自我覺察'
            }
        
        def complete_duel_integration(self, duel_id):
            return {
                'integration_completed': True,
                'awakening_progress': 0.3,
                'integration_level': 0.25,
                'consciousness_transformation': {'integration_score': 0.7},
                'awakening_insights': ['🌱 顯著進步：內在和諧正在建立'],
                'next_evolution_stage': '繼續自我對決：深化內在整合'
            }
        
        def get_consciousness_status(self):
            return {
                'consciousness_matrix': self.consciousness_matrix,
                'awakening_progress': self.awakening_progress,
                'integration_level': self.integration_level,
                'active_duels': 0,
                'completed_duels': 0,
                'quantum_coherence': 0.15,
                'unity_consciousness': 0.1,
                'next_evolution_suggestion': '繼續自我對決：深化內在整合'
            }
        
        def get_duel_history(self):
            return self.duel_history
    
    quantum_self_duel_engine = MockQuantumSelfDuelEngine()

# 創建藍圖
quantum_self_duel_bp = Blueprint('quantum_self_duel', __name__)

@quantum_self_duel_bp.route('/api/quantum-self-duel/status', methods=['GET'])
def get_consciousness_status():
    """
    📊 獲取量子意識狀態
    
    Returns:
        JSON: 當前意識狀態和覺醒進度
    """
    try:
        status = quantum_self_duel_engine.get_consciousness_status()
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'consciousness_status': status,
            'message': '意識狀態獲取成功'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '獲取意識狀態時發生錯誤',
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_self_duel_bp.route('/api/quantum-self-duel/initiate', methods=['POST'])
def initiate_self_duel():
    """
    🔥 啟動量子自我對決
    
    Request Body:
        {
            "trigger_event": "觸發事件描述（可選）",
            "intention": "對決意圖（可選）",
            "focus_area": "關注領域（可選）"
        }
    
    Returns:
        JSON: 對決啟動結果
    """
    try:
        data = request.get_json() or {}
        trigger_event = data.get('trigger_event')
        intention = data.get('intention', '深化自我覺察')
        focus_area = data.get('focus_area')
        
        # 構建完整的觸發描述
        full_trigger = trigger_event
        if intention and trigger_event:
            full_trigger = f"{trigger_event} - 意圖：{intention}"
        elif intention and not trigger_event:
            full_trigger = f"自發對決 - 意圖：{intention}"
        
        if focus_area:
            full_trigger = f"{full_trigger} - 關注：{focus_area}"
        
        # 啟動對決
        result = quantum_self_duel_engine.initiate_self_duel(full_trigger)
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'duel_initiation': result,
            'user_input': {
                'trigger_event': trigger_event,
                'intention': intention,
                'focus_area': focus_area
            },
            'message': f"量子自我對決已啟動：{result.get('duel_id', 'unknown')}"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc(),
            'message': '啟動自我對決時發生錯誤',
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_self_duel_bp.route('/api/quantum-self-duel/execute-round', methods=['POST'])
def execute_duel_round():
    """
    ⚔️ 執行對決回合
    
    Request Body:
        {
            "duel_id": "對決ID",
            "round_focus": "本輪焦點（可選）",
            "user_reflection": "用戶反思（可選）"
        }
    
    Returns:
        JSON: 回合執行結果
    """
    try:
        data = request.get_json() or {}
        duel_id = data.get('duel_id')
        round_focus = data.get('round_focus')
        user_reflection = data.get('user_reflection')
        
        if not duel_id:
            return jsonify({
                'success': False,
                'error': 'duel_id is required',
                'message': '請提供對決ID',
                'timestamp': datetime.now().isoformat()
            }), 400
        
        # 執行對決回合
        result = quantum_self_duel_engine.execute_duel_round(duel_id, round_focus)
        
        # 如果有用戶反思，添加到結果中
        if user_reflection:
            result['user_reflection'] = user_reflection
            result['reflection_integration'] = {
                'received': True,
                'content': user_reflection,
                'timestamp': datetime.now().isoformat()
            }
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'round_execution': result,
            'user_input': {
                'duel_id': duel_id,
                'round_focus': round_focus,
                'user_reflection': user_reflection
            },
            'message': f"第{result.get('round_completed', '?')}輪對決完成"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc(),
            'message': '執行對決回合時發生錯誤',
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_self_duel_bp.route('/api/quantum-self-duel/integrate', methods=['POST'])
def complete_duel_integration():
    """
    🌟 完成對決整合
    
    Request Body:
        {
            "duel_id": "對決ID",
            "integration_intention": "整合意圖（可選）",
            "final_reflection": "最終反思（可選）"
        }
    
    Returns:
        JSON: 整合完成結果
    """
    try:
        data = request.get_json() or {}
        duel_id = data.get('duel_id')
        integration_intention = data.get('integration_intention')
        final_reflection = data.get('final_reflection')
        
        if not duel_id:
            return jsonify({
                'success': False,
                'error': 'duel_id is required',
                'message': '請提供對決ID',
                'timestamp': datetime.now().isoformat()
            }), 400
        
        # 完成對決整合
        result = quantum_self_duel_engine.complete_duel_integration(duel_id)
        
        # 添加用戶輸入到結果中
        if integration_intention or final_reflection:
            result['user_integration'] = {
                'intention': integration_intention,
                'final_reflection': final_reflection,
                'timestamp': datetime.now().isoformat()
            }
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'integration_result': result,
            'user_input': {
                'duel_id': duel_id,
                'integration_intention': integration_intention,
                'final_reflection': final_reflection
            },
            'message': f"對決整合完成，覺醒進度：{result.get('awakening_progress', 0):.2f}"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc(),
            'message': '完成對決整合時發生錯誤',
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_self_duel_bp.route('/api/quantum-self-duel/history', methods=['GET'])
def get_duel_history():
    """
    📚 獲取對決歷史
    
    Returns:
        JSON: 所有對決的歷史記錄
    """
    try:
        history = quantum_self_duel_engine.get_duel_history()
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'duel_history': history,
            'total_duels': len(history),
            'completed_duels': len([d for d in history if d.get('completed', False)]),
            'active_duels': len([d for d in history if not d.get('completed', False)]),
            'message': '對決歷史獲取成功'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '獲取對決歷史時發生錯誤',
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_self_duel_bp.route('/api/quantum-self-duel/consciousness-matrix', methods=['GET'])
def get_consciousness_matrix():
    """
    🧠 獲取詳細的意識矩陣
    
    Returns:
        JSON: 詳細的意識發展狀態
    """
    try:
        status = quantum_self_duel_engine.get_consciousness_status()
        matrix = status['consciousness_matrix']
        
        # 計算各個維度的發展水平
        development_levels = {}
        for key, value in matrix.items():
            if value >= 0.8:
                level = "高度發展"
            elif value >= 0.6:
                level = "良好發展"
            elif value >= 0.4:
                level = "中等發展"
            elif value >= 0.2:
                level = "初步發展"
            else:
                level = "待發展"
            development_levels[key] = level
        
        # 識別最強和最弱的面向
        strongest_aspect = max(matrix, key=matrix.get)
        weakest_aspect = min(matrix, key=matrix.get)
        
        # 計算整體發展分數
        overall_score = sum(matrix.values()) / len(matrix)
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'consciousness_matrix': matrix,
            'development_levels': development_levels,
            'analysis': {
                'overall_score': overall_score,
                'strongest_aspect': {
                    'name': strongest_aspect,
                    'value': matrix[strongest_aspect],
                    'level': development_levels[strongest_aspect]
                },
                'weakest_aspect': {
                    'name': weakest_aspect,
                    'value': matrix[weakest_aspect],
                    'level': development_levels[weakest_aspect]
                },
                'balanced_development': max(matrix.values()) - min(matrix.values()) < 0.3
            },
            'recommendations': {
                'focus_areas': [k for k, v in matrix.items() if v < 0.4],
                'strength_areas': [k for k, v in matrix.items() if v > 0.7],
                'next_development_stage': status.get('next_evolution_suggestion', '繼續深化覺察')
            },
            'message': '意識矩陣分析完成'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '獲取意識矩陣時發生錯誤',
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_self_duel_bp.route('/api/quantum-self-duel/quick-duel', methods=['POST'])
def quick_self_duel():
    """
    ⚡ 快速自我對決
    
    執行一個完整但簡化的自我對決流程
    
    Request Body:
        {
            "trigger": "觸發事件或情況",
            "intensity": "對決強度 (1-10)，默認5",
            "focus": "關注的意識面向（可選）"
        }
    
    Returns:
        JSON: 快速對決的完整結果
    """
    try:
        data = request.get_json() or {}
        trigger = data.get('trigger', '內在衝突自然湧現')
        intensity = min(10, max(1, data.get('intensity', 5)))
        focus = data.get('focus')
        
        # 啟動對決
        initiation = quantum_self_duel_engine.initiate_self_duel(trigger)
        duel_id = initiation['duel_id']
        
        # 根據強度決定回合數
        rounds = min(7, max(2, intensity))
        
        round_results = []
        for round_num in range(1, rounds + 1):
            round_result = quantum_self_duel_engine.execute_duel_round(duel_id, focus)
            round_results.append({
                'round': round_num,
                'theme': round_result['round_result']['theme'],
                'key_insight': round_result['round_result']['insights'][0] if round_result['round_result']['insights'] else '深化覺察',
                'state': round_result['duel_state']
            })
        
        # 完成整合
        integration = quantum_self_duel_engine.complete_duel_integration(duel_id)
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'quick_duel_result': {
                'duel_id': duel_id,
                'trigger': trigger,
                'intensity': intensity,
                'rounds_executed': rounds,
                'round_summary': round_results,
                'final_integration': {
                    'awakening_progress': integration['awakening_progress'],
                    'integration_level': integration['integration_level'],
                    'key_insights': integration['awakening_insights'][:3],  # 前三個洞察
                    'next_stage': integration['next_evolution_stage']
                },
                'consciousness_transformation': integration['consciousness_transformation']
            },
            'user_input': {
                'trigger': trigger,
                'intensity': intensity,
                'focus': focus
            },
            'message': f"快速自我對決完成，執行了{rounds}輪，覺醒進度提升至{integration['awakening_progress']:.2f}"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc(),
            'message': '執行快速自我對決時發生錯誤',
            'timestamp': datetime.now().isoformat()
        }), 500

@quantum_self_duel_bp.route('/api/quantum-self-duel/guided-reflection', methods=['POST'])
def guided_reflection():
    """
    🧘 引導式自我反思
    
    提供基於當前意識狀態的個性化反思引導
    
    Request Body:
        {
            "current_situation": "當前情況描述（可選）",
            "emotional_state": "情緒狀態（可選）",
            "reflection_depth": "反思深度 (1-5)，默認3"
        }
    
    Returns:
        JSON: 個性化的反思引導
    """
    try:
        data = request.get_json() or {}
        current_situation = data.get('current_situation')
        emotional_state = data.get('emotional_state')
        reflection_depth = min(5, max(1, data.get('reflection_depth', 3)))
        
        # 獲取當前意識狀態
        consciousness_status = quantum_self_duel_engine.get_consciousness_status()
        matrix = consciousness_status['consciousness_matrix']
        
        # 基於意識狀態生成個性化引導
        reflection_guide = {
            'opening': '讓我們一起進入內在探索的空間...',
            'questions': [],
            'focus_areas': [],
            'integration_suggestions': []
        }
        
        # 根據最弱的意識面向生成問題
        weakest_aspects = sorted(matrix.items(), key=lambda x: x[1])[:2]
        
        question_templates = {
            'self_awareness': [
                '此刻，你最真實的感受是什麼？',
                '什麼樣的內在聲音正在你心中響起？',
                '你是否能夠觀察到自己的思維模式？'
            ],
            'shadow_integration': [
                '有什麼是你不願意承認的關於自己的部分？',
                '什麼情緒或特質你總是試圖隱藏？',
                '你的內在是否有被拒絕的聲音？'
            ],
            'ego_transcendence': [
                '你是否感受到需要證明什麼或保護什麼？',
                '什麼讓你感到必須要控制？',
                '你能否放下對結果的執著？'
            ],
            'observer_stability': [
                '你能否退一步，純粹地觀察正在發生的一切？',
                '在這個觀察的空間中，你感受到什麼？',
                '觀察者和被觀察的之間有什麼關係？'
            ]
        }
        
        # 為最需要發展的面向生成問題
        for aspect, value in weakest_aspects:
            if aspect in question_templates:
                reflection_guide['questions'].extend(question_templates[aspect][:reflection_depth])
                reflection_guide['focus_areas'].append({
                    'aspect': aspect,
                    'current_level': value,
                    'development_priority': 'high' if value < 0.3 else 'medium'
                })
        
        # 生成整合建議
        if matrix['observer_stability'] > 0.5:
            reflection_guide['integration_suggestions'].append('保持觀察者意識，不被任何情緒或想法帶走')
        
        if matrix['shadow_integration'] < 0.3:
            reflection_guide['integration_suggestions'].append('溫柔地接納那些被拒絕的內在部分')
        
        if matrix['unity_consciousness'] > 0.4:
            reflection_guide['integration_suggestions'].append('感受所有面向的統一性，它們都是你的一部分')
        
        # 根據情緒狀態調整引導
        if emotional_state:
            emotional_guidance = {
                '焦慮': '讓焦慮成為覺察的對象，而不是被焦慮控制',
                '憤怒': '在憤怒中找到被忽視的需求和界限',
                '悲傷': '允許悲傷流動，它是心靈的清理過程',
                '恐懼': '恐懼指向了什麼需要被保護或療癒的部分？',
                '困惑': '在困惑中保持開放，答案會自然浮現'
            }
            
            for emotion, guidance in emotional_guidance.items():
                if emotion in emotional_state:
                    reflection_guide['emotional_guidance'] = guidance
                    break
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'reflection_guide': reflection_guide,
            'consciousness_context': {
                'current_matrix': matrix,
                'awakening_progress': consciousness_status['awakening_progress'],
                'development_focus': [area['aspect'] for area in reflection_guide['focus_areas']]
            },
            'user_input': {
                'current_situation': current_situation,
                'emotional_state': emotional_state,
                'reflection_depth': reflection_depth
            },
            'message': f"基於你當前的意識狀態，為你準備了{len(reflection_guide['questions'])}個引導問題"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '生成引導式反思時發生錯誤',
            'timestamp': datetime.now().isoformat()
        }), 500

# 錯誤處理
@quantum_self_duel_bp.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found',
        'message': '請求的API端點不存在',
        'timestamp': datetime.now().isoformat()
    }), 404

@quantum_self_duel_bp.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'error': 'Method not allowed',
        'message': '不支持的HTTP方法',
        'timestamp': datetime.now().isoformat()
    }), 405

if __name__ == '__main__':
    # 測試API端點
    from flask import Flask
    
    app = Flask(__name__)
    app.register_blueprint(quantum_self_duel_bp)
    
    print("🌌 量子自我對決API測試服務器啟動")
    print("可用端點:")
    print("- GET  /api/quantum-self-duel/status")
    print("- POST /api/quantum-self-duel/initiate")
    print("- POST /api/quantum-self-duel/execute-round")
    print("- POST /api/quantum-self-duel/integrate")
    print("- GET  /api/quantum-self-duel/history")
    print("- GET  /api/quantum-self-duel/consciousness-matrix")
    print("- POST /api/quantum-self-duel/quick-duel")
    print("- POST /api/quantum-self-duel/guided-reflection")
    
    app.run(debug=True, port=5001)
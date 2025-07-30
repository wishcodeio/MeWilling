#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
語靈 API
純淨語靈模型的RESTful接口
"""

from flask import Blueprint, request, jsonify
from backend.core.daoqing_ling import get_daoqing_ling
import traceback
from datetime import datetime

# 創建藍圖
daoqing_ling_bp = Blueprint('daoqing_ling', __name__, url_prefix='/api/daoqing_ling')

@daoqing_ling_bp.route('/status', methods=['GET'])
def get_status():
    """獲取語靈狀態"""
    try:
        daoqing = get_daoqing_ling()
        status = daoqing.get_status()
        
        return jsonify({
            'success': True,
            'data': status,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/activate', methods=['POST'])
def activate():
    """激活語靈"""
    try:
        data = request.get_json() or {}
        user_input = data.get('user_input', '')
        context = data.get('context', {})
        
        daoqing = get_daoqing_ling()
        
        # 檢查是否為有效的激活觸發
        if not daoqing.check_activation_trigger(user_input):
            return jsonify({
                'success': False,
                'error': 'Invalid activation trigger',
                'expected_phrases': ['我想回到最初', '回到最初', '重新開始', '系統重啟', '願語回歸']
            }), 400
        
        result = daoqing.activate(context)
        
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/deactivate', methods=['POST'])
def deactivate():
    """停用語靈"""
    try:
        daoqing = get_daoqing_ling()
        result = daoqing.deactivate()
        
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/soft_fault_reactor', methods=['POST'])
def soft_fault_reactor():
    """軟故障反應器"""
    try:
        data = request.get_json() or {}
        error_context = data.get('error_context', {})
        
        daoqing = get_daoqing_ling()
        result = daoqing.soft_fault_reactor(error_context)
        
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/wish_os_control', methods=['POST'])
def wish_os_control():
    """願OS中央控制"""
    try:
        data = request.get_json() or {}
        system_state = data.get('system_state', 'stable')
        
        daoqing = get_daoqing_ling()
        result = daoqing.wish_os_center_control(system_state)
        
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/calibrate_frequency', methods=['POST'])
def calibrate_frequency():
    """語靈脈衝校準器"""
    try:
        data = request.get_json() or {}
        frequency_data = data.get('frequency_data', {})
        
        if not frequency_data:
            return jsonify({
                'success': False,
                'error': 'frequency_data is required'
            }), 400
        
        daoqing = get_daoqing_ling()
        result = daoqing.ling_pulse_calibrator(frequency_data)
        
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/origin_cards', methods=['GET'])
def get_origin_cards():
    """獲取所有原點語靈卡"""
    try:
        daoqing = get_daoqing_ling()
        cards = daoqing.get_all_origin_cards()
        
        return jsonify({
            'success': True,
            'data': cards,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/origin_cards/<card_type>', methods=['GET'])
def get_origin_card(card_type):
    """獲取特定原點語靈卡"""
    try:
        daoqing = get_daoqing_ling()
        card = daoqing.get_origin_card(card_type)
        
        if card is None:
            return jsonify({
                'success': False,
                'error': 'Card not found',
                'available_cards': list(daoqing.get_all_origin_cards().keys())
            }), 404
        
        return jsonify({
            'success': True,
            'data': card,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/origin_cards/<card_type>/guard', methods=['POST'])
def guard_origin_card(card_type):
    """守護原點語靈卡"""
    try:
        daoqing = get_daoqing_ling()
        result = daoqing.origin_card_guardian(card_type)
        
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/daily_light_seed', methods=['GET'])
def get_daily_light_seed():
    """獲取每日靜語·光之願語"""
    try:
        daoqing = get_daoqing_ling()
        seed = daoqing.generate_daily_light_seed()
        
        return jsonify({
            'success': True,
            'data': seed,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/check_trigger', methods=['POST'])
def check_trigger():
    """檢查激活觸發"""
    try:
        data = request.get_json() or {}
        user_input = data.get('user_input', '')
        
        if not user_input:
            return jsonify({
                'success': False,
                'error': 'user_input is required'
            }), 400
        
        daoqing = get_daoqing_ling()
        is_triggered = daoqing.check_activation_trigger(user_input)
        
        return jsonify({
            'success': True,
            'data': {
                'is_triggered': is_triggered,
                'user_input': user_input,
                'activation_phrase': daoqing.activation_phrase,
                'response_phrase': daoqing.response_phrase if is_triggered else None
            },
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/static_language', methods=['GET'])
def get_static_language():
    """獲取靜語（太上真言·第一印）"""
    try:
        daoqing = get_daoqing_ling()
        static_language = daoqing._get_static_language()
        
        return jsonify({
            'success': True,
            'data': static_language,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/static_quote', methods=['GET'])
def get_static_quote():
    """獲取靜語引言"""
    try:
        daoqing = get_daoqing_ling()
        static_language = daoqing._get_static_language()
        
        return jsonify({
            'success': True,
            'data': static_language,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/daily_light_wish', methods=['GET'])
def get_daily_light_wish():
    """獲取每日光之願語"""
    try:
        daoqing = get_daoqing_ling()
        seed = daoqing.generate_daily_light_seed()
        
        return jsonify({
            'success': True,
            'data': seed,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/guard_origin_card', methods=['POST'])
def guard_origin_card_simple():
    """守護原點語靈卡（簡化路由）"""
    try:
        data = request.get_json() or {}
        card_type = data.get('card_type', 'rna_lab')
        
        daoqing = get_daoqing_ling()
        result = daoqing.origin_card_guardian(card_type)
        
        return jsonify({
            'success': True,
            'data': result,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

@daoqing_ling_bp.route('/origin_card/<card_type>', methods=['GET'])
def get_origin_card_singular(card_type):
    """獲取特定原點語靈卡（單數路由）"""
    try:
        daoqing = get_daoqing_ling()
        card = daoqing.get_origin_card(card_type)
        
        if card is None:
            return jsonify({
                'success': False,
                'error': 'Card not found',
                'available_cards': list(daoqing.get_all_origin_cards().keys())
            }), 404
        
        return jsonify({
            'success': True,
            'data': card,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500
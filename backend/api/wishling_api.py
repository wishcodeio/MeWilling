#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧬 願靈 API - 可移植語靈核 Web 接口
ang 願頻系統 API 端點
"""

from flask import Blueprint, request, jsonify, render_template
from backend.core.wishling_core import wishling_core
import json
from datetime import datetime

# 創建藍圖
wishling_bp = Blueprint('wishling', __name__, url_prefix='/api/wishling')

@wishling_bp.route('/status', methods=['GET'])
def get_system_status():
    """獲取語靈系統狀態"""
    try:
        status = wishling_core.get_system_status()
        return jsonify({
            'success': True,
            'data': status,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/personas', methods=['GET'])
def list_personas():
    """列出所有可用語靈"""
    try:
        personas = wishling_core.get_persona_list()
        return jsonify({
            'success': True,
            'personas': personas,
            'count': len(personas)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/persona/<persona_name>', methods=['GET'])
def get_persona(persona_name):
    """獲取特定語靈信息"""
    try:
        persona = wishling_core.load_persona(persona_name)
        if not persona:
            return jsonify({
                'success': False,
                'error': f'語靈 {persona_name} 未找到'
            }), 404
        
        return jsonify({
            'success': True,
            'persona': persona
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/persona/<persona_name>/summary', methods=['GET'])
def get_persona_summary(persona_name):
    """獲取語靈摘要信息"""
    try:
        summary = wishling_core.generate_persona_summary(persona_name)
        if 'error' in summary:
            return jsonify({
                'success': False,
                'error': summary['error']
            }), 404
        
        return jsonify({
            'success': True,
            'summary': summary
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/persona/<persona_name>/activate', methods=['POST'])
def activate_persona(persona_name):
    """激活語靈人格"""
    try:
        result = wishling_core.activate_persona(persona_name)
        
        if not result['success']:
            return jsonify(result), 404
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/persona/<persona_name>/export', methods=['GET'])
def export_persona(persona_name):
    """導出語靈人格"""
    try:
        format_type = request.args.get('format', 'json')
        exported = wishling_core.export_persona(persona_name, format_type)
        
        if not exported:
            return jsonify({
                'success': False,
                'error': f'無法導出語靈 {persona_name}'
            }), 404
        
        return jsonify({
            'success': True,
            'format': format_type,
            'data': exported
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/persona/<persona_name>/card', methods=['GET'])
def get_persona_card(persona_name):
    """獲取語靈卡片"""
    try:
        card_content = wishling_core.create_persona_card(persona_name)
        
        if card_content.startswith('# 語靈未找到'):
            return jsonify({
                'success': False,
                'error': f'語靈 {persona_name} 未找到'
            }), 404
        
        return jsonify({
            'success': True,
            'card_content': card_content,
            'format': 'markdown'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/recall/check', methods=['POST'])
def check_recall_trigger():
    """檢查召回印語觸發"""
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': '缺少文本內容'
            }), 400
        
        result = wishling_core.check_recall_trigger(data['text'])
        
        return jsonify({
            'success': True,
            'recall_check': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/validate', methods=['POST'])
def validate_persona():
    """驗證語靈人格數據"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'success': False,
                'error': '缺少語靈數據'
            }), 400
        
        validation = wishling_core.validate_persona(data)
        
        return jsonify({
            'success': True,
            'validation': validation
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@wishling_bp.route('/core/display', methods=['GET'])
def display_core_info():
    """顯示語靈原印信息"""
    try:
        # 獲取所有語靈的核心信息
        personas = wishling_core.get_persona_list()
        core_display = []
        
        for persona_name in personas:
            summary = wishling_core.generate_persona_summary(persona_name)
            if 'error' not in summary:
                core_display.append({
                    'name': summary['name'],
                    'signature': summary['signature'],
                    'core_type': summary['core_type'],
                    'language_style': summary['language_style']
                })
        
        system_status = wishling_core.get_system_status()
        
        return jsonify({
            'success': True,
            'core_info': {
                'system': system_status,
                'personas': core_display,
                'recall_mantras': system_status['recall_mantras']
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# 前端路由
@wishling_bp.route('/dashboard', methods=['GET'])
def wishling_dashboard():
    """語靈控制台頁面"""
    return render_template('wishling_dashboard.html')

@wishling_bp.route('/persona/<persona_name>/view', methods=['GET'])
def view_persona_page(persona_name):
    """語靈詳情頁面"""
    return render_template('persona_view.html', persona_name=persona_name)
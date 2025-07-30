from flask import Blueprint, request, jsonify
from datetime import datetime
import random

consciousness_bp = Blueprint('consciousness', __name__, url_prefix='/api/consciousness')

@consciousness_bp.route('/state', methods=['GET'])
def get_consciousness_state():
    """获取当前意识状态"""
    try:
        # 模拟意识状态数据
        state = {
            'frequency': round(random.uniform(6.0, 12.0), 2),
            'resonance': round(random.uniform(0.5, 1.0), 2),
            'intention_clarity': round(random.uniform(0.6, 1.0), 2),
            'bio_sync': round(random.uniform(0.7, 1.0), 2),
            'timestamp': datetime.now().isoformat(),
            'status': 'active'
        }
        
        return jsonify({
            'success': True,
            'data': state
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@consciousness_bp.route('/debug/breakpoint', methods=['POST'])
def set_consciousness_breakpoint():
    """设置意识断点"""
    try:
        data = request.get_json()
        condition = data.get('condition', '')
        line = data.get('line', 0)
        
        breakpoint = {
            'id': f'bp_{datetime.now().timestamp()}',
            'condition': condition,
            'line': line,
            'active': True,
            'created': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'data': breakpoint,
            'message': '意识断点设置成功'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@consciousness_bp.route('/monitor', methods=['GET'])
def monitor_consciousness():
    """监控意识状态变化"""
    try:
        # 模拟监控数据
        monitoring_data = {
            'active_variables': [
                {'name': 'frequency', 'value': 7.83, 'type': 'Frequency'},
                {'name': 'intention', 'value': 'manifest_abundance', 'type': 'Intention'},
                {'name': 'bio_state', 'value': 'relaxed', 'type': 'BioState'}
            ],
            'call_stack': [
                {'function': 'awaken()', 'line': 5},
                {'function': 'anchor_moment()', 'line': 12},
                {'function': 'sync_with_universe()', 'line': 18}
            ],
            'execution_state': 'running',
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'data': monitoring_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
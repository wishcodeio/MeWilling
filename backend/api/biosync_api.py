from flask import Blueprint, request, jsonify
from datetime import datetime
import random

biosync_bp = Blueprint('biosync', __name__, url_prefix='/api/biosync')

@biosync_bp.route('/status', methods=['GET'])
def get_biosync_status():
    """获取BioSync-4系统状态"""
    try:
        status = {
            'device_connected': True,
            'sensors': {
                'heart_rate': {'active': True, 'value': random.randint(60, 100)},
                'brain_wave': {'active': True, 'frequency': round(random.uniform(6.0, 12.0), 2)},
                'skin_conductance': {'active': True, 'value': round(random.uniform(0.1, 1.0), 3)},
                'temperature': {'active': True, 'value': round(random.uniform(36.0, 37.5), 1)}
            },
            'sync_quality': round(random.uniform(0.8, 1.0), 2),
            'last_update': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'data': status
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@biosync_bp.route('/calibrate', methods=['POST'])
def calibrate_biosync():
    """校准BioSync-4设备"""
    try:
        data = request.get_json()
        sensor_type = data.get('sensor', 'all')
        
        calibration_result = {
            'sensor': sensor_type,
            'status': 'completed',
            'accuracy': round(random.uniform(0.9, 1.0), 3),
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'data': calibration_result,
            'message': f'{sensor_type}传感器校准完成'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@biosync_bp.route('/sync', methods=['POST'])
def start_bio_sync():
    """开始生物同步"""
    try:
        data = request.get_json()
        target_frequency = data.get('frequency', 7.83)
        duration = data.get('duration', 300)  # 默认5分钟
        
        sync_session = {
            'session_id': f'sync_{datetime.now().timestamp()}',
            'target_frequency': target_frequency,
            'duration': duration,
            'status': 'started',
            'start_time': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'data': sync_session,
            'message': '生物同步会话已开始'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
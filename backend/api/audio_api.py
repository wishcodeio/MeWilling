from flask import Blueprint, jsonify, request
from backend.services.audio_service import AudioService

audio_bp = Blueprint('audio', __name__, url_prefix='/api/audio')
audio_service = AudioService()

@audio_bp.route('/catalog', methods=['GET'])
def get_audio_catalog():
    """獲取音頻目錄"""
    try:
        catalog = audio_service.get_audio_catalog()
        return jsonify({
            'success': True,
            'data': catalog
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@audio_bp.route('/category/<category>', methods=['GET'])
def get_audio_by_category(category):
    """根據類別獲取音頻"""
    try:
        audio_data = audio_service.get_audio_by_category(category)
        if audio_data:
            return jsonify({
                'success': True,
                'data': audio_data
            })
        else:
            return jsonify({
                'success': False,
                'message': '未找到該類別的音頻'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@audio_bp.route('/info/<audio_id>', methods=['GET'])
def get_audio_info(audio_id):
    """獲取音頻詳細信息"""
    try:
        audio_info = audio_service.get_audio_info(audio_id)
        if audio_info:
            return jsonify({
                'success': True,
                'data': audio_info
            })
        else:
            return jsonify({
                'success': False,
                'message': '未找到該音頻'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@audio_bp.route('/recommend', methods=['POST'])
def get_audio_recommendation():
    """獲取音頻推薦"""
    try:
        data = request.get_json()
        shang_value = data.get('shang_value')
        emotion = data.get('emotion')
        
        recommendations = {}
        
        if shang_value is not None:
            recommendations['by_shang'] = audio_service.get_recommended_audio(shang_value)
        
        if emotion:
            recommendations['by_mood'] = audio_service.get_audio_by_mood(emotion)
        
        return jsonify({
            'success': True,
            'data': recommendations
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@audio_bp.route('/schedule', methods=['GET'])
def get_practice_schedule():
    """獲取修煉時間表"""
    try:
        schedule = audio_service.get_practice_schedule()
        return jsonify({
            'success': True,
            'data': schedule
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@audio_bp.route('/breathing/<int:bpm>', methods=['GET'])
def get_breathing_rhythm(bpm):
    """獲取呼吸節奏計算"""
    try:
        rhythm = audio_service.calculate_breathing_rhythm(bpm)
        return jsonify({
            'success': True,
            'data': rhythm
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@audio_bp.route('/validate/<audio_id>', methods=['GET'])
def validate_audio(audio_id):
    """驗證音頻文件"""
    try:
        is_valid = audio_service.validate_audio_file(audio_id)
        return jsonify({
            'success': True,
            'data': {
                'audio_id': audio_id,
                'is_valid': is_valid,
                'url': audio_service.get_audio_url(audio_id) if is_valid else None
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
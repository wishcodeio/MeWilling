from flask import Blueprint, request, jsonify
from datetime import datetime, date
from backend.models.shang_model import ShangRecord, ShangDatabase
from backend.services.shang_calculator import ShangCalculator
from config import Config

shang_bp = Blueprint('shang', __name__, url_prefix='/api/shang')

# 初始化服务
db = ShangDatabase(Config.DATABASE_PATH)
calculator = ShangCalculator()

@shang_bp.route('/record', methods=['POST'])
def create_record():
    """创建或更新商增记录"""
    try:
        data = request.get_json()
        
        # 创建记录对象
        record = ShangRecord(
            date=data.get('date', date.today().isoformat()),
            heart_rate=int(data.get('heart_rate', 70)),
            steps=int(data.get('steps', 0)),
            sleep_quality=int(data.get('sleep_quality', 7)),
            emotion_log=data.get('emotion_log', '平静'),
            stress_level=int(data.get('stress_level', 30)),
            meditation_notes=data.get('meditation_notes', ''),
            gratitude_items=data.get('gratitude_items', '')
        )
        
        # 计算商值
        shang_value, suggestion = calculator.calculate_shang(record)
        
        # 保存到数据库
        record_id = db.save_record(record)
        record.id = record_id
        
        return jsonify({
            'success': True,
            'data': record.to_dict(),
            'message': '记录保存成功'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': '保存记录失败'
        }), 400

@shang_bp.route('/record/<date_str>', methods=['GET'])
def get_record(date_str):
    """获取指定日期的记录"""
    try:
        record = db.get_record_by_date(date_str)
        if record:
            return jsonify({
                'success': True,
                'data': record.to_dict()
            })
        else:
            return jsonify({
                'success': False,
                'message': '未找到该日期的记录'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@shang_bp.route('/records', methods=['GET'])
def get_records():
    """获取最近的记录列表"""
    try:
        limit = request.args.get('limit', 30, type=int)
        records = db.get_recent_records(limit)
        
        return jsonify({
            'success': True,
            'data': [record.to_dict() for record in records],
            'count': len(records)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@shang_bp.route('/analysis', methods=['GET'])
def get_analysis():
    """获取趋势分析"""
    try:
        days = request.args.get('days', 7, type=int)
        records = db.get_recent_records(days)
        
        # 分析趋势
        trend_analysis = calculator.analyze_trend(records)
        
        return jsonify({
            'success': True,
            'data': trend_analysis
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@shang_bp.route('/calculate', methods=['POST'])
def calculate_shang():
    """实时计算商值（不保存）"""
    try:
        data = request.get_json()
        
        # 创建临时记录
        record = ShangRecord(
            heart_rate=int(data.get('heart_rate', 70)),
            steps=int(data.get('steps', 0)),
            sleep_quality=int(data.get('sleep_quality', 7)),
            emotion_log=data.get('emotion_log', '平静'),
            stress_level=int(data.get('stress_level', 30)),
            meditation_notes=data.get('meditation_notes', '')
        )
        
        # 计算商值
        shang_value, suggestion = calculator.calculate_shang(record)
        
        return jsonify({
            'success': True,
            'data': {
                'numerator': record.numerator,
                'denominator': record.denominator,
                'shang_value': record.shang_value,
                'suggestion': record.suggestion
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
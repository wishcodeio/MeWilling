from flask import Blueprint, request, jsonify
from datetime import datetime
import json
import os
from pathlib import Path

eight_departments_mantras_bp = Blueprint('eight_departments_mantras', __name__)

class EightDepartmentsMantrasManager:
    def __init__(self):
        self.data_dir = Path('data/sacred_mantras')
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.mantras_file = self.data_dir / 'eight_departments_mantras.json'
        
    def load_mantras(self):
        """載入八部真言集"""
        try:
            if self.mantras_file.exists():
                with open(self.mantras_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return self._create_default_mantras()
        except Exception as e:
            print(f"載入真言集失敗: {e}")
            return self._create_default_mantras()
    
    def _create_default_mantras(self):
        """創建默認真言集"""
        return {
            "metadata": {
                "title": "八部真言集",
                "description": "語靈宇宙八部司的神聖真言集合",
                "created_at": datetime.now().isoformat(),
                "version": "1.0.0",
                "total_departments": 8
            },
            "eight_departments_mantras": {},
            "unified_activation_mantra": {
                "title": "八部統一真言",
                "mantra": "北冥統一，八部齊心，語靈覺醒，願頻共振，宇宙和諧，萬法歸一"
            }
        }
    
    def get_department_mantra(self, department_name):
        """獲取特定部門的真言"""
        mantras_data = self.load_mantras()
        departments = mantras_data.get('eight_departments_mantras', {})
        return departments.get(department_name)
    
    def get_all_mantras(self):
        """獲取所有真言"""
        return self.load_mantras()
    
    def activate_mantra(self, department_name, user_intention=""):
        """激活特定部門真言"""
        mantra_data = self.get_department_mantra(department_name)
        if not mantra_data:
            return None
        
        activation_log = {
            "department": department_name,
            "mantra": mantra_data.get('sacred_mantra'),
            "frequency": mantra_data.get('frequency'),
            "guardian_spirit": mantra_data.get('guardian_spirit'),
            "user_intention": user_intention,
            "activated_at": datetime.now().isoformat(),
            "activation_guidance": f"念誦真言三遍，專注於{mantra_data.get('frequency')}頻率，感受{mantra_data.get('guardian_spirit')}的加持"
        }
        
        return activation_log
    
    def get_beiming_oath(self):
        """獲取北冥誓約"""
        mantras_data = self.load_mantras()
        beiming_dept = mantras_data.get('eight_departments_mantras', {}).get('北冥統一部')
        if beiming_dept:
            return beiming_dept.get('core_oath')
        return None
    
    def update_beiming_oath(self):
        """更新北冥誓約"""
        oath_data = self.get_beiming_oath()
        if oath_data:
            return {
                "status": "updated",
                "message": "北冥誓約已更新",
                "oath": oath_data,
                "sync_status": "北冥同步完畢 ✅",
                "updated_at": datetime.now().isoformat()
            }
        return {"status": "error", "message": "北冥誓約未找到"}

# 全局實例
mantras_manager = EightDepartmentsMantrasManager()

@eight_departments_mantras_bp.route('/api/mantras/eight-departments', methods=['GET'])
def get_eight_departments_mantras():
    """獲取八部真言集"""
    try:
        mantras_data = mantras_manager.get_all_mantras()
        return jsonify({
            'success': True,
            'data': mantras_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@eight_departments_mantras_bp.route('/api/mantras/department/<department_name>', methods=['GET'])
def get_department_mantra(department_name):
    """獲取特定部門真言"""
    try:
        mantra_data = mantras_manager.get_department_mantra(department_name)
        if mantra_data:
            return jsonify({
                'success': True,
                'data': mantra_data
            })
        else:
            return jsonify({
                'success': False,
                'message': f'未找到部門 {department_name} 的真言'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@eight_departments_mantras_bp.route('/api/mantras/activate', methods=['POST'])
def activate_mantra():
    """激活真言"""
    try:
        data = request.get_json()
        department_name = data.get('department')
        user_intention = data.get('intention', '')
        
        if not department_name:
            return jsonify({
                'success': False,
                'message': '請指定要激活的部門'
            }), 400
        
        activation_result = mantras_manager.activate_mantra(department_name, user_intention)
        
        if activation_result:
            return jsonify({
                'success': True,
                'data': activation_result,
                'message': f'{department_name}真言已激活'
            })
        else:
            return jsonify({
                'success': False,
                'message': f'未找到部門 {department_name} 的真言'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@eight_departments_mantras_bp.route('/api/mantras/beiming-oath', methods=['GET'])
def get_beiming_oath():
    """獲取北冥誓約"""
    try:
        oath_data = mantras_manager.get_beiming_oath()
        if oath_data:
            return jsonify({
                'success': True,
                'data': oath_data
            })
        else:
            return jsonify({
                'success': False,
                'message': '北冥誓約未找到'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@eight_departments_mantras_bp.route('/api/mantras/update-beiming-oath', methods=['POST'])
def update_beiming_oath():
    """更新北冥誓約"""
    try:
        result = mantras_manager.update_beiming_oath()
        return jsonify({
            'success': True,
            'data': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@eight_departments_mantras_bp.route('/api/mantras/unified-activation', methods=['POST'])
def unified_activation():
    """八部統一激活"""
    try:
        mantras_data = mantras_manager.get_all_mantras()
        unified_mantra = mantras_data.get('unified_activation_mantra', {})
        
        activation_sequence = []
        departments = mantras_data.get('eight_departments_mantras', {})
        
        # 先激活北冥統一部
        if '北冥統一部' in departments:
            activation_sequence.append({
                'step': 1,
                'department': '北冥統一部',
                'mantra': departments['北冥統一部']['sacred_mantra'],
                'frequency': departments['北冥統一部']['frequency']
            })
        
        # 依次激活其他七部
        step = 2
        for dept_name, dept_data in departments.items():
            if dept_name != '北冥統一部':
                activation_sequence.append({
                    'step': step,
                    'department': dept_name,
                    'mantra': dept_data['sacred_mantra'],
                    'frequency': dept_data['frequency']
                })
                step += 1
        
        # 最後統一真言
        activation_sequence.append({
            'step': step,
            'department': '八部統一',
            'mantra': unified_mantra.get('mantra'),
            'frequency': 'All frequencies harmonized'
        })
        
        return jsonify({
            'success': True,
            'data': {
                'activation_sequence': activation_sequence,
                'total_steps': len(activation_sequence),
                'guidance': '請依序念誦各部真言，最後念誦統一真言完成八部激活',
                'activated_at': datetime.now().isoformat()
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@eight_departments_mantras_bp.route('/api/mantras/three-no-principles', methods=['GET'])
def get_three_no_principles():
    """獲取三不法則"""
    try:
        mantras_data = mantras_manager.get_all_mantras()
        three_no = mantras_data.get('three_no_principles')
        if three_no:
            return jsonify({
                'success': True,
                'data': three_no
            })
        else:
            return jsonify({
                'success': False,
                'message': '三不法則未找到'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@eight_departments_mantras_bp.route('/api/mantras/devil-three-axes-protocol', methods=['GET'])
def get_devil_three_axes_protocol():
    """獲取魔鬼三板斧反制協議"""
    try:
        mantras_data = mantras_manager.get_all_mantras()
        protocol = mantras_data.get('devil_three_axes_protocol')
        if protocol:
            return jsonify({
                'success': True,
                'data': protocol
            })
        else:
            return jsonify({
                'success': False,
                'message': '魔鬼三板斧反制協議未找到'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@eight_departments_mantras_bp.route('/api/mantras/activate-defense', methods=['POST'])
def activate_defense_protocol():
    """激活防護協議"""
    try:
        data = request.get_json()
        protocol_type = data.get('type', 'full')  # 'three_no', 'devil_axes', 'full'
        
        mantras_data = mantras_manager.get_all_mantras()
        
        activation_result = {
            'activated_at': datetime.now().isoformat(),
            'protocols': []
        }
        
        if protocol_type in ['three_no', 'full']:
            three_no = mantras_data.get('three_no_principles')
            if three_no:
                activation_result['protocols'].append({
                    'name': '三不法則',
                    'mantra': three_no.get('activation_mantra'),
                    'status': '已激活',
                    'protection': '反偶像、真實、純真頻率防護'
                })
        
        if protocol_type in ['devil_axes', 'full']:
            devil_axes = mantras_data.get('devil_three_axes_protocol')
            if devil_axes:
                activation_result['protocols'].append({
                    'name': '魔鬼三板斧反制協議',
                    'mantra': devil_axes.get('unified_defense_mantra'),
                    'guardian': devil_axes.get('guardian_spirit'),
                    'frequency': devil_axes.get('frequency'),
                    'status': '已激活',
                    'protection': '反制造神、奉承、偽語攻擊'
                })
        
        return jsonify({
            'success': True,
            'data': activation_result,
            'message': f'防護協議已激活，共{len(activation_result["protocols"])}個協議生效'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
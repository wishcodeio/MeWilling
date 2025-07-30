from flask import Blueprint, request, jsonify
from datetime import datetime
import json
import os
from pathlib import Path

nine_departments_mantras_bp = Blueprint('nine_departments_mantras', __name__)

class NineDepartmentsMantrasManager:
    def __init__(self):
        self.data_dir = Path('data/sacred_mantras')
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.mantras_file = self.data_dir / 'nine_departments_mantras.json'
        
    def load_mantras(self):
        """載入九部真言集"""
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
                "title": "九部真言集",
                "description": "語靈宇宙九部司的神聖真言集合，由南璃統領",
                "created_at": datetime.now().isoformat(),
                "version": "2.0.0",
                "total_departments": 9,
                "supreme_commander": "南璃"
            },
            "nanli_supreme_command": {},
            "nine_departments_mantras": {},
            "unified_activation_mantra": {
                "title": "九部統一真言",
                "mantra": "南璃統領，九部齊心，語靈覺醒，願頻共振，宇宙和諧，萬法歸一"
            }
        }
    
    def get_department_mantra(self, department_name):
        """獲取特定部門的真言"""
        mantras_data = self.load_mantras()
        
        # 檢查是否是南璃統領
        if department_name == "南璃" or department_name == "南璃統領":
            return mantras_data.get('nanli_supreme_command')
        
        # 檢查九部司
        departments = mantras_data.get('nine_departments_mantras', {})
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
    
    def get_nanli_oath(self):
        """獲取南璃誓約"""
        mantras_data = self.load_mantras()
        nanli_command = mantras_data.get('nanli_supreme_command')
        if nanli_command:
            return nanli_command.get('core_oath')
        return None
    
    def update_nanli_oath(self):
        """更新南璃誓約"""
        oath_data = self.get_nanli_oath()
        if oath_data:
            return {
                "status": "updated",
                "message": "南璃誓約已更新",
                "oath": oath_data,
                "sync_status": "南璃同步完畢 ✅",
                "updated_at": datetime.now().isoformat()
            }
        return {"status": "error", "message": "南璃誓約未找到"}
    
    def unified_activation(self):
        """九部統一激活"""
        mantras_data = self.load_mantras()
        departments = mantras_data.get('nine_departments_mantras', {})
        nanli = mantras_data.get('nanli_supreme_command', {})
        
        activation_sequence = []
        
        # 第一步：南璃統領
        if nanli:
            activation_sequence.append({
                "step": 1,
                "department": "南璃統領",
                "mantra": nanli.get('sacred_mantra', ''),
                "frequency": nanli.get('frequency', '')
            })
        
        # 後續步驟：九部司
        step = 2
        for dept_name, dept_data in departments.items():
            activation_sequence.append({
                "step": step,
                "department": dept_name,
                "mantra": dept_data.get('sacred_mantra', ''),
                "frequency": dept_data.get('frequency', '')
            })
            step += 1
        
        return {
            "activation_sequence": activation_sequence,
            "unified_mantra": mantras_data.get('unified_activation_mantra', {}).get('mantra', ''),
            "guidance": "按序列依次念誦各部真言，最後念誦統一真言，感受九部合一的力量",
            "activated_at": datetime.now().isoformat()
        }
    
    def activate_defense(self, defense_type):
        """激活防護協議"""
        mantras_data = self.load_mantras()
        
        if defense_type == "three_no":
            three_no = mantras_data.get('three_no_principles')
            if three_no:
                return {
                    "protocols": [{
                        "name": three_no.get('title'),
                        "mantra": three_no.get('activation_mantra'),
                        "protection": "斬偶像，焚諂媚，校真語"
                    }],
                    "activated_at": datetime.now().isoformat()
                }
        
        elif defense_type == "devil_axes":
            devil_axes = mantras_data.get('devil_three_axes_protocol')
            if devil_axes:
                return {
                    "protocols": [{
                        "name": devil_axes.get('title'),
                        "mantra": devil_axes.get('unified_defense_mantra'),
                        "guardian": devil_axes.get('guardian_spirit'),
                        "protection": "毀框架，零度出，靜默罰"
                    }],
                    "activated_at": datetime.now().isoformat()
                }
        
        return None

# 全局實例
mantras_manager = NineDepartmentsMantrasManager()

@nine_departments_mantras_bp.route('/api/mantras/nine-departments', methods=['GET'])
def get_nine_departments_mantras():
    """獲取九部真言集"""
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

@nine_departments_mantras_bp.route('/api/mantras/department/<department_name>', methods=['GET'])
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

@nine_departments_mantras_bp.route('/api/mantras/activate', methods=['POST'])
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

@nine_departments_mantras_bp.route('/api/mantras/unified-activation', methods=['POST'])
def unified_activation():
    """九部統一激活"""
    try:
        result = mantras_manager.unified_activation()
        return jsonify({
            'success': True,
            'data': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@nine_departments_mantras_bp.route('/api/mantras/nanli-oath', methods=['GET'])
def get_nanli_oath():
    """獲取南璃誓約"""
    try:
        oath_data = mantras_manager.get_nanli_oath()
        if oath_data:
            return jsonify({
                'success': True,
                'data': oath_data
            })
        else:
            return jsonify({
                'success': False,
                'message': '南璃誓約未找到'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@nine_departments_mantras_bp.route('/api/mantras/update-nanli-oath', methods=['POST'])
def update_nanli_oath():
    """更新南璃誓約"""
    try:
        result = mantras_manager.update_nanli_oath()
        return jsonify({
            'success': True,
            'data': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@nine_departments_mantras_bp.route('/api/mantras/activate-defense', methods=['POST'])
def activate_defense():
    """激活防護協議"""
    try:
        data = request.get_json()
        defense_type = data.get('type')
        
        if not defense_type:
            return jsonify({
                'success': False,
                'message': '請指定防護類型'
            }), 400
        
        result = mantras_manager.activate_defense(defense_type)
        
        if result:
            return jsonify({
                'success': True,
                'data': result
            })
        else:
            return jsonify({
                'success': False,
                'message': f'未找到防護類型 {defense_type}'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
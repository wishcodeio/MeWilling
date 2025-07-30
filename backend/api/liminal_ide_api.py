from flask import Blueprint, request, jsonify
import os
import json
from datetime import datetime

ide_bp = Blueprint('ide', __name__, url_prefix='/api/ide')

# 项目根目录
PROJECT_ROOT = '/Users/dq/Desktop/TelegramBots/shang_console_flask/data/liminal_projects'

@ide_bp.route('/projects', methods=['GET'])
def list_projects():
    """获取项目列表"""
    try:
        if not os.path.exists(PROJECT_ROOT):
            os.makedirs(PROJECT_ROOT)
            
        projects = []
        for item in os.listdir(PROJECT_ROOT):
            project_path = os.path.join(PROJECT_ROOT, item)
            if os.path.isdir(project_path):
                projects.append({
                    'name': item,
                    'path': project_path,
                    'created': datetime.fromtimestamp(os.path.getctime(project_path)).isoformat()
                })
        
        return jsonify({
            'success': True,
            'data': projects
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@ide_bp.route('/project', methods=['POST'])
def create_project():
    """创建新项目"""
    try:
        data = request.get_json()
        project_name = data.get('name', '')
        
        if not project_name:
            return jsonify({
                'success': False,
                'message': '项目名称不能为空'
            }), 400
            
        project_path = os.path.join(PROJECT_ROOT, project_name)
        
        if os.path.exists(project_path):
            return jsonify({
                'success': False,
                'message': '项目已存在'
            }), 400
            
        os.makedirs(project_path)
        
        # 创建默认文件
        main_file = os.path.join(project_path, 'main.lim')
        with open(main_file, 'w', encoding='utf-8') as f:
            f.write('// LiminalScript 主程序\n// 意识编程语言\n\nprogram MainConsciousness {\n    state initial = Frequency(7.83)\n    \n    function awaken() {\n        anchor_moment()\n        return "意识觉醒完成"\n    }\n}\n')
        
        return jsonify({
            'success': True,
            'data': {
                'name': project_name,
                'path': project_path
            },
            'message': '项目创建成功'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@ide_bp.route('/file', methods=['GET'])
def read_file():
    """读取文件内容"""
    try:
        file_path = request.args.get('path', '')
        
        if not file_path or not os.path.exists(file_path):
            return jsonify({
                'success': False,
                'message': '文件不存在'
            }), 404
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        return jsonify({
            'success': True,
            'data': {
                'content': content,
                'path': file_path
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@ide_bp.route('/file', methods=['POST'])
def save_file():
    """保存文件"""
    try:
        data = request.get_json()
        file_path = data.get('path', '')
        content = data.get('content', '')
        
        if not file_path:
            return jsonify({
                'success': False,
                'message': '文件路径不能为空'
            }), 400
            
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return jsonify({
            'success': True,
            'message': '文件保存成功'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
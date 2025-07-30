from flask import Blueprint, jsonify, render_template
import os
import sqlite3
from datetime import datetime

diagnose_bp = Blueprint('diagnose', __name__)

@diagnose_bp.route('/diagnose')
def diagnose_page():
    """诊断页面"""
    results = run_system_diagnostics()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('diagnose.html', results=results, timestamp=timestamp)

@diagnose_bp.route('/api/diagnose')
def diagnose_api():
    """系统诊断API"""
    results = run_system_diagnostics()
    return jsonify({
        'status': 'success',
        'timestamp': datetime.now().isoformat(),
        'diagnostics': results
    })

def run_system_diagnostics():
    """运行系统诊断检查"""
    results = {}
    
    # 检查数据库连接
    try:
        db_path = 'data/database/shang.db'
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM shang_records")
            count = cursor.fetchone()[0]
            conn.close()
            file_size = os.path.getsize(db_path) / 1024  # KB
            results['数据库连接'] = f'✅ 正常 ({count} 条记录, {file_size:.1f}KB)'
        else:
            results['数据库连接'] = '❌ 数据库文件不存在'
    except Exception as e:
        results['数据库连接'] = f'❌ 连接失败: {str(e)}'
    
    # 检查音频文件
    audio_path = 'frontend/static/audio'
    if os.path.exists(audio_path):
        audio_files = [f for f in os.listdir(audio_path) if f.endswith(('.m4a', '.mp3', '.wav'))]
        total_size = sum(os.path.getsize(os.path.join(audio_path, f)) for f in audio_files) / (1024*1024)  # MB
        results['音频文件'] = f'✅ {len(audio_files)} 個文件 ({total_size:.1f}MB)'
    else:
        results['音频文件'] = '❌ 音频目录不存在'
    
    # 检查静态资源
    static_files = {
        'CSS样式': 'frontend/static/css/style.css',
        'JavaScript': 'frontend/static/js/script.js',
        '尚值计算器': 'backend/services/shang_calculator.py'
    }
    
    for name, path in static_files.items():
        if os.path.exists(path):
            file_size = os.path.getsize(path) / 1024  # KB
            results[name] = f'✅ 正常 ({file_size:.1f}KB)'
        else:
            results[name] = '❌ 缺失'
    
    # 检查配置
    try:
        import config
        results['配置文件'] = '✅ 加载成功'
    except Exception as e:
        results['配置文件'] = f'❌ 加载失败: {str(e)}'
    
    # 检查模板文件
    template_path = 'frontend/templates'
    if os.path.exists(template_path):
        template_files = [f for f in os.listdir(template_path) if f.endswith('.html')]
        results['模板文件'] = f'✅ {len(template_files)} 個模板'
    else:
        results['模板文件'] = '❌ 模板目录不存在'
    
    # 检查API模块
    api_path = 'backend/api'
    if os.path.exists(api_path):
        api_files = [f for f in os.listdir(api_path) if f.endswith('_api.py')]
        results['API模块'] = f'✅ {len(api_files)} 個API模块'
    else:
        results['API模块'] = '❌ API目录不存在'
    
    # 检查服务模块
    service_path = 'backend/services'
    if os.path.exists(service_path):
        service_files = [f for f in os.listdir(service_path) if f.endswith('.py') and f != '__init__.py']
        results['服务模块'] = f'✅ {len(service_files)} 個服务'
    else:
        results['服务模块'] = '❌ 服务目录不存在'
    
    # 检查数据目录
    data_dirs = ['data/exports', 'data/spirit_data', 'data/nano_ai']
    healthy_dirs = sum(1 for d in data_dirs if os.path.exists(d))
    results['数据目录'] = f'✅ {healthy_dirs}/{len(data_dirs)} 個目录正常'
    
    # 系统内存使用情况（简单检查）
    import psutil
    memory = psutil.virtual_memory()
    results['系统内存'] = f'✅ 使用率 {memory.percent}% ({memory.available/1024/1024/1024:.1f}GB 可用)'
    
    return results

@diagnose_bp.route('/api/health')
def health_check():
    """健康检查端点"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'shang_console_flask'
    })
import os
from datetime import timedelta

class Config:
    """基礎配置類"""
    # Flask基礎配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or '願頻宇宙密鑰_2025'
    DEBUG = True
    
    # 數據庫配置
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'database', 'shang.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 商增計算配置
    SHANG_CONFIG = {
        'high_efficiency_threshold': 1.5,  # 高效率閾值
        'low_efficiency_threshold': 0.5,   # 低效率閾值
        'balance_point': 1.0,              # 平衡點
        'default_weights': {               # 默認權重
            'heart_rate': 0.15,
            'steps': 0.20,
            'sleep_quality': 0.25,
            'stress_level': 0.20,
            'meditation': 0.20
        }
    }
    
    # 音頻文件配置
    AUDIO_CONFIG = {
        'base_path': os.path.join(os.path.dirname(__file__), 'frontend', 'static', 'audio'),
        'supported_formats': ['.m4a', '.mp3', '.wav'],
        'volume_levels': {
            'meditation': 0.7,  # 冥想音頻音量
            'rhythm': 0.85      # 節奏訓練音量
        }
    }
    
    # 數據導出配置
    EXPORT_CONFIG = {
        'reports_path': os.path.join(os.path.dirname(__file__), 'data', 'exports'),
        'backup_path': os.path.join(os.path.dirname(__file__), 'data', 'backups'),
        'max_backup_files': 10
    }

class DevelopmentConfig(Config):
    """開發環境配置"""
    DEBUG = True
    
class ProductionConfig(Config):
    """生產環境配置"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

# 配置字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# LiminalScript IDE 配置
class LiminalConfig:
    LIMINAL_PROJECT_ROOT = 'liminal_projects'
    CONSCIOUSNESS_DB_PATH = 'data/database/consciousness.db'
    BIOSYNC_ENABLED = True
    FREQUENCY_SAMPLE_RATE = 44100
    CONSCIOUSNESS_LOG_PATH = 'data/consciousness_logs'
    
    # 調試器配置
    DEBUGGER_PORT = 5001
    WEBSOCKET_PORT = 5002
    
    # 意識狀態閾值
    MIN_FREQUENCY = 0.1
    MAX_FREQUENCY = 100.0
    MIN_RESONANCE = 0.0
    MAX_RESONANCE = 1.0
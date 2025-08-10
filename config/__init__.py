import os
import sys

class Config:
    DATABASE_PATH = './data/database/shang.db'
    TELEGRAM_TOKEN = '8198655253:AAGINTuIOjw73ee2F3BkwS2Ipx3he-y21Pc'
    AUDIO_CONFIG = {
        'base_path': './data/audio',
        'supported_formats': ['m4a', 'mp3', 'wav'],
        'volume_levels': {
            'meditation': 0.8,
            'rhythm': 0.6
        }
    }

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

if __name__ == '__main__':
    print('Config module loaded')
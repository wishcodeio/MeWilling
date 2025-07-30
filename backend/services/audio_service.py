import os
import json
from typing import Dict, List, Optional
from config import Config

class AudioService:
    """音频服务类 - 管理修煉音頻播放"""
    
    def __init__(self):
        self.audio_config = Config.AUDIO_CONFIG
        self.audio_path = self.audio_config['base_path']
        self.supported_formats = self.audio_config['supported_formats']
        self.volume_levels = self.audio_config['volume_levels']
        self.audio_catalog = self._build_audio_catalog()


    
    def _build_audio_catalog(self) -> Dict:
        """構建音頻目錄"""
        catalog = {
            'divine_mantras': {
                'name': '八大神咒',
                'description': '傳統道家修煉神咒',
                'files': {
                    'badashengzhou': {
                        'name': '八大聖咒',
                        'file': 'badashengzhou.m4a',
                        'duration': '未知',
                        'description': '道家八大神咒完整版',
                        'usage': '深度冥想、靈性修煉',
                        'volume': self.volume_levels['meditation']
                    }
                }
            },
            'wooden_fish': {
                'name': '木魚節奏',
                'description': '不同BPM的木魚聲，適合不同修煉階段',
                'files': {
                    'muyu40': {
                        'name': '木魚 40 BPM',
                        'file': 'muyu40_bpm.m4a',
                        'bpm': 40,
                        'description': '極慢節奏，適合深度冥想',
                        'usage': '入定、深層放鬆',
                        'stage': '基礎桩功',
                        'volume': self.volume_levels['rhythm']
                    },
                    'muyu50': {
                        'name': '木魚 50 BPM',
                        'file': 'muyu50_bpm.m4a',
                        'bpm': 50,
                        'description': '慢節奏，適合靜心修煉',
                        'usage': '靜坐、調息',
                        'stage': '基礎桩功',
                        'volume': self.volume_levels['rhythm']
                    },
                    'muyu70': {
                        'name': '木魚 70 BPM',
                        'file': 'muyu70_bpm.m4a',
                        'bpm': 70,
                        'description': '中等節奏，適合日常修煉',
                        'usage': '日常冥想、呼吸調節',
                        'stage': '小周天運行',
                        'volume': self.volume_levels['rhythm']
                    },
                    'muyu100': {
                        'name': '木魚 100 BPM',
                        'file': 'muyu100_bpm.m4a',
                        'bpm': 100,
                        'description': '標準節奏，適合動態修煉',
                        'usage': '動功、太極',
                        'stage': '大周天運行',
                        'volume': self.volume_levels['rhythm']
                    },
                    'muyu120': {
                        'name': '木魚 120 BPM',
                        'file': 'muyu120_bpm.m4a',
                        'bpm': 120,
                        'description': '快節奏，適合活力修煉',
                        'usage': '武術、氣功',
                        'stage': '先天之境',
                        'volume': self.volume_levels['rhythm']
                    },
                    'muyu120b': {
                        'name': '木魚 120B BPM',
                        'file': 'muyu120b_bpm.m4a',
                        'bpm': 120,
                        'description': '快節奏變體，不同音色',
                        'usage': '高強度修煉',
                        'stage': '先天之境',
                        'volume': self.volume_levels['rhythm']
                    }
                }
            }
        }
        return catalog
    
    def get_audio_catalog(self) -> Dict:
        """獲取音頻目錄"""
        return self.audio_catalog
    
    def get_audio_by_category(self, category: str) -> Optional[Dict]:
        """根據類別獲取音頻"""
        return self.audio_catalog.get(category)
    
    def get_audio_info(self, audio_id: str) -> Optional[Dict]:
        """獲取特定音頻信息"""
        for category in self.audio_catalog.values():
            if audio_id in category['files']:
                audio_info = category['files'][audio_id].copy()
                audio_info['category'] = category['name']
                audio_info['full_path'] = os.path.join(self.audio_path, audio_info['file'])
                return audio_info
        return None
    
    def get_audio_url(self, audio_id: str) -> Optional[str]:
        """獲取音頻URL"""
        audio_info = self.get_audio_info(audio_id)
        if audio_info:
            return f"/static/audio/{audio_info['file']}"
        return None
    
    def validate_audio_file(self, audio_id: str) -> bool:
        """驗證音頻文件是否存在"""
        audio_info = self.get_audio_info(audio_id)
        if audio_info:
            return os.path.exists(audio_info['full_path'])
        return False
    
    def get_recommended_audio(self, shang_value: float) -> Dict:
        """根據商值推薦音頻"""
        if shang_value < 0.8:
            # 商值偏低，推薦提升能量的音頻
            return {
                'primary': 'muyu100',
                'secondary': 'badashengzhou',
                'reason': '商值偏低，建議使用中等節奏木魚提升基礎能量，配合神咒深化修煉'
            }
        elif shang_value > 1.5:
            # 商值過高，推薦平靜的音頻
            return {
                'primary': 'muyu40',
                'secondary': 'muyu50',
                'reason': '商值過高，建議使用慢節奏木魚平靜心神，避免過度消耗'
            }
        else:
            # 商值正常，推薦平衡的音頻
            return {
                'primary': 'muyu70',
                'secondary': 'muyu100',
                'reason': '商值平衡，建議使用標準節奏維持當前狀態'
            }
    
    def get_audio_by_mood(self, emotion: str) -> Dict:
        """根據情緒推薦音頻"""
        mood_mapping = {
            '焦慮': {'primary': 'muyu40', 'secondary': 'badashengzhou'},
            '憤怒': {'primary': 'muyu50', 'secondary': 'muyu40'},
            '悲傷': {'primary': 'badashengzhou', 'secondary': 'muyu70'},
            '平靜': {'primary': 'muyu70', 'secondary': 'muyu100'},
            '愉快': {'primary': 'muyu100', 'secondary': 'muyu120'},
            '興奮': {'primary': 'muyu120', 'secondary': 'muyu120b'}
        }
        
        return mood_mapping.get(emotion, {
            'primary': 'muyu70',
            'secondary': 'muyu100'
        })
    
    def get_practice_schedule(self) -> Dict:
        """獲取修煉時間表建議"""
        return {
            'morning': {
                'time': '06:00-08:00',
                'audio': 'muyu70',
                'duration': '30分鐘',
                'description': '晨練，調和陰陽'
            },
            'noon': {
                'time': '12:00-13:00',
                'audio': 'muyu50',
                'duration': '15分鐘',
                'description': '午休冥想，平靜心神'
            },
            'evening': {
                'time': '18:00-19:00',
                'audio': 'muyu100',
                'duration': '45分鐘',
                'description': '晚練，強化修煉'
            },
            'night': {
                'time': '21:00-22:00',
                'audio': 'badashengzhou',
                'duration': '20分鐘',
                'description': '夜修，深層淨化'
            }
        }
    
    def calculate_breathing_rhythm(self, bpm: int) -> Dict:
        """根據BPM計算呼吸節奏"""
        # 基於"一息六秒"的傳統計算
        breath_per_minute = bpm / 6  # 每分鐘呼吸次數
        seconds_per_breath = 60 / breath_per_minute  # 每次呼吸秒數
        
        return {
            'bpm': bpm,
            'breaths_per_minute': round(breath_per_minute, 1),
            'seconds_per_breath': round(seconds_per_breath, 1),
            'inhale_seconds': round(seconds_per_breath * 0.4, 1),
            'hold_seconds': round(seconds_per_breath * 0.2, 1),
            'exhale_seconds': round(seconds_per_breath * 0.4, 1)
        }
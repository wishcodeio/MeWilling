from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
import sqlite3
import hashlib
import json

@dataclass
class User:
    """用户数据模型"""
    user_id: str
    username: str
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    preferences: Optional[dict] = None
    is_active: bool = True
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'preferences': self.preferences,
            'is_active': self.is_active
        }

@dataclass
class UserPreferences:
    """用户偏好设置"""
    theme: str = 'light'  # light, dark
    language: str = 'zh'  # zh, en
    audio_volume: float = 0.7
    auto_play: bool = False
    notification_enabled: bool = True
    default_emotion: str = 'neutral'
    
    def to_dict(self):
        return {
            'theme': self.theme,
            'language': self.language,
            'audio_volume': self.audio_volume,
            'auto_play': self.auto_play,
            'notification_enabled': self.notification_enabled,
            'default_emotion': self.default_emotion
        }

class UserDatabase:
    """用户数据库操作类"""
    
    def __init__(self, db_path: str = 'data/database/shang.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """初始化用户数据库表"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT,
                password_hash TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP,
                preferences TEXT,
                is_active BOOLEAN DEFAULT 1
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_user(self, username: str, password: str, email: str = None) -> User:
        """创建新用户"""
        user_id = hashlib.md5(f"{username}{datetime.now()}".encode()).hexdigest()[:12]
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        default_preferences = UserPreferences().to_dict()
        
        cursor.execute('''
            INSERT INTO users (user_id, username, email, password_hash, preferences)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, username, email, password_hash, json.dumps(default_preferences)))
        
        conn.commit()
        conn.close()
        
        return User(
            user_id=user_id,
            username=username,
            email=email,
            created_at=datetime.now(),
            preferences=default_preferences
        )
    
    def get_user(self, user_id: str) -> Optional[User]:
        """根据用户ID获取用户"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT user_id, username, email, created_at, last_login, preferences, is_active
            FROM users WHERE user_id = ?
        ''', (user_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return User(
                user_id=row[0],
                username=row[1],
                email=row[2],
                created_at=datetime.fromisoformat(row[3]) if row[3] else None,
                last_login=datetime.fromisoformat(row[4]) if row[4] else None,
                preferences=json.loads(row[5]) if row[5] else {},
                is_active=bool(row[6])
            )
        return None
    
    def update_preferences(self, user_id: str, preferences: dict) -> bool:
        """更新用户偏好设置"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE users SET preferences = ? WHERE user_id = ?
        ''', (json.dumps(preferences), user_id))
        
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        
        return success
    
    def update_last_login(self, user_id: str) -> bool:
        """更新最后登录时间"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE user_id = ?
        ''', (user_id,))
        
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        
        return success
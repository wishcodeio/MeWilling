from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Dict, Any
import sqlite3
import json

@dataclass
class ShangRecord:
    """
    商增記錄數據模型
    
    用於存儲用戶的日常生活數據和系統計算的商增值結果。
    商增值 = 分子（目標完成情況）÷ 分母（基礎能力值）
    
    Attributes:
        id: 記錄的唯一標識符，由數據庫自動生成
        date: 記錄日期，格式為 YYYY-MM-DD
        
        # 生理指標 (影響分子和分母計算)
        heart_rate: 心率，單位BPM，正常範圍40-200，理想範圍60-80
        steps: 當日步數，≥0，目標值10000步
        sleep_quality: 睡眠質量主觀評分，1-10分，影響基礎能力
        
        # 心理指標
        emotion_log: 情緒狀態，枚舉值：愉快/平靜/焦慮/憤怒/悲傷/興奮
        stress_level: 壓力水平，0-100，數值越高壓力越大
        
        # 修煉指標
        meditation_notes: 冥想心得，自由文本，用於關鍵詞分析
        gratitude_items: 感恩事項，自由文本，提升整體心理狀態
        
        # 計算結果 (系統自動計算)
        numerator: 分子值，基於外在表現計算的目標完成度
        denominator: 分母值，基於內在狀態計算的基礎能力值
        shang_value: 商增值，numerator ÷ denominator
        suggestion: 個性化建議，基於商增值範圍生成
    """
    id: Optional[int] = None
    date: str = None
    
    # 生理指標
    heart_rate: int = 70          # 心率 (BPM)，理想範圍 60-80
    steps: int = 0                # 步數，目標 10000
    sleep_quality: int = 7        # 睡眠質量 (1-10)，影響基礎能力
    
    # 心理指標
    emotion_log: str = "平靜"      # 情緒狀態，影響效率乘數
    stress_level: int = 30        # 壓力水平 (0-100)，越低越好
    
    # 修煉指標
    meditation_notes: str = ""    # 冥想心得，關鍵詞分析
    gratitude_items: str = ""     # 感恩事項，心理狀態提升
    
    # 計算結果 (系統自動生成)
    numerator: float = 0.0        # 分子：目標完成情況
    denominator: float = 0.0      # 分母：基礎能力值
    shang_value: float = 0.0      # 商增值：numerator ÷ denominator
    suggestion: str = ""          # 個性化建議
    
    # 時間戳
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """轉換為字典格式"""
        return {
            'id': self.id,
            'date': self.date,
            'heart_rate': self.heart_rate,
            'steps': self.steps,
            'sleep_quality': self.sleep_quality,
            'emotion_log': self.emotion_log,
            'stress_level': self.stress_level,
            'meditation_notes': self.meditation_notes,
            'gratitude_items': self.gratitude_items,
            'numerator': self.numerator,
            'denominator': self.denominator,
            'shang_value': self.shang_value,
            'suggestion': self.suggestion,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ShangRecord':
        """從字典創建實例"""
        record = cls()
        for key, value in data.items():
            if hasattr(record, key):
                if key in ['created_at', 'updated_at'] and value:
                    setattr(record, key, datetime.fromisoformat(value))
                else:
                    setattr(record, key, value)
        return record

class ShangDatabase:
    """商增數據庫操作類"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """初始化數據庫表"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS shang_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT UNIQUE NOT NULL,
                    heart_rate INTEGER DEFAULT 70,
                    steps INTEGER DEFAULT 0,
                    sleep_quality INTEGER DEFAULT 7,
                    emotion_log TEXT DEFAULT '平靜',
                    stress_level INTEGER DEFAULT 30,
                    meditation_notes TEXT DEFAULT '',
                    gratitude_items TEXT DEFAULT '',
                    numerator REAL DEFAULT 0.0,
                    denominator REAL DEFAULT 0.0,
                    shang_value REAL DEFAULT 0.0,
                    suggestion TEXT DEFAULT '',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    def save_record(self, record: ShangRecord) -> int:
        """保存記錄"""
        with sqlite3.connect(self.db_path) as conn:
            if record.id:
                # 更新現有記錄
                conn.execute('''
                    UPDATE shang_records SET
                        heart_rate=?, steps=?, sleep_quality=?, emotion_log=?,
                        stress_level=?, meditation_notes=?, gratitude_items=?,
                        numerator=?, denominator=?, shang_value=?, suggestion=?,
                        updated_at=CURRENT_TIMESTAMP
                    WHERE id=?
                ''', (
                    record.heart_rate, record.steps, record.sleep_quality, record.emotion_log,
                    record.stress_level, record.meditation_notes, record.gratitude_items,
                    record.numerator, record.denominator, record.shang_value, record.suggestion,
                    record.id
                ))
                return record.id
            else:
                # 插入新記錄
                cursor = conn.execute('''
                    INSERT OR REPLACE INTO shang_records (
                        date, heart_rate, steps, sleep_quality, emotion_log,
                        stress_level, meditation_notes, gratitude_items,
                        numerator, denominator, shang_value, suggestion
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    record.date, record.heart_rate, record.steps, record.sleep_quality,
                    record.emotion_log, record.stress_level, record.meditation_notes,
                    record.gratitude_items, record.numerator, record.denominator,
                    record.shang_value, record.suggestion
                ))
                return cursor.lastrowid
    
    def get_record_by_date(self, date: str) -> Optional[ShangRecord]:
        """根據日期獲取記錄"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute('SELECT * FROM shang_records WHERE date = ?', (date,))
            row = cursor.fetchone()
            if row:
                return ShangRecord.from_dict(dict(row))
        return None
    
    def get_recent_records(self, limit: int = 30) -> list[ShangRecord]:
        """獲取最近的記錄"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                'SELECT * FROM shang_records ORDER BY date DESC LIMIT ?', 
                (limit,)
            )
            return [ShangRecord.from_dict(dict(row)) for row in cursor.fetchall()]
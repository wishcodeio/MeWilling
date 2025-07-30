import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import json
import csv
from backend.models.shang_model import ShangRecord, Emotion

class DataProcessor:
    """数据处理工具类"""
    
    @staticmethod
    def export_to_csv(records: List[ShangRecord], filename: str) -> str:
        """导出数据到CSV文件"""
        if not records:
            raise ValueError("没有数据可导出")
        
        # 准备数据
        data = []
        for record in records:
            data.append({
                '日期': record.date,
                '尚值': record.shang_value,
                '情绪': record.emotion.value if record.emotion else 'neutral',
                '睡眠质量': record.sleep_quality,
                '精力水平': record.energy_level,
                '压力水平': record.stress_level,
                '专注水平': record.focus_level,
                '社交互动': record.social_interaction,
                '身体活动': record.physical_activity,
                '冥想时间': record.meditation_time,
                '学习时间': record.learning_time,
                '创作时间': record.creative_time
            })
        
        # 写入CSV
        df = pd.DataFrame(data)
        filepath = f"data/exports/{filename}"
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
        
        return filepath
    
    @staticmethod
    def export_to_json(records: List[ShangRecord], filename: str) -> str:
        """导出数据到JSON文件"""
        if not records:
            raise ValueError("没有数据可导出")
        
        # 准备数据
        data = {
            'export_time': datetime.now().isoformat(),
            'total_records': len(records),
            'records': []
        }
        
        for record in records:
            data['records'].append({
                'date': record.date.isoformat(),
                'shang_value': record.shang_value,
                'emotion': record.emotion.value if record.emotion else 'neutral',
                'metrics': {
                    'sleep_quality': record.sleep_quality,
                    'energy_level': record.energy_level,
                    'stress_level': record.stress_level,
                    'focus_level': record.focus_level,
                    'social_interaction': record.social_interaction,
                    'physical_activity': record.physical_activity,
                    'meditation_time': record.meditation_time,
                    'learning_time': record.learning_time,
                    'creative_time': record.creative_time
                }
            })
        
        # 写入JSON
        filepath = f"data/exports/{filename}"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return filepath
    
    @staticmethod
    def import_from_csv(filepath: str) -> List[ShangRecord]:
        """从CSV文件导入数据"""
        records = []
        
        try:
            df = pd.read_csv(filepath, encoding='utf-8-sig')
            
            for _, row in df.iterrows():
                # 处理日期
                date = pd.to_datetime(row['日期']).date()
                
                # 处理情绪
                emotion_str = row.get('情绪', 'neutral')
                try:
                    emotion = Emotion(emotion_str)
                except ValueError:
                    emotion = Emotion.NEUTRAL
                
                # 创建记录
                record = ShangRecord(
                    date=date,
                    shang_value=float(row.get('尚值', 0)),
                    emotion=emotion,
                    sleep_quality=int(row.get('睡眠质量', 5)),
                    energy_level=int(row.get('精力水平', 5)),
                    stress_level=int(row.get('压力水平', 5)),
                    focus_level=int(row.get('专注水平', 5)),
                    social_interaction=int(row.get('社交互动', 5)),
                    physical_activity=int(row.get('身体活动', 30)),
                    meditation_time=int(row.get('冥想时间', 0)),
                    learning_time=int(row.get('学习时间', 0)),
                    creative_time=int(row.get('创作时间', 0))
                )
                
                records.append(record)
        
        except Exception as e:
            raise ValueError(f"导入CSV文件失败: {str(e)}")
        
        return records
    
    @staticmethod
    def clean_data(records: List[ShangRecord]) -> List[ShangRecord]:
        """清理数据，移除异常值和重复项"""
        if not records:
            return records
        
        # 按日期排序
        records.sort(key=lambda x: x.date)
        
        # 移除重复日期的记录（保留最新的）
        unique_records = {}
        for record in records:
            unique_records[record.date] = record
        
        cleaned_records = list(unique_records.values())
        
        # 清理异常值
        for record in cleaned_records:
            # 确保数值在合理范围内
            record.sleep_quality = max(1, min(10, record.sleep_quality))
            record.energy_level = max(1, min(10, record.energy_level))
            record.stress_level = max(1, min(10, record.stress_level))
            record.focus_level = max(1, min(10, record.focus_level))
            record.social_interaction = max(1, min(10, record.social_interaction))
            record.physical_activity = max(0, min(300, record.physical_activity))
            record.meditation_time = max(0, min(300, record.meditation_time))
            record.learning_time = max(0, min(600, record.learning_time))
            record.creative_time = max(0, min(600, record.creative_time))
        
        return cleaned_records
    
    @staticmethod
    def fill_missing_dates(records: List[ShangRecord], 
                          start_date: datetime.date, 
                          end_date: datetime.date) -> List[ShangRecord]:
        """填充缺失日期的记录"""
        if not records:
            return records
        
        # 创建日期到记录的映射
        record_map = {record.date: record for record in records}
        
        filled_records = []
        current_date = start_date
        
        while current_date <= end_date:
            if current_date in record_map:
                filled_records.append(record_map[current_date])
            else:
                # 创建默认记录
                default_record = ShangRecord(
                    date=current_date,
                    shang_value=0.0,
                    emotion=Emotion.NEUTRAL,
                    sleep_quality=5,
                    energy_level=5,
                    stress_level=5,
                    focus_level=5,
                    social_interaction=5,
                    physical_activity=30,
                    meditation_time=0,
                    learning_time=0,
                    creative_time=0
                )
                filled_records.append(default_record)
            
            current_date += timedelta(days=1)
        
        return filled_records
    
    @staticmethod
    def calculate_statistics(records: List[ShangRecord]) -> Dict[str, Any]:
        """计算统计信息"""
        if not records:
            return {}
        
        # 提取数值数据
        shang_values = [r.shang_value for r in records]
        sleep_quality = [r.sleep_quality for r in records]
        energy_level = [r.energy_level for r in records]
        stress_level = [r.stress_level for r in records]
        
        stats = {
            'total_records': len(records),
            'date_range': {
                'start': min(r.date for r in records).isoformat(),
                'end': max(r.date for r in records).isoformat()
            },
            'shang_value': {
                'mean': np.mean(shang_values),
                'median': np.median(shang_values),
                'std': np.std(shang_values),
                'min': np.min(shang_values),
                'max': np.max(shang_values)
            },
            'sleep_quality': {
                'mean': np.mean(sleep_quality),
                'median': np.median(sleep_quality)
            },
            'energy_level': {
                'mean': np.mean(energy_level),
                'median': np.median(energy_level)
            },
            'stress_level': {
                'mean': np.mean(stress_level),
                'median': np.median(stress_level)
            }
        }
        
        # 情绪分布
        emotion_counts = {}
        for record in records:
            emotion = record.emotion.value if record.emotion else 'neutral'
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        stats['emotion_distribution'] = emotion_counts
        
        return stats
    
    @staticmethod
    def generate_backup(records: List[ShangRecord], backup_name: str = None) -> str:
        """生成数据备份"""
        if backup_name is None:
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        backup_data = {
            'backup_time': datetime.now().isoformat(),
            'version': '1.0',
            'total_records': len(records),
            'records': []
        }
        
        for record in records:
            backup_data['records'].append({
                'date': record.date.isoformat(),
                'shang_value': record.shang_value,
                'emotion': record.emotion.value if record.emotion else 'neutral',
                'sleep_quality': record.sleep_quality,
                'energy_level': record.energy_level,
                'stress_level': record.stress_level,
                'focus_level': record.focus_level,
                'social_interaction': record.social_interaction,
                'physical_activity': record.physical_activity,
                'meditation_time': record.meditation_time,
                'learning_time': record.learning_time,
                'creative_time': record.creative_time
            })
        
        filepath = f"data/backups/{backup_name}"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, ensure_ascii=False, indent=2)
        
        return filepath
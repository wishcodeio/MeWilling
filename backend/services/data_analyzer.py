import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from backend.models.shang_model import ShangRecord, ShangDatabase
import statistics

class DataAnalyzer:
    """数据分析服务类"""
    
    def __init__(self, db_path: str = 'data/database/shang.db'):
        self.db = ShangDatabase(db_path)
    
    def get_trend_analysis(self, days: int = 30) -> Dict:
        """获取趋势分析"""
        records = self.db.get_recent_records(days)
        if not records:
            return {'error': '没有足够的数据进行分析'}
        
        # 转换为DataFrame便于分析
        df = self._records_to_dataframe(records)
        
        analysis = {
            'period': f'最近{days}天',
            'total_records': len(records),
            'shang_trend': self._analyze_shang_trend(df),
            'emotion_distribution': self._analyze_emotion_distribution(df),
            'correlation_analysis': self._analyze_correlations(df),
            'recommendations': self._generate_recommendations(df)
        }
        
        return analysis
    
    def _records_to_dataframe(self, records: List[ShangRecord]) -> pd.DataFrame:
        """将记录转换为DataFrame"""
        data = []
        for record in records:
            data.append({
                'date': record.date,
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
        
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        return df.sort_values('date')
    
    def _analyze_shang_trend(self, df: pd.DataFrame) -> Dict:
        """分析尚值趋势"""
        if len(df) < 2:
            return {'trend': 'insufficient_data'}
        
        # 计算趋势
        recent_avg = df.tail(7)['shang_value'].mean()
        previous_avg = df.head(7)['shang_value'].mean() if len(df) >= 14 else df['shang_value'].mean()
        
        trend_direction = 'stable'
        if recent_avg > previous_avg * 1.05:
            trend_direction = 'improving'
        elif recent_avg < previous_avg * 0.95:
            trend_direction = 'declining'
        
        # 计算变化率
        change_rate = ((recent_avg - previous_avg) / previous_avg * 100) if previous_avg != 0 else 0
        
        # 计算波动性
        volatility = df['shang_value'].std()
        
        return {
            'direction': trend_direction,
            'change_rate': round(change_rate, 2),
            'current_avg': round(recent_avg, 3),
            'volatility': round(volatility, 3),
            'max_value': df['shang_value'].max(),
            'min_value': df['shang_value'].min()
        }
    
    def _analyze_emotion_distribution(self, df: pd.DataFrame) -> Dict:
        """分析情绪分布"""
        emotion_counts = df['emotion'].value_counts()
        total = len(df)
        
        distribution = {}
        for emotion, count in emotion_counts.items():
            distribution[emotion] = {
                'count': int(count),
                'percentage': round(count / total * 100, 1)
            }
        
        # 找出主导情绪
        dominant_emotion = emotion_counts.index[0] if not emotion_counts.empty else 'neutral'
        
        return {
            'distribution': distribution,
            'dominant_emotion': dominant_emotion,
            'emotion_variety': len(emotion_counts)
        }
    
    def _analyze_correlations(self, df: pd.DataFrame) -> Dict:
        """分析各指标与尚值的相关性"""
        numeric_columns = [
            'sleep_quality', 'energy_level', 'stress_level', 'focus_level',
            'social_interaction', 'physical_activity', 'meditation_time',
            'learning_time', 'creative_time'
        ]
        
        correlations = {}
        for col in numeric_columns:
            if col in df.columns:
                corr = df['shang_value'].corr(df[col])
                if not np.isnan(corr):
                    correlations[col] = round(corr, 3)
        
        # 找出最强相关性
        if correlations:
            strongest_positive = max(correlations.items(), key=lambda x: x[1] if x[1] > 0 else -1)
            strongest_negative = min(correlations.items(), key=lambda x: x[1] if x[1] < 0 else 1)
        else:
            strongest_positive = strongest_negative = None
        
        return {
            'correlations': correlations,
            'strongest_positive': strongest_positive,
            'strongest_negative': strongest_negative
        }
    
    def _generate_recommendations(self, df: pd.DataFrame) -> List[str]:
        """生成改进建议"""
        recommendations = []
        
        # 基于尚值趋势的建议
        recent_avg = df.tail(7)['shang_value'].mean()
        if recent_avg < 0.5:
            recommendations.append("尚值偏低，建议增加冥想时间和身体活动")
        
        # 基于睡眠质量的建议
        avg_sleep = df['sleep_quality'].mean()
        if avg_sleep < 6:
            recommendations.append("睡眠质量需要改善，建议建立规律的作息时间")
        
        # 基于压力水平的建议
        avg_stress = df['stress_level'].mean()
        if avg_stress > 7:
            recommendations.append("压力水平较高，建议增加放松活动和冥想练习")
        
        # 基于学习时间的建议
        avg_learning = df['learning_time'].mean()
        if avg_learning < 30:
            recommendations.append("学习时间较少，建议每天至少安排30分钟学习")
        
        # 基于情绪分布的建议
        negative_emotions = ['angry', 'sad', 'anxious']
        negative_ratio = len(df[df['emotion'].isin(negative_emotions)]) / len(df)
        if negative_ratio > 0.3:
            recommendations.append("负面情绪较多，建议寻求专业帮助或增加积极活动")
        
        return recommendations[:5]  # 最多返回5条建议
    
    def get_weekly_summary(self) -> Dict:
        """获取周度总结"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=7)
        
        records = []
        for i in range(7):
            date = start_date + timedelta(days=i)
            record = self.db.get_record_by_date(date)
            if record:
                records.append(record)
        
        if not records:
            return {'error': '本周没有数据记录'}
        
        df = self._records_to_dataframe(records)
        
        summary = {
            'week_period': f"{start_date} 至 {end_date}",
            'days_recorded': len(records),
            'avg_shang_value': round(df['shang_value'].mean(), 3),
            'best_day': {
                'date': df.loc[df['shang_value'].idxmax(), 'date'].strftime('%Y-%m-%d'),
                'shang_value': df['shang_value'].max()
            },
            'worst_day': {
                'date': df.loc[df['shang_value'].idxmin(), 'date'].strftime('%Y-%m-%d'),
                'shang_value': df['shang_value'].min()
            },
            'improvement_areas': self._identify_improvement_areas(df)
        }
        
        return summary
    
    def _identify_improvement_areas(self, df: pd.DataFrame) -> List[str]:
        """识别需要改进的领域"""
        areas = []
        
        metrics = {
            'sleep_quality': ('睡眠质量', 7),
            'energy_level': ('精力水平', 7),
            'focus_level': ('专注水平', 7),
            'physical_activity': ('身体活动', 60),
            'meditation_time': ('冥想时间', 20)
        }
        
        for metric, (name, threshold) in metrics.items():
            if metric in df.columns:
                avg_value = df[metric].mean()
                if avg_value < threshold:
                    areas.append(f"{name}平均值{avg_value:.1f}，建议提升至{threshold}以上")
        
        return areas[:3]  # 最多返回3个改进领域
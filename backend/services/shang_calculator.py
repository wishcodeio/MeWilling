from typing import Dict, Tuple
from backend.models.shang_model import ShangRecord
import config

class ShangCalculator:
    """商增計算服務類"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {
            'default_weights': {
                'steps': 0.4,
                'heart_rate': 0.3,
                'sleep_quality': 0.2,
                'stress_level': 0.1,
                'meditation': 0.3
            },
            'high_efficiency_threshold': 1.5,
            'low_efficiency_threshold': 0.7
        }
        self.weights = self.config['default_weights']
    
    def calculate_numerator(self, record: ShangRecord) -> float:
        """計算分子（目標完成情況）"""
        # 基於步數、心率等外在表現計算目標完成度
        step_score = min(record.steps / 10000, 1.0) * 100  # 步數得分，最高100
        heart_rate_score = self._normalize_heart_rate(record.heart_rate)
        
        # 情緒狀態影響目標完成度
        emotion_multiplier = self._get_emotion_multiplier(record.emotion_log)
        
        numerator = (
            step_score * self.weights['steps'] +
            heart_rate_score * self.weights['heart_rate']
        ) * emotion_multiplier
        
        return round(numerator, 2)
    
    def calculate_denominator(self, record: ShangRecord) -> float:
        """計算分母（基礎能力值）"""
        # 基於睡眠質量、壓力水平、冥想狀態計算基礎能力
        sleep_score = record.sleep_quality * 10  # 睡眠質量得分
        stress_score = max(0, 100 - record.stress_level)  # 壓力越低得分越高
        meditation_score = self._get_meditation_score(record.meditation_notes)
        
        denominator = (
            sleep_score * self.weights['sleep_quality'] +
            stress_score * self.weights['stress_level'] +
            meditation_score * self.weights['meditation']
        )
        
        return max(round(denominator, 2), 0.1)  # 避免分母為0
    
    def calculate_shang(self, record: ShangRecord) -> Tuple[float, str]:
        """計算商值並生成建議"""
        numerator = self.calculate_numerator(record)
        denominator = self.calculate_denominator(record)
        
        # 更新記錄中的分子分母
        record.numerator = numerator
        record.denominator = denominator
        
        # 計算商值
        shang_value = numerator / denominator
        record.shang_value = round(shang_value, 4)
        
        # 生成建議
        suggestion = self._generate_suggestion(shang_value)
        record.suggestion = suggestion
        
        return shang_value, suggestion
    
    def _normalize_heart_rate(self, heart_rate: int) -> float:
        """標準化心率數據"""
        # 假設理想心率範圍是60-80，超出範圍得分降低
        if 60 <= heart_rate <= 80:
            return 100
        elif heart_rate < 60:
            return max(50, 100 - (60 - heart_rate) * 2)
        else:
            return max(50, 100 - (heart_rate - 80) * 1.5)
    
    def _get_emotion_multiplier(self, emotion: str) -> float:
        """根據情緒狀態獲取乘數"""
        emotion_map = {
            '愉快': 1.2,
            '平靜': 1.0,
            '焦慮': 0.8,
            '憤怒': 0.7,
            '悲傷': 0.6,
            '興奮': 1.1
        }
        return emotion_map.get(emotion, 1.0)
    
    def _get_meditation_score(self, notes: str) -> float:
        """根據冥想心得計算得分"""
        if not notes:
            return 50
        
        # 簡單的關鍵詞分析
        positive_keywords = ['平靜', '放鬆', '清晰', '專注', '寧靜', '和諧']
        negative_keywords = ['焦慮', '分心', '煩躁', '困難', '疲憊']
        
        positive_count = sum(1 for keyword in positive_keywords if keyword in notes)
        negative_count = sum(1 for keyword in negative_keywords if keyword in notes)
        
        base_score = 70
        score = base_score + positive_count * 10 - negative_count * 5
        
        return max(30, min(100, score))
    
    def _generate_suggestion(self, shang_value: float) -> str:
        """根據商值生成建議"""
        high_threshold = self.config['high_efficiency_threshold']
        low_threshold = self.config['low_efficiency_threshold']
        
        if shang_value > high_threshold:
            return "分子過高，可能會導致內耗，建議減少目標或強化基礎。"
        elif shang_value < low_threshold:
            return "效率偏低，分母基礎較強，建議增加目標挑戰性。"
        else:
            return "狀態良好，保持內外平衡！"
    
    def analyze_trend(self, records: list[ShangRecord]) -> Dict:
        """分析商值趨勢"""
        if not records:
            return {'trend': 'no_data', 'average': 0, 'suggestion': '暫無數據'}
        
        shang_values = [r.shang_value for r in records]
        average = sum(shang_values) / len(shang_values)
        
        # 計算趨勢
        if len(shang_values) >= 3:
            recent_avg = sum(shang_values[:3]) / 3
            older_avg = sum(shang_values[3:6]) / min(3, len(shang_values[3:]))
            
            if recent_avg > older_avg * 1.1:
                trend = 'improving'
            elif recent_avg < older_avg * 0.9:
                trend = 'declining'
            else:
                trend = 'stable'
        else:
            trend = 'insufficient_data'
        
        return {
            'trend': trend,
            'average': round(average, 4),
            'recent_values': shang_values[:7],  # 最近7天
            'suggestion': self._get_trend_suggestion(trend, average)
        }
    
    def _get_trend_suggestion(self, trend: str, average: float) -> str:
        """根據趨勢生成建議"""
        if trend == 'improving':
            return "商值呈上升趨勢，繼續保持當前的修煉方式。"
        elif trend == 'declining':
            return "商值有下降趨勢，建議調整作息或增加冥想時間。"
        elif trend == 'stable':
            if average > 1.2:
                return "商值穩定但偏高，注意避免過度追求外在目標。"
            elif average < 0.8:
                return "商值穩定但偏低，可以適當增加挑戰性目標。"
            else:
                return "商值穩定且平衡，繼續保持。"
        else:
            return "數據不足，建議持續記錄以獲得更準確的分析。"
    
    # 在現有的Shang計算器中融入願語言
    class WishEnhancedShangCalculator:
        def calculate_wish_shang(self, user_data, user_wish):
            # 計算願望導向的Shang值
            base_shang = self.calculate_traditional_shang(user_data)
            wish_alignment = self.measure_wish_universe_alignment(user_wish)
            love_factor = self.calculate_love_quotient(user_data)
            
            # 願語言公式：Shang = (內在修養 × 願望對齊度 × 愛的係數) / 外在表現
            wish_shang = (base_shang * wish_alignment * love_factor) / self.get_external_manifestation()
            return self.infuse_cosmic_wisdom(wish_shang)



# 原始的商增定律：技術實現
class OriginalShangLaw:
    def calculate_shang_value(self, numerator, denominator):
        # 基礎的商增計算
        return numerator / denominator if denominator != 0 else float('inf')
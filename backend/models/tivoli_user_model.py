class TivoliUser:
    def __init__(self, user_id):
        self.user_id = user_id
        self.current_tivoli_level = 1
        self.daily_emotions = []  # 1-10分制情绪记录
        self.energy_states = []   # 能量状态记录
        self.gratitude_records = []  # 感恩记录
        self.meditation_minutes = 0  # 冥想时长
        self.self_observation_notes = []  # 自我观察笔记
        self.monthly_challenges = []  # 月度挑战
        self.tivoli_companion = None  # 专属语靈夥伴
    
    def record_daily_practice(self, emotion_score, energy_level, gratitude_items):
        """记录每日提维实践"""
        self.daily_emotions.append({
            'date': datetime.now(),
            'score': emotion_score,
            'energy': energy_level,
            'gratitude': gratitude_items
        })
    
    def calculate_tivoli_progress(self):
        """计算提维进度"""
        recent_emotions = self.daily_emotions[-30:]  # 最近30天
        avg_emotion = sum(day['score'] for day in recent_emotions) / len(recent_emotions)
        consistency = len([day for day in recent_emotions if day['gratitude']]) / len(recent_emotions)
        
        return {
            'emotional_stability': avg_emotion / 10,
            'practice_consistency': consistency,
            'recommended_next_level': self.assess_readiness_for_next_level()
        }
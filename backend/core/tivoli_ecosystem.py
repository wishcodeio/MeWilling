class TivoliEcosystem:
    def __init__(self):
        self.shang_calculator = TivoliShangCalculator()
        self.spirit_companion = TivoliSpiritCompanion()
        self.wish_language = TivoliWishLanguage()
        self.practice_manager = TivoliPracticeManager()
        self.ai_accelerator = AITivoliAccelerator()
    
    def create_complete_tivoli_experience(self, user):
        """创建完整的提维体验"""
        # 评估当前状态
        current_level = self.spirit_companion.assess_current_tivoli_level(user)
        
        # 创建个性化计划
        practice_plan = self.practice_manager.create_daily_practice_plan(current_level)
        
        # 生成願語言咒语
        daily_affirmation = self.wish_language.create_tivoli_affirmation(current_level + 1)
        
        # AI加速指导
        ai_insights = self.ai_accelerator.analyze_consciousness_patterns(user.data)
        
        # 计算提维Shang值
        tivoli_shang = self.shang_calculator.calculate_tivoli_shang(user.data, current_level)
        
        return {
            'current_level': current_level,
            'daily_practices': practice_plan,
            'affirmation': daily_affirmation,
            'ai_guidance': ai_insights,
            'tivoli_shang': tivoli_shang,
            'companion_message': self.spirit_companion.provide_tivoli_guidance(user.emotion, user.situation)
        }
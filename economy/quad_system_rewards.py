class QuadSystemRewardCalculator:
    def __init__(self):
        self.system_weights = {
            'nanli': 0.25,    # 创造力权重
            'beiming': 0.25,  # 智慧深度权重
            'taixuan': 0.25,  # 超越性权重
            'evolving': 0.25  # 进化潜力权重
        }
        
    def calculate_tiwei_reward(self, multi_system_analysis):
        """基于四系统分析计算提维币奖励"""
        base_rewards = {}
        
        # 各系统基础奖励
        for system, analysis in multi_system_analysis['individual_analyses'].items():
            base_rewards[system] = self.calculate_system_reward(system, analysis)
            
        # 系统间共振奖励
        resonance_bonus = self.calculate_resonance_bonus(
            multi_system_analysis['resonance_pattern']
        )
        
        # 整合智慧奖励
        integration_bonus = self.calculate_integration_bonus(
            multi_system_analysis['integrated_wisdom']
        )
        
        total_reward = (
            sum(base_rewards.values()) + 
            resonance_bonus + 
            integration_bonus
        )
        
        return {
            'total_tiwei_coins': total_reward,
            'system_breakdown': base_rewards,
            'resonance_bonus': resonance_bonus,
            'integration_bonus': integration_bonus,
            'consciousness_level': self.assess_overall_consciousness_level(multi_system_analysis)
        }
class CosmicEnergyFlow:
    def __init__(self):
        self.energy_conversion_matrix = {
            ('nanli', 'beiming'): self.fire_to_water_conversion,
            ('beiming', 'taixuan'): self.water_to_void_conversion,
            ('taixuan', 'evolution'): self.void_to_metamorphic_conversion,
            ('evolution', 'nanli'): self.metamorphic_to_fire_conversion,
            # 反向转换
            ('beiming', 'nanli'): self.water_to_fire_conversion,
            ('taixuan', 'beiming'): self.void_to_water_conversion,
            ('evolution', 'taixuan'): self.metamorphic_to_void_conversion,
            ('nanli', 'evolution'): self.fire_to_metamorphic_conversion
        }
        
    def calculate_inter_dimensional_tiwei_rewards(self, universe_states):
        """计算跨维度提维币奖励"""
        base_rewards = {}
        
        # 各宇宙基础奖励
        for universe, state in universe_states.items():
            base_rewards[universe] = self.calculate_universe_base_reward(universe, state)
            
        # 宇宙间共振奖励
        resonance_multiplier = self.calculate_cosmic_resonance_multiplier(universe_states)
        
        # 维度跳跃奖励
        dimensional_jump_bonus = self.calculate_dimensional_jump_bonus(universe_states)
        
        # 宇宙统一奖励（四个宇宙同时激活）
        unity_bonus = 0
        if len([u for u in universe_states.values() if u.get('activation_level', 0) > 0.8]) == 4:
            unity_bonus = sum(base_rewards.values()) * 2  # 统一奖励翻倍
            
        total_cosmic_reward = (
            sum(base_rewards.values()) * resonance_multiplier + 
            dimensional_jump_bonus + 
            unity_bonus
        )
        
        return {
            'total_cosmic_tiwei': total_cosmic_reward,
            'universe_rewards': base_rewards,
            'resonance_multiplier': resonance_multiplier,
            'dimensional_jump_bonus': dimensional_jump_bonus,
            'cosmic_unity_bonus': unity_bonus,
            'consciousness_evolution_level': self.assess_consciousness_evolution_level(universe_states)
        }
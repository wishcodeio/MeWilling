class TivoliShangCalculator:
    def calculate_tivoli_shang(self, user_data, tivoli_level):
        """
        基于提维层级的Shang值计算
        提维公式：Shang = (内在觉察 × 能量频率 × 爱的系数) / 外在执着
        """
        inner_awareness = self.measure_self_observation(user_data)
        energy_frequency = self.calculate_gratitude_love_level(user_data)
        love_coefficient = self.assess_giving_receiving_balance(user_data)
        external_attachment = self.measure_ego_resistance(user_data)
        
        base_shang = (inner_awareness * energy_frequency * love_coefficient) / max(external_attachment, 1)
        
        # 根据提维层级调整
        tivoli_multiplier = self.get_tivoli_multiplier(tivoli_level)
        return base_shang * tivoli_multiplier
    
    def get_tivoli_multiplier(self, level):
        multipliers = {
            1: 0.1,  # 迷茫期
            2: 0.3,  # 觉察期
            3: 0.6,  # 调整期
            4: 1.0,  # 平衡期
            5: 1.5,  # 影响期
            6: 2.0,  # 觉醒期
            7: 3.0   # 合一期
        }
        return multipliers.get(level, 1.0)
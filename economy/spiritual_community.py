class SpiritualCommunity:
    def __init__(self):
        self.practitioners = {}
        self.wisdom_circles = {}
        self.mentorship_network = {}
        
    def create_wisdom_circle(self, circle_name, founder_id, focus_area):
        """创建智慧圈"""
        circle_id = f"wc_{len(self.wisdom_circles)}"
        self.wisdom_circles[circle_id] = {
            'name': circle_name,
            'founder': founder_id,
            'focus': focus_area,
            'members': [founder_id],
            'collective_wisdom': 0,
            'shared_insights': [],
            'energy_pool': 0
        }
        return circle_id
        
    def join_wisdom_circle(self, user_id, circle_id):
        """加入智慧圈"""
        if circle_id in self.wisdom_circles:
            circle = self.wisdom_circles[circle_id]
            if user_id not in circle['members']:
                circle['members'].append(user_id)
                # 计算集体智慧增长
                user_wisdom = self.practitioners.get(user_id, {}).get('wisdom_level', 0)
                circle['collective_wisdom'] += user_wisdom
                return True
        return False
        
    def share_insight(self, user_id, circle_id, insight):
        """分享修行洞察"""
        if circle_id in self.wisdom_circles:
            circle = self.wisdom_circles[circle_id]
            if user_id in circle['members']:
                insight_record = {
                    'author': user_id,
                    'content': insight,
                    'timestamp': time.time(),
                    'resonance_score': 0,
                    'validation_count': 0
                }
                circle['shared_insights'].append(insight_record)
                
                # 奖励分享者
                self.reward_insight_sharing(user_id, insight_record)
                return True
        return False
        
    def establish_mentorship(self, mentor_id, student_id):
        """建立师徒关系"""
        mentor_level = self.practitioners.get(mentor_id, {}).get('wisdom_level', 0)
        student_level = self.practitioners.get(student_id, {}).get('wisdom_level', 0)
        
        # 确保导师有足够的智慧等级
        if mentor_level >= student_level + 2:
            if mentor_id not in self.mentorship_network:
                self.mentorship_network[mentor_id] = []
            self.mentorship_network[mentor_id].append(student_id)
            return True
        return False
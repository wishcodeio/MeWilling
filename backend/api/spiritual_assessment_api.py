class SpiritualAssessmentAPI:
    def __init__(self):
        self.inner_metrics = {
            "正念水平": 0,
            "道德修養": 0,
            "心理韌性": 0,
            "情緒管理": 0
        }
        self.outer_metrics = {
            "個人成就": 0,
            "社交影響": 0,
            "物質財富": 0,
            "社會貢獻": 0
        }
        
    def calculate_spiritual_shang(self):
        # 計算心靈維度的商增值
        inner_total = sum(self.inner_metrics.values())
        outer_total = sum(self.outer_metrics.values())
        
        if inner_total == 0:
            return {
                "警告": "內在修養不足，需要加強分母建設",
                "建議": "專注於正念修練和道德提升"
            }
            
        spiritual_shang = outer_total / inner_total
        return self.interpret_spiritual_balance(spiritual_shang)
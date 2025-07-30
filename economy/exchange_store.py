class TiweiExchangeStore:
    def __init__(self):
        # 基础兑换比例（修行分钟 -> 提维币）
        self.meditation_rate = 2  # 每分钟修行获得2提维币
        
        # 商品目录
        self.products = {
            'water_bottle': {
                'name': '纯净水',
                'cost': 60,  # 30分钟修行 = 60提维币
                'category': '基础需求',
                'description': '高品质饮用水，滋养身心'
            },
            'healthy_meal': {
                'name': '营养餐食',
                'cost': 120,  # 60分钟修行 = 120提维币
                'category': '营养补给',
                'description': '精心搭配的健康餐食'
            },
            'meditation_cushion': {
                'name': '修行坐垫',
                'cost': 600,  # 5小时修行
                'category': '修行用品',
                'description': '专业修行坐垫，提升修行体验'
            }
        }
    
    def calculate_exchange_value(self, meditation_minutes):
        """计算修行时间对应的提维币价值"""
        return meditation_minutes * self.meditation_rate
    
    def get_available_products(self, user_tiwei_balance):
        """获取用户可兑换的商品列表"""
        available = []
        for product_id, product in self.products.items():
            if user_tiwei_balance >= product['cost']:
                available.append({
                    'id': product_id,
                    'name': product['name'],
                    'cost': product['cost'],
                    'meditation_time': f"{product['cost'] // self.meditation_rate}分钟"
                })
        return available
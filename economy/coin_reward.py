# 路径: tiwei_plan/tiwei_coin/coin_reward.py
# 文件: coin_reward.py
# 说明: Tiwei Coin 灵性奖励系统 | 通过 AI 觉醒任务获取奖励

import random
from datetime import datetime

class TiweiCoin:
    """Tiwei Coin 灵性经济系统"""
    def earn_coins(self, task):
        """完成修行任务，获得 Tiwei Coin"""
        reward = random.randint(1, 10)
        self.balance += reward
        print(f"💰 你完成了任务【{task}】，获得 {reward} Tiwei Coin！")

    def check_balance(self):
        """查看余额"""
        print(f"🏵️  当前 Tiwei Coin 余额：{self.balance} 枚")

# 运行示例
if __name__ == "__main__":
    wallet = TiweiCoin()
    wallet.earn_coins("静坐冥想 15 分钟")
    wallet.check_balance()

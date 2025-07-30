import hashlib
import time
import json

class Block:
    """Tiwei Coin 区块"""
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions  # 修行者的智慧贡献
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        """计算区块哈希"""
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """Tiwei Coin 区块链"""
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
    
    def add_block(self, transactions):
        """添加新区块 - 记录修行者的智慧贡献"""
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, transactions)
        self.chain.append(new_block)

    def create_genesis_block(self):
        """创建创世区块"""
        genesis_block = Block(0, "0", ["Genesis Block"])
        self.chain.append(genesis_block)

    def verify_chain(self):
        """验证区块链完整性"""
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash:
                return False
        return True

if __name__ == "__main__":
    # 初始化 Tiwei 区块链
    tiwei_blockchain = Blockchain()

    # 添加修行贡献
    tiwei_blockchain.add_block(["修行者 A 领悟‘无为而治’"])
    tiwei_blockchain.add_block(["修行者 B 贡献‘道家智慧’"])

    # 验证区块链
    print("⛓️ Tiwei Coin 区块链是否有效:", tiwei_blockchain.verify_chain())

    # 打印区块信息
    for block in tiwei_blockchain.chain:
        print(f"📜 区块 {block.index}: {block.transactions}, 哈希: {block.hash}")

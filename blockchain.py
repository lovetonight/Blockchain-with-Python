import hashlib
import json


class Block:
    def __init__(self, data):
        self.data = data
        self.prev_hash = ""
        self.hash = ""
        self.nonce = 0


def hash(block):
    data = json.dumps(block.data) + block.prev_hash + str(block.nonce)
    data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()


class Blockchain():
    def __init__(self, owner):
        self.chain = []
        self.owner = owner
        block = Block("Dao Trong Hoan")
        block.hash = hash(block)
        self.chain.append(block)

    def print(self):
        for block in self.chain:
            print("Previous Hash: ", block.prev_hash)
            print("Data: ", block.data)
            print("Hash: ", block.hash)
            print("\n")

    def add_block(self, data):
        block = Block(data)
        block.data.append({"from": "", "to": self.owner, "amount": 1000})
        while hash(block).startswith("00") == False:
            block.nonce = block.nonce + 1
        block.hash = hash(block)
        block.prev_hash = self.chain[-1].hash
        self.chain.append(block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]
            if current_block.hash != hash(current_block):
                return False
            if (prev_block.hash != current_block.prev_hash):
                return False
        return True

    def get_balance(self, person):
        balance = 0
        for block in self.chain:
            if type(block.data) != list:
                continue
            for transfer in block.data:
                if transfer["from"] == person:
                    balance = balance - transfer["amount"]
                if transfer["to"] == person:
                    balance = balance + transfer["amount"]
        return balance


blockchain = Blockchain("Hoan")
# blockchain.add_block("Nguyen Thanh Luan")
# blockchain.add_block("Nguyen Phuong Linh")
# blockchain.print()
# blockchain.chain[1].data = "Tran Minh Hiep"
# blockchain.print()
# print(blockchain.is_valid())
blockchain.add_block([{"from": "Hoan", "to": "Luan", "amount": 60},
                     {"from": "Hoan", "to": "Linh", "amount": 40},
                     {"from": "Luan", "to": "Linh", "amount": 30},
                     {"from": "Linh", "to": "Hoan", "amount": 20}])
blockchain.add_block([{"from": "Hiep", "to": "Hoan", "amount": 50},
                     {"from": "Hiep", "to": "Linh", "amount": 40},
                     {"from": "Linh", "to": "Hoan", "amount": 20}])
print(blockchain.get_balance("Hoan"))
# blockchain.print()

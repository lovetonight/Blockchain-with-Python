import hashlib


class Block:
    def __init__(self, data):
        self.data = data
        self.prev_hash = ""
        self.hash = ""
        self.nonce = 0


def hash(Block):
    data = Block.data + Block.prev_hash + str(Block.nonce)
    data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()


class Blockchain():
    def __init__(self):
        self.chain = []

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


blockchain = Blockchain()
blockchain.add_block("Nguyen Thanh Luan")
blockchain.add_block("Nguyen Phuong Linh")
blockchain.print()
blockchain.chain[1].data = "Tran Minh Hiep"
blockchain.print()
print(blockchain.is_valid())

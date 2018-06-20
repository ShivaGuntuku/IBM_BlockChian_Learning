from hashlib import sha256
import json
import time

class Block:
    
    def __init__(self, index, transactions, timestamp):
        self.index = []
        self.transactions = transactions
        self.timestamp = timestamp


    def compute_hash(block):
        """A function that creates the hash of the block"""
        block_string = json.dumps(self.__dict__, sort_keys = True)
        return sha256(block_string.encode()).hexdigest()

class Blockchain:

    def __init__(self):
        self.unconfirmed_transactions = [] # data yet to get into the block
        self.chain =  []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        A function to generate genesis block and appends to it to the chain.
        the block has index 0, previous hash as 0, and a valid hash. 
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]
    
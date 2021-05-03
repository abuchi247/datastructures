import time
import json
import hashlib


class Blockchain(object):
    def __init__(self):
        self.chain = []

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if (len(self.chain) > 0):
            block.prev = self.get_last_block().hash
        else:
            block.prev = "none"
        self.chain.append(block)


class Block(object):
    def __init__(self, transactions, time, index):
        self.index = index  # Block number
        self.prev = ''  # stores the hash of the previous block
        self.transactions = transactions # Transaction data
        self.time = time    # Time of the transaction
        self.hash = self.calculate_hash()   # hash the block

    def calculate_hash(self):
        hash_transactions = ""
        for transaction in self.transactions:
            hash_transactions += transaction

        hash_string = f"{self.time}{hash_transactions}{self.prev}{self.index}"
        hash_encoded = json.dumps(hash_string, sort_keys=True).encode()
        return hashlib.sha256(hash_encoded).hexdigest()


class Transaction(object):
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.time = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = f"{self.sender}{self.receiver}{self.amount}{self.amount}"
        hash_encoded = json.dumps(hash_string, sort_keys=True).encode()
        return hashlib.sha256(hash_encoded).hexdigest()

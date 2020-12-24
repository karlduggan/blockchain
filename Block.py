import hashlib
import datetime
import time

class Block:
    def __init__(self, index, proof_of_work, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_of_work = proof_of_work # nonce
        self.data = data
        self.prev_hash = prev_hash
        self.timestamp = timestamp or datetime.datetime.now()
    @property
    def calculate_hash(self):
        block_of_string = "{}{}{}{}".format(self.index, self.proof_of_work,
                                         self.prev_hash,self.data,
                                         self.timestamp).encode()

        inner_hash = hashlib.sha256(block_of_string).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_of_work,
                                             self.prev_hash, self.data,
                                             self.timestamp)
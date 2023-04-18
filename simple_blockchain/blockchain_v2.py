import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        # Initialize a new block with a timestamp, data, previous hash, nonce, and hash
        self.timestamp = datetime.datetime.now() # Current timestamp
        self.data = data # Data to be stored in the block
        self.previous_hash = previous_hash # Hash of the previous block in the chain
        self.nonce = 0 # Nonce value used in proof-of-work algorithm
        self.hash = self.calculate_hash() # Hash of the block

    def calculate_hash(self):
        # Calculate the hash of the block
        block = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce) # Combine block data into a single string
        hash = hashlib.sha256(block.encode()).hexdigest() # Hash the combined data string
        return hash

    def mine_block(self, difficulty):
        # Mine the block using a proof-of-work algorithm with the specified difficulty level
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1 # Increment the nonce value
            self.hash = self.calculate_hash() # Recalculate the hash

class Blockchain:
    def __init__(self):
        # Initialize a new blockchain with a genesis block and a default difficulty level
        self.chain = [self.create_genesis_block()] # The chain of blocks in the blockchain
        self.difficulty = 2 # The difficulty level for proof-of-work

    def create_genesis_block(self):
        # Create the first block in the blockchain (the genesis block)
        return Block("Genesis Block", "0") # Data is "Genesis Block" and previous hash is "0"

    def get_latest_block(self):
        # Return the latest block in the chain
        return self.chain[-1]

    def add_block(self, data):
        # Add a new block to the blockchain with the specified data
        previous_block = self.get_latest_block() # Get the latest block in the chain
        new_block = Block(data, previous_block.hash) # Create a new block with the data and previous block's hash
        new_block.mine_block(self.difficulty) # Mine the new block using proof-of-work
        self.chain.append(new_block) # Add the new block to the chain

    def is_chain_valid(self):
        # Check if the entire blockchain is valid (all blocks have valid hashes and previous hashes)
        for i in range(1, len(self.chain)):
            current_block = self.chain[i] # Get the current block
            previous_block = self.chain[i - 1] # Get the previous block
            if current_block.hash != current_block.calculate_hash(): # Check if the current block's hash is valid
                return False
            if current_block.previous_hash != previous_block.hash: # Check if the current block's previous hash matches the previous block's hash
                return False
        return True

    def print_chain(self):
        # Print the entire blockchain
        for block in self.chain:
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("\n")

# Create a new blockchain
blockchain = Blockchain()

# Add new blocks to the blockchain
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
blockchain.add_block("Block 3")

# Print the entire blockchain
blockchain.print_chain()

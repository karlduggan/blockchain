import hashlib
import time
# Process which is used in mining
nonce = 0 # Proof of work
diff = 5 #  Difficulty

data = "Data within data"
def hash_calculate(data, nonce):
	string = (data+str(nonce)).encode()
	result = hashlib.sha256(string).hexdigest()
	return result

def zeros(diff):
	temp = ""
	for _ in range(diff):
		temp = temp + "0"
	return temp

h1 = hash_calculate(data,nonce)
while h1[:diff] != zeros(diff):
	nonce += 1
	h1 = hash_calculate(data, nonce)
	print(nonce)
print(h1)
print(f"Proof of work Number: {nonce}")

def verify(hashX, data, proof_no):
	string = (data + str(proof_no)).encode()
	result = hashlib.sha256(string).hexdigest()
	if result == hashX:
		print("True")
	else:
		print("False")

#h3 = "00000b23c4d88100962c7c8ecaaf2b85f3c8dc79d24a83b8c63fa8cd901008e3"
#proof = "308193"
#verify(h3, data, proof)

def my_hash_fn(input_string):
	val = 5381
	for c in input_string:
		val = 33*val + ord(c)
	return val
	

class HashTable:
	def __init__(self, hash_fn, size=256):
		self.hash_fn = hash_fn
	
		# Elements of this table are lists of (key, value) pairs.
		self.table = [[] for i in range(size)]

	# This should return the value associated with the key, 
	# raise KeyError if key not present
	def lookup(self, key):
		if key is not in self.table:
			return "error"
		else:
			return self.key

	# What should this return? Up to you. Maybe no return?
	# You should use CHAINING here to resolve collisions.
	def assign(self, key, value):
		self.table.key = value
		

print("henry has a huge left bicep it's so juicy")

def henrysgiantcalf(henryleg):
	jonahface = 69
	if henryleg == teeronleg:
		return jonahface



Usage:

d = HashTable(my_hash_fn)
d.assign("winston", 100)
value = d.lookup("winston")
print(value) # Should print 100.

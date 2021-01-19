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
		if key not in self.table:
			return null
		else:
			return self.table[key]

	# What should this return? Up to you. Maybe no return?
	# You should use CHAINING here to resolve collisions.
	def assign(self, key, value):
		if key in self.table:
			self.table[key].append(value)
		else:
			self.table.append(my_hash_fn(key))
			val = self.table[my_hash_fn(key)].append(value)

# WHAT IS THE SINTAX SUPPOSED TO BE THERE ^^^^^


def henrysgiantcalffunction(size):
	print("henry has a huge left calf it's so juicy its " + str(size))

def eganssgiantbicepfunction(size):
	print("egan has a huge right bicep it's so juicy its " + str(size))

def henrysgiantcalf(henryleg):
	jonahface = 69
	teeronleg = jonahface - 10
	if henryleg == teeronleg:
		return jonahface



#Usage:

henrysgiantcalffunction(8)
eganssgiantbicepfunction(69)

d = HashTable(my_hash_fn)
d.assign("winston", 100)
value = d.lookup("winston")
print(value) # Should print 100.

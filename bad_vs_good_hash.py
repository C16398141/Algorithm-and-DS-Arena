import string
import timeit

class BadHash(str):
	# badhash can take in a string argument
	def __hash__(self):
		return 42
class GoodHash(str):
	def __hash__(self):
		return ord(self[1]) + (26 * ord(self[0])) - 2619
	
baddict = set()
gooddict = set()

# letter from [a-z]
for i in string.ascii_lowercase:
	for j in string.ascii_lowercase:
		# gentating a pair of letters
		key = i + j
		# baddict will return 42 for all the keys being hashed
		baddict.add(BadHash(key))
		# gooddict will have a distributed range of keys
		gooddict.add(GoodHash(key))
		
badtime = timeit.repeat(
						'key in baddict',
						setup = "from __main__ import baddict, \
								 BadHash; key = BadHash('zz')",
						repeat = 3,
						number = 1000000,
						)
goodtime = timeit.repeat(
						'key in gooddict',
						setup = "from __main__ import gooddict, \
								 GoodHash; key = GoodHash('zz')",
						repeat = 3,
						number = 1000000,
						)

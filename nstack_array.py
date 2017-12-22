class StackBound(object):
	def __init__(self, lbound, ubound):
		self.lbound = lbound
		self.ubound = ubound
		self.index = lbound-1
		
	def next_index(self):
		self.index += 1

	def prev_index(self):
		self.index -= 1

	def unsafe_write(self):
		return self.index == self.ubound

	def unsafe_read(self):
		return self.index == self.lbound -1

class NStackArray(object):
	def __init__(self,size,nstack):
		self.size = size
		self.nstack = nstack
		self.entry = []
		self.array = []
		if not self.partition():
			raise IndexError(f'Invalid stack number.')

	def __repr__(self):
		return str(self.array)

	def partition(self):
		if self.size >= self.nstack: # nstack is 3
			self.array = [None] * self.size
			self.entry = [None] * self.nstack
			initial = self.size // self.nstack
			evenly = initial
			start = count = 0
			remainder = self.size % self.nstack

			while count < self.nstack -1:
				self.entry[count] = StackBound(start, evenly -1)
				count +=1
				start = initial * count
				evenly += initial
				
			self.entry[count] = StackBound(start, evenly -1 + remainder)
			return True
		return False		

	def pop(self,stacknum):
		if self.entry[stacknum -1].unsafe_read():
			print(f'The stack number {stacknum} is empty')
		else:
			val = self.array[self.entry[stacknum -1].index]
			self.array[self.entry[stacknum -1].index] = None
			self.entry[stacknum -1].prev_index()
			return val

	def peek(self,stacknum):
		if self.entry[stacknum -1].unsafe_read():
			print(f'The stack number {stacknum} is empty')
		else:
			return self.array[self.entry[stacknum -1].index]
			

	def push(self,stacknum,val):
		if self.entry[stacknum -1].unsafe_write():
			print(f'The stack number {stacknum} is full')
		else:
			self.array[self.entry[stacknum -1].index + 1] = val
			self.entry[stacknum -1].next_index()

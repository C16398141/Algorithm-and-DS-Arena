from Queue import *

class Stack(Queue):

	def __init__(self, *values, **kwargs):
		super().__init__(self, *values, **kwargs)

	def __repr__(self):
		return ' - '.join([str(item) for item in self])

	def pop(self):
		return super().deque()

	def push(self, *values):
		super().enque(*values,head = self.head)
	

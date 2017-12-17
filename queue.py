"""Queue implmentation using a list"""

from collections import deque

class Queue(object):
	def __init__(self, head=None):
		self.storage = deque([head])

	def enqueue(self, new_element):
		self.storage.append(new_element)

	def peek(self):
		return self.storage[0] 

	def dequeue(self):
		return self.storage.popleft()

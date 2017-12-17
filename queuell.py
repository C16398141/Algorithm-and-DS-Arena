class Node(object):
	def __init__(self,data, next_node = None):
		self.data = data
		self.next_node = next_node

	def __repr__(self):
		return str(self.data)
	
class Queue(object):
	def __init__(self,*values, **kwargs):
		self.head = self.tail = None
		self.max_size = kwargs.get('max_size', 10)
		self.length = 0
		if len(values) > 0:
			self.enque(*values) # have to be unpcked

	def __repr__(self):
		return ' < '.join([str(val) for val in self]) 

	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next_node
			
	def __len__(self):
		return self.length
	
	def __contains__(self,val):
		return self.contains(self.head, val)

	def is_full(self):
		return self.length == self.max_size

	def is_empty(self):
		return self.head == self.tail == None

	def peek(self):
		return self.head.data


	def free_slots(self):
		return self.max_size - self.length

	
	def expand(self, size):

		if size <= self.max_size * (-1):
			raise ValueError(f"Max size can't go below {1}")
		
		elif size<0 and self.free_slots() < (size * (-1)):
			for i in range(size*(-1)):
				self.deque(quiet=True)
				
		self.max_size += size
			
	
	def enque(self, *values):
		if len(values) > 0:
			for val in values:
				if self.is_full():
					raise ValueError (f"Maximum {type(self).__name__} size reached")
				else:
					new_node = Node(val)
					if not self.is_empty():
						self.tail.next_node = new_node
						self.tail = new_node
					else:
						self.head = self.tail = new_node

					self.length += 1
		else:
			raise ValueError ("No items to enque")
		
				
	def deque(self, quiet=False):
		if self.is_empty():
			raise ValueError (f"{type(self).__name__} is empty")
		val = self.peek()
		self.head = self.head.next_node
		self.length -=1
		if not quiet:
			return val
	
	
	def contains(self,head,val):
		if head == None:
			return False
		elif head.data == val:
			return True
		return self.contains(head.next_node, val)

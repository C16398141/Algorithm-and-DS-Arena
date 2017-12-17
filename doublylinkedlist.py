# Tatiana Zihindula
# Implement a doubly linked list class, where every node points to the previous
# Except the last node which points to null

class Node(object):
	
	def __init__(self, data):
		self.data = data
		self.next_node = None
		self.previous = None
	

	def __repr__(self):
		"""return string representation of data"""
		return str(self.data)

class LinkedList(object):
	length = 0 #(O)1 for retrieval

	def __init__(self, *values):
		'''A new linked list has a head and a tail'''
		self.head = None
		self.tail = None

		if values:
		# if values were passed, unpack them then add them all
			self.add(*values)

	def __iter__(self):
		'''Converts a Linked List object into an iterable'''
		current = self.head
		while current:
			# yield the value in current node
			yield current.data
			# then go to the next until 'None'
			current = current.next_node

	def __repr__(self):
		'''Returns the string representation of the list'''
		return '['+'->'.join([str(x) for x in self]) +']'

	def __contains__(self, val):
		'''The search function returns the Node containing val'''
		return self.search(self.head,val) != None 

	def is_empty(self):
		return self.head == self.tail == None

	def __len__(self):
		return self.length
	
	def add(self, *values):
		"""unpacks the values in values"""
		for val in values:
			new_node = Node(val)
			if self.is_empty():
				self.head = self.tail = new_node
			else:
				self.tail.next_node = new_node
				temp = self.tail
				self.tail = new_node
				self.tail.previous = temp
			self.length += 1


	def search(self, head, val):
		'''Recursive version of the search through the linked list'''
		if head == None or head.data == val:
			return head
		else:
			return self.search(head.next_node, val)

		
	def remove(self, val):
		'''removes a node from the Linked list'''
		if self.is_empty() : raise ValueError ('List is empty')
		else:
			current = self.search(self.head,val)
			if current == None:
				raise ValueError (f'{val} not in the list')
			else:
				if current == self.head:
				# remove at the head node
					self.head = self.head.next_node
					self.head.previous = None
					
				elif current == self.tail:
				# remov at the tail
					self.tail = self.tail.previous
					self.tail.next_node = None
				else :
				# remove in the middle
					current.previous.next_node = current.next_node
					current.next_node.previous = current.previous
					
				self.length -= 1
					
	def pop(self):
		'''Deletes the element at the tail and returns it'''
		temp = self.tail.data
		self.remove(self.tail.data)
		return temp

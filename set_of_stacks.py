
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next_node = None
		
	def __repr__(self):
		return str(self.data)

	
class Stack(object):
	def __init__(self, *args, **kwargs):
		self.head = None
		self.__len = 0

		if args:
			for val in args:
				self.push(val)

	def __len__(self):
		return self.__len
		
	def push(self,value):
		new_node = Node(value)
		if not self.head:
			self.head = new_node
		else:
			new_node.next_node = self.head
			self.head = new_node
		self.__len +=1

	def pop(self):
		if len(self) == 0:
			raise ValueError(type(self).__name__ + ' is empty!')
		else:
			val = self.head.data
			self.head = self.head.next_node
			self.__len -=1
			return val



class SetStack(object):
	def __init__(self, *args, **kwargs):
		self.capacity = kwargs.get('capacity', 8)
		self.stacks = []
		self.head = None
		if args:
			for val in args:
				self.push(val)
	def __repr__(self):
		return ' - '.join([str(it) for it in self])
		
	def __len__(self):
		return len(self.stacks)

	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current=current.next_node
	
	def push(self,value):
		if not self.stacks:
			self.stacks.append(Stack(value))
			
		elif not len(self.stacks[-1]) == self.capacity:
			self.stacks[-1].push(value)	
		else:
			temp = Stack(value)
			temp.head.next_node = self.stacks[-1].head
			self.head = temp.head
			self.stacks.append(temp)
			
		self.head = self.stacks[-1].head

	def pop(self):
		if not self.stacks:
			raise ValueError(type(self).__name__ + ' is empty!')	
		else:
			self.head = self.stacks[-1].head.next_node
			val = self.stacks[-1].pop()
			if not len(self.stacks[-1]):
				del self.stacks[-1]	
			return val

	def print_kth(self, k):

		def print_it(node):
			if node:
				print_it(node.next_node)
				print(node.data, end=" ")
				
		def find(head,k):
			if head and k > 0:
				if k == 1:
					return head
				elif k == 2:
					return head.next_node
				else:
					k -= 2
					return find(head.next_node.next_node, k)
				
		print_it(find(self.head,k))
				

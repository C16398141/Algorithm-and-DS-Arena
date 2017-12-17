# -*- coding: utf-8 -*- 
class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
		
class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def append(self, new_element):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element
			
	def get_position(self, positionn):
		"""Get an element from a particular position.
		Assume the first position is "1".
		Return "None" if position is not in the list."""
		
		def position(head,pos):
			if head and pos > 0:
				if pos == 1:
					return head
				elif pos == 2:
					return head.next
				else:
					# go two nodes ahead
					pos -=2
					return position(head.next.next, pos)
			return None
		
		return position(self.head,positionn)

	def insert_first(self, new_element):
		"Insert new element as the head of the LinkedList"
		new_element.next = self.head
		self.head = new_element
		return True

	def delete_first(self):
		"Delete the first (head) element in the LinkedList as return it"
		node = self.head if self.head else None
		if self.head:
			self.head = self.head.next
		return node
	
	def insert(self, new_element, position):
		"""
			Insert a new node at the given position.
			Assume the first position is "1".
			Inserting at position 3 means between
			the 2nd and 3rd elements.
		"""
		
		# if insert at head. i.e position 1
		if position == 1:
			if not self.head:
				self.head = new_element #nothing in the list
			else:
				new_element.next = self.head
				self.head = new_element
		else:
			# not at the head, use the runner technique
			# get the previous node position first
			# even append at the tail should return a valid node
			node = self.get_position(position-1)
			if not node:
				raise IndexError ("Invalid position")
			else:
				new_element.next = node.next
				node.next = new_element
		return True
		
	def get_value_position(self, value):
		""" returns the previous node preceding the target """
		if self.head.value == value:
			return self.head
		
		# not the top of the list
		# the head node has already been checked.
		previous = self.head
		current = self.head.next
		while current:
			if current.value == value:
				return previous
			previous = current
			current = current.next
			
		return None  
	
	def delete(self, value):
		""" Delete the first node with a given value. """
		node = self.get_value_position(value)
		if not node:
			raise ValueError ("Value not in the list")
			
		elif node is self.head:
			self.head = self.head.next
		else:
			# lose the reference of that node
			node.next = node.next.next
			
		return True

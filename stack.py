# stack implementation from using a LinkedList Class
from linkedlist import LinkedList, Node

class Stack(object):
	def __init__(self,top=None):
		self.ll = LinkedList(top)

	def push(self, new_element):
		"Push (add) a new element onto the top of the stack"
		return self.ll.insert_first(new_element)

	def pop(self):
		"remove the element at the top of the stack and return it"
		return self.ll.delete_first()

class Node:
	def __init__(self):
		self.value = None
		self.next = None
		self.prev = None


class LinkedList:
	def __init__(self):
		self.first = None
		self.last = None

	def insert(self, value):
		"""
		Inserts value to linked list.
		:param value: Value to insert.
		:return: Inserted node.
		"""
		n = Node()
		n.value = value
		n.prev = self.last
		self.last = n

		if self.first is None:
			self.first = n
		return n

	def print_list(self):
		"""
		Prints linked list.
		"""
		n = self.first
		while n is not None:
			print(n)
			n = n.next

	def search(self, value):
		"""
		Returns reference to first node with value.
		:param value: Value to search.
		:return: Reference to first node with value, if value is not in list returns None.
		"""
		n = self.first
		while n is not None and n.value != value:
			n = n.next
		return n

	def delete(self, node):
		"""
		Deletes node.
		:param node: Node to delete.
		"""
		if node.next is None:
			self.last = node.prev
		else:
			node.next.prev = node.prev
		if node.prev is None:
			self.first = node.next
		else:
			node.prev.next = node.next

class Item:
	def __init__(self):
		# value: Represents the stored value.
		self.value = None
		# below: Reference to the previous element in the stack.
		self.below = None


class Stack:
	def __init__(self):
		# top: Reference to the top item in the stack.
		self.top = None

	def push(self, value):
		"""
		Inserts at the top of the stack a new item with the value.
		:param self: Stack in which will be value inserted.
		:param value: Value to insert.
		"""
		i = Item()
		i.value = value
		i.below = self.top

		self.top = i

	def pop(self):
		"""
		Removes top item from stack.
		:param self: Stack.
		:return: Removed item. If stack is empty then None.
		"""
		if Stack.isEmpty(self):
			return None
		else:
			key = self.top.value
			self.top = self.top.below
		return key

	def peek(self):
		"""
		Returns top item from stack.
		:param self: Stack.
		:return: Item. If stack is empty then None.
		"""
		if Stack.isEmpty(self):
			return None
		else:
			key = self.top.value
		return key

	def isEmpty(self):
		"""
		Tests empty stack.
		:param self: Stack.
		:return: True if stack is empty, false otherwise.
		"""
		if self.top is None:
			return True
		else:
			return False

	def print(self):
		"""
		Prints items of stack.
		"""
		s = self

		while not s.isEmpty():
			print(s.pop())

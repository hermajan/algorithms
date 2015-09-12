class Item:
	"""
	Class for items in queue.
	"""
	def __init__(self):
		"""
		value: Value of item.
		left: Reference to previous item in queue.
		"""
		self.value = None
		self.left = None


class Queue:
	def __init__(self):
		"""
		first: Reference to first item in queue.
		last: Reference to last item in queue.
		"""
		self.first = None
		self.last = None

	def enqueue(self, value):
		"""
		Inserts new item to queue.
		:param value: Value of item.
		"""
		added = Item()
		added.value = value
		added.left = None

		if self.last is None:
			self.first = added
		else:
			self.last.left = added
		self.last = added

	def dequeue(self):
		"""
		Deletes first item in queue.
		:return: Value of deleted item, if queue is empty returns None.
		"""
		if self.isEmpty():
			return None
		key = self.first.value

		if self.first == self.last:
			self.first = None
			self.last = None
		else:
			self.first = Queue.first.left

		return key

	def isEmpty(self):
		"""
		Returns True if queue is empty, False otherwise.
		:return: True if queue is empty, False otherwise.
		"""
		if self.first is None:
			return True
		return False

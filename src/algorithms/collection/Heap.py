import sys


class MinHeap:
	"""
	Minimal heap.
	"""
	def __init__(self):
		"""
		size: Number of items in heap.
		array: Array of items in heap.
		"""
		self.size = 0
		self.array = None

	def parent_index(self, i):
		"""
		Returns parent index of item.
		:param i: Position of item.
		:return: Parent index of item on position i, if not exists returns None.
		"""
		index = (i-1) // 2
		if index < 0:
			return None
		return index

	def left_index(self, i):
		"""
		Returns left index of item.
		:param i: Position of item.
		:return: Left index of item on position i.
		"""
		return 2*i + 1

	def right_index(self, i):
		"""
		Returns right index of item.
		:param i: Position of item.
		:return: Right index of item on position i.
		"""
		return 2*i + 2

	def parent(heap, i):
		"""
		Returns parent of item.
		:param heap: Heap for getting parent.
		:param i: Position of item.
		:return: Parent of item on position i, if not exists returns None.
		"""
		index = heap.parent_index(i)
		if index is None:
			return None
		return heap.array[index]

	def left(heap, i):
		"""
		Returns left child of item.
		:param heap: Heap for getting child.
		:param i: Position of item.
		:return: Left child of item on position i, if not exists returns None.
		"""
		index = heap.left_index(i)
		if len(heap.array) <= index:
			return None
		return heap.array[index]

	def right(heap, i):
		"""
		Returns right child of item.
		:param heap: Heap for getting child.
		:param i: Position of item.
		:return: Right child of item on position i, if not exists returns None.
		"""
		index = heap.right_index(i)
		if len(heap.array) <= index:
			return None
		return heap.array[index]

	def swap(heap, i, j):
		"""
		Swaps items on positions.
		:param heap: Heap for swapping.
		:param i: Position of item.
		:param j: Position of item.
		"""
		heap.array[i], heap.array[j] = heap.array[j], heap.array[i]

	def heapify(heap, i):
		"""
		Fixes heap to correct minimal heap.
		:param heap: Heap for fixing.
		:param i: Position where heapify starts fixing.
		"""
		smallest = i
		if heap.left_index(i) < heap.size and heap.left(i) < heap.array[smallest]:
			smallest = heap.left_index(i)
		if heap.right_index(i) < heap.size and heap.right(i) < heap.array[smallest]:
			smallest = heap.right_index(i)
		if smallest != i:
			heap.swap(i, smallest)
			heap.heapify(smallest)

	@staticmethod
	def build_heap(array):
		"""
		Builds correct minimal heap from array.
		:param array: Array for building.
		:return: Minimal heap.
		"""
		heap = MinHeap()
		heap.size = len(array)
		heap.array = array

		for i in reversed(range(heap.size // 2)):
			heap.heapify(i)
		return heap

	def decrease_key(heap, i, value):
		"""
		Decreases value for item.
		:param heap: Heap for decreasing.
		:param i: Position of item.
		:param value: Value of item.
		"""
		if heap.array[i] < value:
			return

		heap.array[i] = value
		while i > 0 and heap.parent(i) > heap.array[i]:
			heap.swap(i, heap.parent_index(i))
			i = heap.parent_index(i)

	def insert(heap, value):
		"""
		Inserts value to heap.
		:param heap: Heap for inserting.
		:param value: Value for inserting.
		"""
		heap.size += 1
		heap.array.append(sys.maxsize)
		heap.decrease_key(heap.size-1, value)

	def extract_min(heap):
		"""
		Extracts minimal item from heap.
		:param heap: Heap for extracting.
		:return: Value of extracted item, if heap is empty returns None.
		"""
		if heap.size <= 0:
			return None

		min = heap.array[0]
		heap.array[0] = heap.array[heap.size-1]
		heap.size -= 1
		heap.heapify(0)
		return min

	@staticmethod
	def heap_sort(array):
		"""
		Sorts array through heap from largest item to lowest.
		:param array: Array for sorting.
		:return: Sorted array.
		"""
		heap = MinHeap.build_heap(array)

		for i in reversed(range(heap.size)):
			heap.swap(0, i)
			heap.size -= 1
			heap.heapify(0)

		array[:] = heap.array
		return array

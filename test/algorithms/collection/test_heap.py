from unittest import TestCase
from algorithms.collection.Heap import MinHeap


class TestHeap(TestCase):
	def test_build_heap(self):
		array = [4, 3, 1]
		heap = MinHeap.build_heap(array)

		self.assertEqual(heap.size, 3)
		try:
			self.assertEqual(heap.array, [1, 3, 4])
		except AssertionError:
			self.assertEqual(heap.array, [1, 4, 3])

	def test_decrease_key(self):
		heap = MinHeap()
		heap.array = [2, 3, 4]
		heap.size = 3
		heap.decrease_key(2, 1)

		self.assertEqual(heap.array, [1, 3, 2])
		self.assertEqual(heap.size, 3)

		heap.decrease_key(0, 4)
		self.assertEqual(heap.array, [1, 3, 2])
		self.assertEqual(heap.size, 3)

	def test_insert(self):
		heap = MinHeap()
		heap.array = []
		heap.size = 0

		heap.insert(2)
		self.assertEqual(heap.array, [2], "Error in inserting on empty heap.")
		self.assertEqual(heap.size, 1)

		nonempty = "Error in inserting on nonempty heap."
		heap.insert(3)
		heap.insert(4)
		self.assertEqual(heap.array, [2, 3, 4], nonempty)
		self.assertEqual(heap.size, 3)

		heap.insert(5)
		self.assertEqual(heap.array, [2, 3, 4, 5], nonempty)
		self.assertEqual(heap.size, 4)

		heap.insert(1)
		self.assertEqual(heap.array, [1, 2, 4, 5, 3], nonempty)
		self.assertEqual(heap.size, 5)

	def test_extract_min(self):
		heap = MinHeap()
		heap.array = [2, 3, 4, 5]
		heap.size = 4

		item = heap.extract_min()
		self.assertEqual(heap.array[0:heap.size], [3, 5, 4])
		self.assertEqual(item, 2)

		item = heap.extract_min()
		self.assertEqual(heap.array[0:heap.size], [4, 5])
		self.assertEqual(item, 3)

		item = heap.extract_min()
		self.assertEqual(heap.array[0:heap.size], [5])
		self.assertEqual(item, 4)

		item = heap.extract_min()
		self.assertEqual(heap.array[0:heap.size], [])
		self.assertEqual(item, 5)

		item = heap.extract_min()
		self.assertEqual(item, None)

	def test_heap_sort(self):
		array = [8, 4, 9, 3, 2, 7, 5, 0, 6, 1]
		sort = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

		self.assertEqual(MinHeap.heap_sort(array), sort)

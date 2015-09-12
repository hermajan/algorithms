from unittest import TestCase
from algorithms.collection.Queue import Queue
from algorithms.collection.Queue import Item


class TestQueue(TestCase):
	def test_enqueue(self):
		q = Queue()
		q.enqueue(1)

		# Inserting to empty queue.
		self.assertIsNotNone(q.first)
		self.assertIsNotNone(q.last)

		self.assertEqual(q.first.value, 1)
		self.assertIsNone(q.first.left)
		self.assertEqual(q.last.value, 1)
		self.assertIsNone(q.last.left)

		# Inserting to nonempty queue.
		q = Queue()
		i = Item()
		i.left = None
		i.value = 1
		q.first = i
		q.last = i

		q.enqueue(2)
		self.assertIsNotNone(q.first)
		self.assertIsNotNone(q.last)

		self.assertEqual(q.last.value, 2)
		self.assertEqual(q.first, i)
		self.assertEqual(q.first.left.value, 2)

	def test_dequeue(self):
		q = Queue()
		v = q.dequeue()

		# Deleting in empty queue.
		self.assertIsNone(v)
		self.assertIsNone(q.first)
		self.assertIsNone(q.last)

		# Deleting in nonempty queue.
		q = Queue()
		i = Item()
		i.value = 1
		i.left = None
		q.first = i
		q.last = i
		v = q.dequeue()

		self.assertEqual(v, 1)
		self.assertIsNone(q.first)
		self.assertIsNone(q.last)

	def test_isEmpty(self):
		q = Queue()
		self.assertTrue(q.isEmpty())

		i = Item()
		i.left = None
		i.value = 1
		q.first = i
		q.last = i
		self.assertFalse(q.isEmpty())

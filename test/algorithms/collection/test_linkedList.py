from unittest import TestCase
from algorithms.collection.LinkedList import LinkedList, Node


class TestLinkedList(TestCase):
	def test_insert(self):
		l = LinkedList()
		l.insert(1)

		# Inserting to empty queue.
		self.assertIsNotNone(l.first)
		self.assertIsNotNone(l.last)

		self.assertEqual(l.first.value, 1)
		self.assertEqual(l.last.value, 1)
		self.assertIsNone(l.first.next)
		self.assertIsNone(l.last.prev)

		# Inserting to nonempty queue.
		l = LinkedList()
		n = Node()
		n.value = 1
		n.next = None
		l.first = n
		l.last = n

		l.insert(2)
		self.assertIsNotNone(l.last)
		self.assertEqual(l.last.value, 2)
		self.assertIsNotNone(l.last.prev)

		self.assertEqual(l.last.prev, l.first)
		self.assertEqual(l.first.value, 1)

	def test_search(self):
		l = LinkedList()
		n1 = Node()
		n2 = Node()
		n1.value = 1
		n1.next = n2
		n1.prev = None
		n2.value = 2
		n2.next = None
		n2.prev = n1
		l.first = n1
		l.last = n2

		i = l.search(2)
		self.assertEqual(i, n2)

		i = l.search(3)
		self.assertIsNone(i)

	def test_delete(self):
		l = LinkedList()
		n1 = Node()
		n2 = Node()
		n3 = Node()
		n1.value = 1
		n1.next = n2
		n1.prev = None
		n2.value = 2
		n2.next = n3
		n2.prev = n1
		n3.value = 3
		n3.next = None
		n3.prev = n2
		l.first = n1
		l.last = n3

		l.delete(n2)
		self.assertEqual(l.last, n3)
		self.assertEqual(l.last.prev, n1)
		self.assertIsNone(l.search(2))

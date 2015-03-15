from unittest import TestCase

from src.algorithms.collection.Stack import Item
from src.algorithms.collection.Stack import Stack


class TestStack(TestCase):
	def test_push(self):
		# Inserting to the empty stack.
		s = Stack()
		s.push(1)

		self.assertIsNotNone(s.top)
		self.assertIs(s.top.value, 1)
		self.assertIsNone(s.top.below)

		# Inserting to the nonempty stack.
		i = Item()
		i.below = None
		i.value = 1
		s.top = i
		s.push(2)

		self.assertIsNotNone(s.top)
		self.assertIs(s.top.value, 2)
		self.assertIs(s.top.below, i)

	def test_pop(self):
		# Removing from the empty stack.
		s = Stack()
		v = s.pop()

		self.assertIsNone(v)
		self.assertIsNone(s.top)

		# Removing from the nonempty stack.
		i = Item()
		i.value = 1
		i.below = None
		s.top = i
		v = s.pop()

		self.assertIs(v, 1)
		self.assertIsNone(s.top)

	def test_peek(self):
		# Returning from the empty stack.
		s = Stack()
		v = s.pop()

		self.assertIsNone(v)

		# Returning from the nonempty stack.
		i = Item()
		i.value = 1
		i.below = None
		s.top = i
		v = s.pop()

		self.assertIs(v, 1)

	def test_isEmpty(self):
		# isEmpty on the empty stack.
		s = Stack()

		self.assertTrue(s.isEmpty())

		# isEmpty on the nonempty stack.
		i = Item()
		i.below = None
		i.value = 1
		s.top = i

		self.assertFalse(s.isEmpty())

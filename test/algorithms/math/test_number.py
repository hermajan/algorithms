from unittest import TestCase
from src.algorithms.math.Number import Number


class TestNumber(TestCase):
	def test_is_even(self):
		print("is_even")
		self.assertEqual(True, Number.is_even(4))
		self.assertEqual(True, Number.is_even(8))
		self.assertEqual(False, Number.is_even(15))
		self.assertEqual(True, Number.is_even(16))
		self.assertEqual(False, Number.is_even(23))
		self.assertEqual(True, Number.is_even(42))

	def test_is_odd(self):
		print("is_odd")
		self.assertEqual(False, Number.is_odd(4))
		self.assertEqual(False, Number.is_odd(8))
		self.assertEqual(True, Number.is_odd(15))
		self.assertEqual(False, Number.is_odd(16))
		self.assertEqual(True, Number.is_odd(23))
		self.assertEqual(False, Number.is_odd(42))

	def test_is_odd_bitwise(self):
		print("is_odd_bitwise")
		self.assertEqual(False, Number.is_odd_bitwise(4))
		self.assertEqual(False, Number.is_odd_bitwise(8))
		self.assertEqual(True, Number.is_odd_bitwise(15))
		self.assertEqual(False, Number.is_odd_bitwise(16))
		self.assertEqual(True, Number.is_odd_bitwise(23))
		self.assertEqual(False, Number.is_odd_bitwise(42))

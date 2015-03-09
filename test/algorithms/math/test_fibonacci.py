from unittest import TestCase
from src.algorithms.math.Fibonacci import Fibonacci


class TestFibonacci(TestCase):
	def test_fib_iterative(self):
		print("fib_iterative")
		self.assertEqual(1, Fibonacci.fib_iterative(1))
		self.assertEqual(1, Fibonacci.fib_iterative(2))
		self.assertEqual(8, Fibonacci.fib_iterative(6))
		self.assertEqual(55, Fibonacci.fib_iterative(10))
		self.assertEqual(144, Fibonacci.fib_iterative(12))

	def test_fib_recursive(self):
		print("fib_recursive")
		self.assertEqual(1, Fibonacci.fib_recursive(1))
		self.assertEqual(1, Fibonacci.fib_recursive(2))
		self.assertEqual(8, Fibonacci.fib_recursive(6))
		self.assertEqual(55, Fibonacci.fib_recursive(10))
		self.assertEqual(144, Fibonacci.fib_recursive(12))

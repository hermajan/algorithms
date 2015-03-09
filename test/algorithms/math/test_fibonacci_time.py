import time
from unittest import TestCase
import sys
from src.algorithms.math.Fibonacci import Fibonacci

sys.setrecursionlimit(6000)


class TestFibonacciTime(TestCase):
	index = 36
	number = 14930352

	def test_fib_iterative_time(self):
		print("Time of iterative calculating of Fibonacci number (O(n)): "),
		start = time.clock()
		result = Fibonacci.fib_iterative(self.index)
		end = time.clock()

		print(str(end - start) + " s\n")
		self.assertEqual(self.number, result)

	def test_fib_recursive_time(self):
		print("Time of recursive calculating of Fibonacci number (O(2^n)): "),
		start = time.clock()
		result = Fibonacci.fib_recursive(self.index)
		end = time.clock()

		print(str(end - start) + " s\n")
		self.assertEqual(self.number, result)

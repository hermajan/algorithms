import sys
import time
from unittest import TestCase
from src.algorithms.math.Exponentiation import Exponentiation

sys.setrecursionlimit(6000)


class TestExponentiationTime(TestCase):
	result = 0

	def setUp(self):
		for i in range(1, 3000):
			self.result += 13 ** i

	def test_power_default_python_time(self):
		print("Time of exponentiation in Python: "),
		start = time.clock()
		counter1 = 0
		for i in range(1, 3000):
			counter1 += 13 ** i
		end = time.clock()

		print(str(end - start) + " s\n")
		self.assertEqual(self.result, counter1)

	def test_power_iterative_time(self):
		print("Time of iterative exponentiation (O(n)): "),
		start = time.clock()
		counter2 = 0
		for i in range(1, 3000):
			counter2 += Exponentiation.power_iterative(13, i)
		end = time.clock()

		print(str(end - start) + " s\n")
		self.assertEqual(self.result, counter2)

	def test_power_log_time(self):
		print("Time of iterative logarithmic exponentiation (O(log(n))): "),
		start = time.clock()
		counter3 = 0
		for i in range(1, 3000):
			counter3 += Exponentiation.power_log(13, i)
		end = time.clock()

		print(str(end - start) + " s\n")
		self.assertEqual(self.result, counter3)

	def test_power_recursive_time(self):
		print("Time of recursive exponentiation (O(n)): "),
		start = time.clock()
		counter4 = 0
		for i in range(1, 3000):
			counter4 += Exponentiation.power_recursive(13, i)
		end = time.clock()

		print(str(end - start) + " s\n")
		self.assertEqual(self.result, counter4)

	def test_power_recursive_log_time(self):
		print("Time of recursive logarithmic exponentiation (O(log(n)): "),
		start = time.clock()
		counter5 = 0
		for i in range(1, 3000):
			counter5 += Exponentiation.power_recursive_log(13, i)
		end = time.clock()

		print(str(end - start) + " s\n")
		self.assertEqual(self.result, counter5)

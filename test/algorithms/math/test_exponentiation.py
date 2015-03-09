from unittest import TestCase
from src.algorithms.math.Exponentiation import Exponentiation


class TestExponentiation(TestCase):
	def test_power_iterative(self):
		print("power_iterative")
		self.assertEqual(1, Exponentiation.power_iterative(0.0, 0))
		self.assertEqual(1024, Exponentiation.power_iterative(2, 10))
		self.assertEqual(15.625, Exponentiation.power_iterative(2.5, 3))
		self.assertEqual(81129638414606681695789005144064.0, Exponentiation.power_iterative(2, 106))

	def test_power_log(self):
		print("power_log")
		self.assertEqual(1, Exponentiation.power_log(0.0, 0))
		self.assertEqual(1024, Exponentiation.power_log(2, 10))
		self.assertEqual(15.625, Exponentiation.power_log(2.5, 3))
		self.assertEqual(81129638414606681695789005144064.0, Exponentiation.power_log(2, 106))

	def test_power_negative(self):
		print("power_negative")
		self.assertEqual(1, Exponentiation.power_negative(0.0, 0))
		self.assertEqual(1024, Exponentiation.power_negative(2, 10))
		self.assertEqual(15.625, Exponentiation.power_negative(2.5, 3))
		self.assertEqual(81129638414606681695789005144064.0, Exponentiation.power_negative(2, 106))

		self.assertAlmostEqual(0.125, Exponentiation.power_negative(2, -3), 3)

	def test_power_recursive(self):
		print("power_recursive")
		self.assertEqual(1, Exponentiation.power_recursive(0.0, 0))
		self.assertEqual(1024, Exponentiation.power_recursive(2, 10))
		self.assertEqual(15.625, Exponentiation.power_recursive(2.5, 3))
		self.assertEqual(81129638414606681695789005144064.0, Exponentiation.power_recursive(2, 106))

	def test_power_recursive_log(self):
		print("power_recursive_log")
		self.assertEqual(1, Exponentiation.power_recursive_log(0.0, 0))
		self.assertEqual(1024, Exponentiation.power_recursive_log(2, 10))
		self.assertEqual(15.625, Exponentiation.power_recursive_log(2.5, 3))
		self.assertEqual(81129638414606681695789005144064.0, Exponentiation.power_recursive_log(2, 106))

	def test_power_real(self):
		print("power_real")
		#self.assertEqual(1, Exponentiation.power_real(0.0, 0))
		self.assertEqual(1024, Exponentiation.power_real(2, 10))
		self.assertAlmostEqual(15.625, Exponentiation.power_real(2.5, 3), 3)
		#self.assertAlmostEqual(81129638414606681695789005144064.0, Exponentiation.power_real(2, 106), 1)

		self.assertAlmostEqual(0.125, Exponentiation.power_real(2, -3), 3)
		self.assertEqual(4, Exponentiation.power_real(16, 0.5))

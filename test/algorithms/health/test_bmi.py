from unittest import TestCase
from algorithms.health.bmi import BMI


class TestBmi(TestCase):
	b = BMI(70, 1.70)
	print(b.index(), b.category())

	def test_index(self):
		self.assertAlmostEqual(24.22, self.b.index(), 2)

	def test_category(self):
		self.assertEqual("healthy weight", self.b.category())

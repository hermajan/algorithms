import math


class BMI:
	"""
	BMI is abbreviation for body mass index.
	"""
	kg = 0
	m = 0.00

	def __init__(self, weight, height):
		self.kg = weight
		self.m = height

	def index(self):
		return self.kg / math.pow(self.m, 2)

	def category(self):
		ind = self.index()

		if ind < 18.5:
			return "underweight"
		elif ind < 25:
			return "healthy weight"
		elif ind < 30:
			return "overweight"
		elif ind >= 30:
			return "obese"
		else:
			return "not on scale"

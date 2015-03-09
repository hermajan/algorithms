import math


class Exponentiation:
	"""Implementations of a exponentiation."""

	@staticmethod
	def power_iterative(base, exp):
		"""
		Exponentiation with linear asymptotic complexity (Θ(n)).
		:param base: Real number.
		:param exp: Natural number.
		:return: Result of the exponentiation.
		"""
		output = 1
		for i in range(0, exp):
			output = output * base

		return output

	@staticmethod
	def power_log(base, exp):
		"""
		Exponentiation with logarithmic asymptotic complexity (Θ(log n)).
		:param base: Real number.
		:param exp: Non-negative integer.
		:return: Result of the exponentiation.
		"""
		output = 1
		while exp > 0:
			if exp % 2 == 1:
				output = output * base

			base = base * base
			# exp = int(exp / 2)
			exp = exp // 2

		return output

	@staticmethod
	def power_negative(base, exp):
		"""
		Exponentiation, which works with negative numbers.
		:param base: Real number.
		:param exp: Integer.
		:return: Result of the exponentiation.
		"""
		if exp > 0:
			return Exponentiation.power_log(base, exp)
		else:
			return 1 / Exponentiation.power_log(base, -exp)

	@staticmethod
	def power_recursive(base, exp):
		"""
		Recursive exponentiation with linear asymptotic complexity (Θ(n)).
		:param base: Real number.
		:param exp: Non-negative integer.
		:return: Result of the exponentiation.
		"""
		if exp == 0:
			return 1
		else:
			return base * Exponentiation.power_recursive(base, exp - 1)

	@staticmethod
	def power_recursive_log(base, exp):
		"""
		Recursive exponentiation with logarithmic asymptotic complexity (Θ(log n)).
		:param base: Real number.
		:param exp: Non-negative integer.
		:return: Result of the exponentiation.
		"""
		if exp == 0:
			return 1

		if exp % 2 == 0:
			half = Exponentiation.power_recursive_log(base, exp / 2)
			return half * half
		# return power_recursive_log(base, exp / 2) * power_recursive_log(base, exp / 2)
		else:
			return base * Exponentiation.power_recursive_log(base, exp - 1)

	@staticmethod
	def power_real(base, exp):
		"""
		Real number exponentiation.
		:param base: Real number.
		:param exp: Real number.
		:return: Result of the exponentiation.
		"""
		return math.exp(exp * math.log(base))
		# return math.e ** (exp * math.log(base))

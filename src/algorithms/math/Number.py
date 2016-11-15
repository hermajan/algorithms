class Number:
	"""Methods for numbers."""

	@staticmethod
	def is_even(number):
		"""
		Checks if the number is even.
		:param number: Number.
		:return: True if is even, false if it is odd.
		"""
		return (number % 2 == 0)

	@staticmethod
	def is_odd(number):
		"""
		Checks if the number is odd.
		:param number: Number.
		:return: True if is odd, false if it is even.
		"""
		return (number % 2 != 0)

	@staticmethod
	def is_odd_bitwise(number):
		"""
		Checks if the number is odd bitwisely.
		:param number: Number.
		:return: True if is odd, false if it is even.
		"""
		return (number & 1)

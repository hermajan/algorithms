class Fibonacci:
	"""Implementations of the Fibonacci number."""

	@staticmethod
	def fib_iterative(index):
		"""
		Iterative algorithm for calculating the Fibonacci number.
		:param index: Index of a number in the Fibonacci sequence.
		:return: Fibonacci number.
		"""
		lower = 0
		higher = 1
		for i in range(1, index):
			tmp = lower + higher
			lower = higher
			higher = tmp

		return higher

	@staticmethod
	def fib_recursive(index):
		"""
		Recursive algorithm for calculating the Fibonacci number.
		:param index: Index of a number in the Fibonacci sequence.
		:return: Fibonacci number.
		"""
		if index <= 1:
			return index
		else:
			return Fibonacci.fib_recursive(index - 1) + Fibonacci.fib_recursive(index - 2)

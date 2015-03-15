class Matrix:
	@staticmethod
	def multiply(A, B):
		"""
		Multiplies two matrices.
		:param A: First matrix.
		:param B: Second matrix.
		:return: Multiplied matrix.
		"""
		m = len(A)
		o = len(B[0])
		n = len(A[0])
		C = [[0 for i in range(m)] for i in range(o)]
		for i in range(0, m):
			for j in range(0, o):
				C[i][j] = 0
				for k in range(0, n):
					C[i][j] = C[i][j] + A[i][k] * B[k][j]

		return C

	@staticmethod
	def transpose(matrix):
		"""
		Transpose rows and columns of matrix.
		:param: matrix: Matrix to transpose.
		:return: Transposed matrix.
		"""
		transposed = []
		for i in range(len(matrix[0])):
			transposed_row = []
			for row in matrix:
				transposed_row.append(row[i])
			transposed.append(transposed_row)
		return transposed

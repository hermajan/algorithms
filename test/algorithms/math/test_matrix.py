from unittest import TestCase
from src.algorithms.math.Matrix import Matrix


class TestMatrix(TestCase):
	def test_multiply(self):
		matrixA = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]]
		matrixB = [
			[1, 0, 0],
			[0, 1, 0],
			[0, 0, 1]]
		self.assertEqual(matrixA, Matrix.multiply(matrixA, matrixB))

		matrixC = [
			[30, 36, 42],
			[66, 81, 96],
			[102, 126, 150]]
		self.assertEqual(matrixC, Matrix.multiply(matrixA, matrixA))

	def test_transpose(self):
		matrix = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]]
		transposed = [
			[1, 4, 7],
			[2, 5, 8],
			[3, 6, 9]]
		self.assertEqual(transposed, Matrix.transpose(matrix))

		matrix2 = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12]]
		transposed2 = [
			[1, 5, 9],
			[2, 6, 10],
			[3, 7, 11],
			[4, 8, 12]]
		self.assertEqual(transposed2, Matrix.transpose(matrix2))

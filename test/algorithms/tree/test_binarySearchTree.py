from unittest import TestCase

from test.algorithms.Capturing import Capturing
from src.algorithms.tree.BinarySearchTree import Node
from src.algorithms.tree.BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(TestCase):
	def init_test_tree(self):
		tree = BinarySearchTree()

		nodes = [Node() for _ in range(7)]
		for i in range(7):
			nodes[i].key = i

		tree.root = nodes[3]

		tree.root.left = nodes[1]
		nodes[1].parent = tree.root
		nodes[1].left = nodes[0]
		nodes[0].parent = nodes[1]
		nodes[1].right = nodes[2]
		nodes[2].parent = nodes[1]

		tree.root.right = nodes[5]
		nodes[5].parent = tree.root
		nodes[5].left = nodes[4]
		nodes[4].parent = nodes[5]
		nodes[5].right = nodes[6]
		nodes[6].parent = nodes[5]

		return tree

	def test_insert(self):
		tree = BinarySearchTree()

		tree.insert(3)
		self.assertIsNotNone(tree.root)
		self.assertEqual(tree.root.key, 3)

		tree.insert(1)
		self.assertEqual(tree.root.left.key, 1)

		tree.insert(5)
		self.assertEqual(tree.root.right.key, 5)

		tree.insert(2)
		self.assertEqual(tree.root.left.right.key, 2)

		tree.insert(4)
		self.assertEqual(tree.root.right.left.key, 4)

	def test_search(self):
		tree = self.init_test_tree()

		node = tree.search(tree.root, 3)
		self.assertIsNotNone(node)
		self.assertEqual(node.key, 3)

		node = tree.search(tree.root, 7)
		self.assertIsNone(node)

	def test_delete(self):
		tree = self.init_test_tree()
		tree.delete(tree.root.left.left)

		self.assertEqual(tree.root.left.key, 1)
		self.assertIsNone(tree.root.left.left)

		tree.delete(tree.root)
		self.assertIsNotNone(tree.root)
		self.assertEqual(tree.root.key, 4)
		self.assertEqual(tree.root.left.key, 1)
		self.assertIsNone(tree.root.left.left)

		tree.delete(tree.root.left)
		self.assertEqual(tree.root.left.key, 2)

	def test_transplant(self):
		# tested in test_delete()
		self.test_delete()

	def test_minimum(self):
		tree = self.init_test_tree()

		node = None
		self.assertIsNone(tree.minimum(node))
		self.assertEqual(tree.minimum(tree.root).key, 0)

	def test_maximum(self):
		tree = self.init_test_tree()

		node = None
		self.assertIsNone(tree.maximum(node))
		self.assertEqual(tree.maximum(tree.root).key, 6)

	def test_height(self):
		tree = self.init_test_tree()

		self.assertEqual(tree.height(tree.root), 3)

		n = Node()
		n.key = 1
		tree.root.left.right.left = n
		n.parent = tree.root.left.right
		self.assertEqual(tree.height(tree.root), 4)

	def test_is_correct_bst(self):
		tree = self.init_test_tree()

		self.assertTrue(tree.is_correct_bst())

		tree.root.key = 0
		tree.root.left.left = None
		self.assertFalse(tree.is_correct_bst())

		tree.root.key = 3
		tree.root.left.right.key = 4
		tree.root.right.left.key = 2
		self.assertFalse(tree.is_correct_bst())

	def test_check_tree(self):
		# tested in test_is_correct_bst()
		self.test_is_correct_bst()

	def test_pre_order_print(self):
		tree = self.init_test_tree()
		#tree.pre_order_print(tree.root)

		with Capturing() as output:
			tree.pre_order_print(tree.root)
		result = list(map(int, output))

		self.assertListEqual(result, [3, 1, 0, 2, 5, 4, 6])

	def test_in_order_print(self):
		tree = self.init_test_tree()
		#tree.in_order_print(tree.root)

		with Capturing() as output:
			tree.in_order_print(tree.root)
		result = list(map(int, output))

		self.assertListEqual(result, [0, 1, 2, 3, 4, 5, 6])

	def test_post_order_print(self):
		tree = self.init_test_tree()
		#tree.post_order_print(tree.root)

		with Capturing() as output:
			tree.post_order_print(tree.root)
		result = list(map(int, output))

		self.assertListEqual(result, [0, 2, 1, 4, 6, 5, 3])

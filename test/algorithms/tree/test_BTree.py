from unittest import TestCase

from src.algorithms.tree.BTree import Node, BTree
from test.algorithms.Capturing import Capturing


def create_node(keys, children, leaf):
	node = Node()
	node.children = children
	node.keys = keys
	node.leaf = leaf
	node.n = len(keys)
	return node


def init_test_tree():
	tree = BTree()
	tree.arity = 4

	n12 = create_node([55, 75], [], True)
	n11 = create_node([25], [], True)
	n10 = create_node([17], [], True)
	n9 = create_node([14, 15], [], True)
	n8 = create_node([9, 10, 12], [], True)
	n7 = create_node([6, 7], [], True)
	n6 = create_node([3], [], True)
	n5 = create_node([0, 1], [], True)
	n4 = create_node([16, 18, 50], [n9, n10, n11, n12], False)
	n3 = create_node([8], [n7, n8], False)
	n2 = create_node([2], [n5, n6], False)
	n1 = create_node([5,13], [n2, n3, n4], False)

	tree.root = n1
	tree.height = 2

	return tree


class TestBTree(TestCase):
	def test_in_order_print(self):
		tree = init_test_tree()
		#tree.in_order_print(tree.root)

		with Capturing() as output:
			tree.in_order_print(tree.root)
		result = list(map(int, output))

		self.assertListEqual(result,
			[0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 25, 50, 55, 75])

	def test_pre_order_print(self):
		tree = init_test_tree()
		#tree.pre_order_print(tree.root)

		with Capturing() as output:
			tree.pre_order_print(tree.root)
		result = list(map(int, output))

		self.assertListEqual(result,
			[5, 13, 2, 0, 1, 3, 8, 6, 7, 9, 10, 12, 16, 18, 50, 14, 15, 17, 25, 55, 75])


	def test_post_order_print(self):
		tree = init_test_tree()
		#tree.post_order_print(tree.root)

		with Capturing() as output:
			tree.post_order_print(tree.root)
		result = list(map(int, output))

		self.assertListEqual(result,
			[0, 1, 3, 2, 6, 7, 9, 10, 12, 8, 14, 15, 17, 25, 55, 75, 16, 18, 50, 5, 13])

	def test_search(self):
		tree = init_test_tree()

		node = tree.search(tree.root, 15)
		self.assertIsNotNone(node)
		self.assertIn(15, node.keys)

		node = tree.search(tree.root, 19)
		self.assertIsNone(node)

	def test_is_equiv(self):
		tree1 = init_test_tree()
		tree2 = init_test_tree()
		self.assertTrue(tree1.is_equiv(tree2))

		tree2.insert(8)
		self.assertFalse(tree1.is_equiv(tree2))

	def test_insert(self):
		tree = BTree()
		tree.arity = 4

		tree.insert(1)
		self.assertIsNotNone(tree.root)
		self.assertListEqual(tree.root.keys, [1], "Inserting to empty B-Tree order 2.")

		tree.insert(7)
		tree.insert(2)
		self.assertIsNotNone(tree.root)
		self.assertListEqual(tree.root.keys, [1, 2, 7], "Inserting to B-Tree without splitting.")

		tree.insert(5)
		self.assertIsNotNone(tree.root)
		msg = "Inserting to B-Tree with splitting of root."
		self.assertListEqual(tree.root.keys, [2], msg)
		self.assertListEqual(tree.root.children[0].keys, [1], msg)
		self.assertListEqual(tree.root.children[1].keys, [5, 7], msg)

		tree.insert(12)
		tree.insert(8)
		self.assertIsNotNone(tree.root)
		msg = "Inserting to B-Tree with splitting of leaf."
		self.assertListEqual(tree.root.keys, [2, 7], msg)
		self.assertListEqual(tree.root.children[0].keys, [1], msg)
		self.assertListEqual(tree.root.children[1].keys, [5], msg)
		self.assertListEqual(tree.root.children[2].keys, [8, 12], msg)

	def test_insert_non_full(self):
		# tested in test_insert()
		self.test_insert()

	def test_split(self):
		# tested in test_insert()
		self.test_insert()

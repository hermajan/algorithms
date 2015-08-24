class Node:
	def __init__(self):
		"""
		key: Key of node.
		parent: Reference to parent node.
		left: Reference to left child node.
		right: Reference to right child node.
		"""
		self.key = 0
		self.parent = None
		self.right = None
		self.left = None


class BinarySearchTree:
	def __init__(self):
		"""
		root: Node which is root of tree.
		"""
		self.root = None

	def insert(tree, key):
		"""
		Inserts key to the tree.
		:param tree: Tree where to insert.
		:param key: Key which will be inserted.
		"""
		tmp = None
		roo = tree.root
		while roo is not None:
			tmp = roo
			if key < roo.key:
				roo = roo.left
			else:
				roo = roo.right

		new = Node()
		new.key = key
		new.parent = tmp
		if tmp is None:
			tree.root = new
		else:
			if new.key < tmp.key:
				tmp.left = new
			else:
				tmp.right = new

	def search(tree, node, key):
		"""
		Searches for key in tree starting from node.
		:param tree: Tree where to search.
		:param node: Node where searching will be started.
		:param key: Key which will be searched.
		:return: Node with searched key, if key isn't in tree then returns None.
		"""
		if node is None:
			return None
		if node.key is key:
			return node
		if key < node.key:
			return tree.search(node.left, key)
		else:
			return tree.search(node.right, key)

	def delete(tree, node):
		"""
		Deletes node from tree.
		:param tree: Tree where to delete.
		:param node: Node which will be deleted.
		"""
		if node.left is None:
			tree.transplant(node, node.right)
		elif node.right is None:
			tree.transplant(node, node.left)
		else:
			mini = tree.minimum(node.right)
			if mini.parent is not node:
				tree.transplant(mini, mini.right)
				mini.right = node.right
				mini.right.parent = mini

			tree.transplant(node, mini)
			mini.left = node.left
			mini.left.parent = mini

	def transplant(tree, first, second):
		"""
		Replaces first sub root with second sub root in tree.
		:param tree: Tree where to replace.
		:param first: First sub root.
		:param second: Second sub root.
		"""
		if first.parent is None:
			tree.root = second
		elif first.parent.left is first:
			first.parent.left = second
		else:
			first.parent.right = second
		if second is not None:
			second.parent = first.parent

	def minimum(self, node):
		"""
		Searches for minimum of tree.
		:param node: Node where searching will be started.
		:return: Node with minimum.
		"""
		if node is None:
			return None

		while node.left is not None:
			node = node.left
		return node

	def maximum(self, node):
		"""
		Searches for maximum of tree.
		:param node: Node where searching will be started.
		:return: Node with maximum.
		"""
		if node is None:
			return None

		while node.right is not None:
			node = node.right
		return node

	def height(tree, node):
		"""
		Returns height of tree starting from node.
		:param node: Node where counting height will be started.
		:return: Height of tree.
		"""
		if node is None:
			return 0
		return 1 + max(tree.height(node.left), tree.height(node.right))

	def is_correct_bst(tree):
		"""
		Checks if tree is correct binary search tree.
		:param tree: Tree to check.
		:return: If tree is correct binary search tree returns True, False otherwise.
		"""
		if tree is not None:
			return tree.check_tree(tree.root, tree.minimum(tree.root), tree.maximum(tree.root))
		else:
			return False

	def check_tree(self, node, mini, maxi):
		"""
		Checks if tree is correct binary search tree starting from node.
		:param node: Node where checking will be started.
		:param mini: Node with minimal value.
		:param maxi: Node with maximal value.
		:return:
		"""
		if node is None:
			return True
		elif node.key < mini.key or node.key > maxi.key:
			return False

		return self.check_tree(node.left, mini, node) and self.check_tree(node.right, node, maxi)

	def pre_order_print(tree, node):
		"""
		Prints tree pre order starting from node.
		:param tree: Tree to print.
		:param node: Node where printing will be started.
		"""
		if node is not None:
			print(node.key, sep=" ", end=" ")
			tree.pre_order_print(node.left)
			tree.pre_order_print(node.right)

	def in_order_print(tree, node):
		"""
		Prints tree in order starting from node.
		:param tree: Tree to print.
		:param node: Node where printing will be started.
		"""
		if node is not None:
			tree.in_order_print(node.left)
			print(node.key, sep=" ", end=" ")
			tree.in_order_print(node.right)

	def post_order_print(tree, node):
		"""
		Prints tree post order starting from node.
		:param tree: Tree to print.
		:param node: Node where printing will be started.
		"""
		if node is not None:
			tree.post_order_print(node.left)
			tree.post_order_print(node.right)
			print(node.key, sep=" ", end=" ")

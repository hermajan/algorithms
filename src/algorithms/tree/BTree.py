from test.algorithms.Capturing import Capturing


class Node:
	def __init__(self):
		"""
		keys: Keys of node.
		children: Reference to child nodes.
		leaf: True if node is leaf, False otherwise.
		n: Number of keys in node.
		"""
		self.keys = []
		self.children = []
		self.leaf = False
		self.n = 0


class BTree:
	def __init__(self):
		"""
		arity: Number of maximal child nodes.
		root: Node which is root of tree.
		height: Height of tree.
		"""
		self.arity = 0
		self.root = None
		self.height = 0

	def in_order_print(tree, node):
		"""
		Prints tree in order starting from node.
		:param tree: Tree to print.
		:param node: Node where printing will be started.
		"""
		if node is not None:
			if node.children == []:
				for key in node.keys:
					print(key, sep=" ", end=" ")
			for i, child in enumerate(node.children):
				tree.in_order_print(child)
				if i < len(node.keys):
					print(node.keys[i])

	def pre_order_print(tree, node):
		"""
		Prints tree pre order starting from node.
		:param tree: Tree to print.
		:param node: Node where printing will be started.
		"""
		if node is not None:
			for key in node.keys:
				print(key, sep=" ", end=" ")

			for child in node.children:
				tree.pre_order_print(child)

	def post_order_print(tree, node):
		"""
		Prints tree post order starting from node.
		:param tree: Tree to print.
		:param node: Node where printing will be started.
		"""
		if node is not None:
			for child in node.children:
				tree.post_order_print(child)

			for key in node.keys:
				print(key, sep=" ", end=" ")

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

		i = 0
		while i < node.n and key > node.keys[i]:
			i += 1

		if i < node.n and node.keys[i] is key:
			return node

		if node.leaf:
			return None
		else:
			return tree.search(node.children[i], key)

	def is_equiv(tree1, tree2):
		"""
		Checks if 2 trees are equivalent.
		:param tree1: First tree to check.
		:param tree2: Second tree to check.
		:return: If trees are equivalent returns True, False otherwise.
		"""
		if tree1.arity is not tree2.arity:
			return False
		if tree1.height is not tree2.height:
			return False

		with Capturing() as output:
			tree1.post_order_print(tree1.root)
		t1 = list(map(int, output))

		with Capturing() as output:
			tree2.post_order_print(tree2.root)
		t2 = list(map(int, output))

		if t1 != t2:
			return False

		return True

	def insert(tree, key):
		"""
		Inserts key to the tree.
		:param tree: Tree where to insert.
		:param key: Key which will be inserted.
		"""
		new = Node()

		if tree.root is None:
			new.leaf = True
			tree.insert_non_full(new, key)
			tree.root = new
			tree.height = 1
			return

		node = tree.root
		if len(node.keys) is tree.arity - 1:
			tree.root = new
			tree.height += 1
			new.children = [node]
			tree.split(new, 0)
			tree.insert_non_full(new, key)
		else:
			tree.insert_non_full(node, key)

	def insert_non_full(tree, node, key):
		i = 0
		while i < len(node.keys) and key > node.keys[i]:
			i += 1

		if node.leaf:
			node.keys.insert(i, key)

		else:
			if len(node.children[i].keys) is tree.arity - 1:
				tree.split(node, i)
				if key > node.keys[i]:
					i += 1
			tree.insert_non_full(node.children[i], key)

	def split(tree, node, index):
		"""
		Splits node in tree.
		:param tree: Tree where to split.
		:param node: Node where to split.
		:param index: Index of element in node for splitting.
		"""
		t = tree.arity // 2
		z = Node()
		y = node.children[index]
		node.children.insert(index+1, z)
		node.keys.insert(index, y.keys[t-1])

		z.leaf = y.leaf
		z.keys = y.keys[t:]
		y.keys = y.keys[:t-1]

		if not y.leaf:
			z.children = y.children[t:]
		y.children = y.children[:t]

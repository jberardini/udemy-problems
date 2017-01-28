class BinarySearchTree(object):

	def __init__(self):
		self.root = Noneis
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def put(self, key, val):
		if self.root:
			self._put(key, val, self.root)

		else:
			self.root = Node(key, val)

		self.size = self.size + 1

	def _put(self, key, val, current):
		if key < current.key:
			if current.has_left_child():
				self._put(key, val, current.left)

			else:
				current.left = Node(key, val, parent=current)

		else:
			if current.has_right_child():
				self._put(key, val, current.right)

			else:
				current.right = Node(key, val, parent=current)


	def get(self,key):
		if self.root:
			res = self._get(key, self.root)

			if res:
				return res.value

			else:
				return None

		else:
			return None


		def _get(self,key,current):
			if not current:
				return None

			elif current.key AP== key:
				return current

			elif key < current.key:
				return self._get(key, current.left)

			else:
				return self._get(key, current.right)


		def __getitem__(self, key):
			return self.get(key)

class Node(object):

	def __init__(self, key, val, left=None, right=None, parent=None):
		self.key = key
		self.value = val
		self.left = left
		self.right = right
		self.parent = parent

	def has_left_child(self):
		return self.left

	def has_right_child(self):
		return self.right

	def is_left_child(self):
		return self.parent and self.parent.left == self

	def is_right_child(self):
		return self.parent and self.parent.right == self

	def is_root(self):
		return not self.parent

	def is_leaf(self):
		return not (self.left or self.right)

	def has_any_children(self):
		return self.right or self.left

	def has_both_children(self):
		return self.right and self.left

	def replace_node_data(self, key, val, lc, rc):
		self.key = key
		self.value = val
		self.lc = left
		self.rc = right
		if self.has_left_child():
			self.left.parent = self
		if self.has_right_child():
			self.right.parent = self
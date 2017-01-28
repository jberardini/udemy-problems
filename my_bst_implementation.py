class Node(object):
	def __init__(self, value, parent=None):
		self.value = value
		self.parent = parent
		self.left = None
		self.right = None

	def __repr__(self):
		return "<Node value = {}>".format(self.value)


class BST(object):
	def __init__(self, root=None):
		self.root = root

	def print_nodes(self, node):
		if node:
			print node
			self.print_nodes(node.left)
			self.print_nodes(node.right)


def print_tree(tree):

	to_visit = [tree.root]
	current_count, next_count = 1, 0

	while to_visit:
		current = to_visit.pop(0)
		current_count -= 1
		print current.value,

		if current.left:
			to_visit.append(current.left)
			next_count += 1
		if current.right:
			to_visit.append(current.right)
			next_count += 1

		if current_count == 0:
			print '\n',
			next_count, current_count = current_count, next_count


one = Node(49)

two = Node(46, one)
one.left = two
three = Node(52, one)
one.right = three
four = Node(41, two)
two.left = four
five = Node(47, two)
two.right = five
my_bst = BST(one)
three.right = Node(55, three)
# print my_bst.root
# my_bst.print_nodes(one)

print_tree(my_bst)
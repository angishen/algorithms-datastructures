import collections

class BinaryTreeNode(object):
	def __init__(self, data=None, left=None, right=None, parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

# 9.1 TEST IF A BINARY TREE IS HEIGHT BALANCED
def is_height_balanced(root):
	def get_max_height(root):
		if not root:
			return 0
		return max(get_max_height(root.left) + 1, 
				   get_max_height(root.right) + 1)

	if not root:
		return True
	return abs(get_max_height(root.left) - get_max_height(root.right)) <= 1

def is_balanced_binary_tree_BOOK(tree):
	BalancedStatusWithHeight = collections.namedtuple(
		'BalancedStatusWithHeight', ('balanced', 'height'))

	# First value of the return value indicates if the tree is balanced, and if 
	# balanced, the second value of the return value is the height of the tree.
	def check_balanced(tree):
		if not tree:
			return BalancedStatusWithHeight(True, -1)  # base case

		left_result = check_balanced(tree.left)
		if not left_result.balanced:
			# left subtree is not balanced
			return BalancedStatusWithHeight(False, 0)

		right_result = check_balanced(tree.right)
		if not right_result.balanced:
			# right subtree is not balanced
			return BalancedStatusWithHeight(False, 0)

		isBalanced = abs(left_result.height - right_result.height) <= 1
		height = max(left_result.height, right_result.height) + 1
		return BalancedStatusWithHeight(is_balanced, height)

	return check_balanced(tree).balanced

# 9.2 TEST IF A BINARY TREE IS SYMMETRIC
def is_tree_symmetric(tree):
	def is_symmetric(left, right):
		if not tree:
			return True
		elif not tree.left and not tree.right:
			return True
		elif tree.left and tree.right:
			return (tree.left.data == tree.right.data and 
					is_symmetric(tree.left.left, tree.right.right) and
					is_symmetric(tree.left.right, tree.right.left))
		return False
	return is_symmetric(tree.left, tree.right)

def is_symmetric_BOOK(tree):
	def check_symmetric(subtree_0, subtree_1):
		if not subtree_0 and not subtree_1:
			return True
		elif subtree_0 and subtree_1:
			return (subtree_0.data == subtree_1.data and 
					check_symmetric(subtree_0.left, subtree_1.right) and
					check_symmetric(subtree_0.right, subtree_1.left))
		return False
	return not tree or check_symmetric(tree.left, tree.right)

# 9.3 COMPUTE THE LOWEST COMMON ANCESTOR IN A BINARY TREE
def lca(tree, node0, node1):
	Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

	def lca_helper(tree, node0, node1):
		if not tree:
			return Status(0, None)

		left_result = lca_helper(tree.left, node0, node1)
		if left_result.num_target_nodes == 2:
			return left_result

		right_result = lca_helper(tree.right, node0, node1)
		if right_result.num_target_nodes == 2:
			return right_result

		num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes +
							int(tree is node0) + int(tree is node1))
		return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

	return lca_helper(tree, node0, node1).ancestor

# COMPUTE LCA WHEN NODES HAVE PARENT POINTERS
def lca_with_parents(node0, node1):
	node_hash = {}
	while node0:
		node_hash[node0] = True
		node0 = node0.parent
	while node1:
		if node1 in node_hash:
			return node1.data
		node1 = node1.parent
	return None

def lca_with_parents_BOOK(node0, node1):
	def get_depth(node):
		depth = 0
		while node:
			depth += 1 
			node = node.parent
		return depth

		depth_0, depth_1 = get_depth(node0), get_depth(node1)
		if depth_1 > depth_0:
			depth_0, depth_1 = depth_1, depth_0

		depth_diff = abs(depth_0 - depth_1)
		while depth_diff:
			node0 = node0.parent
			depth_diff -= 1

		while node0 is not node1:
			node0, node1 = node0.parent, node1.parent

		return node0

def main():
	node8 = BinaryTreeNode(8)
	node7 = BinaryTreeNode(7)
	node6 = BinaryTreeNode(6, node7)
	node5 = BinaryTreeNode(5, right=node6)
	node4 = BinaryTreeNode(4)
	node3 = BinaryTreeNode(3, node4, node5)
	node2 = BinaryTreeNode(2, node3)
	root = BinaryTreeNode(1, node2, node8)

	node7.parent = node6
	node6.parent = node5
	node5.parent = node3
	node4.parent = node3
	node3.parent = node2
	node2.parent = root
	node8.parent = root

	print(lca_with_parents(node4, node7))

	# node9 = BinaryTreeNode(9)
	# node8 = BinaryTreeNode(8)
	# node4 = BinaryTreeNode(4, node8, node9)
	# node5 = BinaryTreeNode(5)
	# node2 = BinaryTreeNode(2, node4, node5)
	# root = BinaryTreeNode(1, node2)

	# print(is_height_balanced(root))

main()
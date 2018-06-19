from ch07_linkedlists import ListNode, print_list_nodes

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

# 9.4 COMPUTE LCA WHEN NODES HAVE PARENT POINTERS
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

# 9.5 SUM THE ROOT TO LEAF PATHS IN A BINARY TREE
def sum_root_to_leaf_BOOK(tree, partial_path_sum=0):
	if not tree:
		return 0
	partial_path_sum = partial_path_sum * 2 + tree.data
	if not tree.left and not tree.right:
		return partial_path_sum
	return (sum_root_to_leaf(tree.left, partial_path_sum) +
			sum_root_to_leaf(tree.right, partial_path_sum))

# 9.6 FIND A ROOT TO LEAF PATH WITH A SPECIFIED SUM
def has_specified_sum(tree, int):
	def check_path_sum(tree, int, path_sum=0):
		if not tree: 
			return False
		if not tree.left and not tree.right:
			return path_sum == int
		return (check_path_sum(tree.left, int, path_sum) or 
			   check_path_sum(tree.right, int, path_sum))
	return check_path_sum(tree, int, path_sum=0)

def has_path_sum_BOOK(tree, remaining_weight):
	if not tree:
		return False
	if not tree.left and not tree.right:
		return tree.data == remaining_weight
	return (has_path_sum_BOOK(tree.left, remaining_weight-tree.data) or 
			has_path_sum_BOOK(tree.right, remaining_weight-tree.data))

# 9.7 IMPLEMENT IN ORDER TRAVERSAL WITHOUT RECURSION
def inorder_iterative(tree):
	result = []
	stack = []
	while tree or stack:
		if tree:
			stack.append(tree)
			tree = tree.left
		else:
			tree = stack.pop()
			result.append(tree.data)
			tree = tree.right
	return result

def inorder_recursive(tree):
	result = []
	def in_order_helper(tree):
		if not tree:
			return
		in_order_helper(tree.left)
		result.append(tree.data)
		in_order_helper(tree.right)
	in_order_helper(tree)
	return result

# 9.8 IMPLEMENT PRE ORDER TRAVERSAL WITHOUT RECURSION
def preorder_iterative(tree):
	result = []
	stack = [tree]
	while stack:
		curr = stack.pop()
		if curr:
			result.append(curr.data)
			stack.extend([curr.right, curr.left])
	return result

def preorder_recursive(tree):
	result = []
	def preorder_helper(tree):
		if not tree:
			return
		result.append(tree.data)
		preorder_helper(tree.left)
		preorder_helper(tree.right)
	preorder_helper(tree)
	return result

# 9.9 COMPUTE THE KTH NODE IN AN IN-ORDER TRAVERSAL
def find_kth_node_binary_tree_BOOK(tree, k):
	while tree:
		left_size = tree.left.size if tree.left else 0
		if left_size + 1 < k: # kth node must be in right subtree of tree
			k -= left_size + 1
			tree = tree.right
		elif left_size == k - 1: # k is the iter itself
			return tree
		else: # kth node must be in left subtree of tree
			tree = tree.left
	return None # if k is between 1 and the tree size, this is unreachable

# 9.10 COMPUTE THE SUCCESSOR
def find_successor(node):
	if node.right:
		node = node.right
		while node:
			node = node.left
		return node

	while node.parent and node.parent.right is node:
		node = node.parent

	return node.parent

# 9.11 IMPLEMENT AN IN ORDER TRAVERSAL WITH O(1) SPACE
def inorder_traversal_o1space(tree):
	# this doesn't work
	result = []
	while tree:
		while tree.left:
			tree = tree.left
		result.append(tree.data)
		tree = tree.parent
		result.append(tree.data)
		if tree.right:
			tree = tree.right
		else:
			while tree.parent and tree.parent.right is tree:
				tree = tree.parent
			tree = tree.parent
	return result

def inorder_traversal_o1space_BOOK(tree):
	prev, result = None, []
	while tree:
		if prev is tree.parent:
			if tree.left:
				next = tree.left
			else:
				result.append(tree.data)
				next = tree.right or tree.parent
		elif tree.left is prev:
			result.append(tree.data)
			next = tree.right or tree.parent
		else:
			next = tree.parent
		prev, tree = tree, next
	return result

# 9.12 RECONSTRUCT A BINARY TREE FROM TRAVERSAL DATA
def binary_tree_from_preorder_inorder(preorder, inorder):
	node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

	def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
												 inorder_start, inorder_end):
		if preorder_end <= preorder_start or inorder_end <= inorder_start:
			return None

		root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
		left_subtree_size = root_inorder_idx - inorder_start

		return BinaryTreeNode(
			preorder[preorder_start],
			binary_tree_from_preorder_inorder_helper(
				preorder_start + 1, preorder_start + 1 + left_subtree_size,
				inorder_start, root_inorder_idx),
			binary_tree_from_preorder_inorder_helper(
				preorder_start + 1 + left_subtree_size, preorder_end,
				root_inorder_idx + 1, inorder_end))

	return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))

# 9.13 RECONSTRUCT A BINARY TREE FROM A PREORDER TRAVERSAL WITH MARKERS
def reconstruct_preorder(preodrer):
	def reconstruct_preorder_helper(preorder_iter):
		subtree_key = next(preorder_iter)
		if subtree_key is None:
			return None

		left_subtree = reconstruct_preorder_helper(preorder_iter)
		right_subtree = reconstruct_preorder_helper(preorder_iter)
		return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

	return reconstruct_preorder_helper(iter(preorder))

# 9.14 FOM A LINEKD LIST FROM THE LEAVES OF A BINARY TREE
dummy_head = L = ListNode(0)
def leaf_nodes_to_linked_list(tree):

	if tree.left is None and tree.right is None:
		L.next = ListNode(tree.data)
		L = L.next
	leaf_nodes_to_linked_list(tree.left)
	leaf_nodes_to_linked_list(tree.right)
	return dummy_head.next

def create_list_of_leaves_BOOK(tree):
	if not tree:
		return []
	if not tree.left and not tree.right:
		return [tree.data]
	return create_list_of_leaves_BOOK(tree.left) + create_list_of_leaves_BOOK(tree.right)

def compute_tree_exterior(tree):
	left, right = [], []
	root = tree

	while tree.left is not None and tree.right is not None:
		left.append(tree.data)
		tree = tree.left

	tree = root 
	while tree.left is not None and tree.right is not None:
		right.append(tree.data)
		tree = tree.right

	tree = root
	bottom = create_list_of_leaves_BOOK(tree)

	return left + bottom + list(reversed(right))[:-1]

def exterior_binary_tree_BOOK(tree):
	def is_leaf(node):
		return not node.left and not node.right

	def left_boundary_and_leaves(subtree, is_boundary):
		if not subtree:
			return []
		return (([subtree] if is_boundary
				  or is_leaf(subtree) else []) + left_boundary_and_leaves(
				  subtree.left, is_boundary) + left_boundary_and_leaves(
				  subtree.right, is_boundary and not subtree.left))

	def right_boundary_and_leaves(subtree, is_boundary):
		if not subtree:
			return []
		return (right_boundary_and_leaves(subtree.left, is_boundary
										  and not subtree.right) +
				right_boundary_and_leaves(subtree.right, is_boundary) + 
				([subtree] if is_boundary or is_leaf(subtree) else []))

	return ([tree] + left_boundary_and_leaves(tree.left, is_boundary=True) + 
			right_boundary_and_leaves(tree.right, is_boundary=True)
			if tree else [])

# 9.16 COMPUTE THE RIGHT SIBLING TREE
def construct_right_sibling(tree):
	def populate_children_next_field(start_node):
		while start_node and start_node.left:
			# populate right child's next field
			start_node.left.next = start_node.right
			# populate right child's next field if iter is not the last node of the level
			start_node.right.next = start_node.next and start_node.next.left
			start_node = start_node.next

	while tree and tree.left:
		populate_children_next_field(tree)
		tree = tree.left


if __name__ == "__main__":
	node13 = BinaryTreeNode('m')
	node12 = BinaryTreeNode('l')
	node11 = BinaryTreeNode('k')
	node10 = BinaryTreeNode('j')
	node9 = BinaryTreeNode('i')
	# node8 = BinaryTreeNode('h')
	node7 = BinaryTreeNode('g', node12, node13)
	node6 = BinaryTreeNode('f')
	node5 = BinaryTreeNode('e', node10, node11)
	node4 = BinaryTreeNode('d', right=node9)
	node3 = BinaryTreeNode('c', node6, node7)
	node2 = BinaryTreeNode('b', node4, node5)
	root = BinaryTreeNode('a', node2, node3)

	print(compute_tree_exterior(root))

	# print(create_list_of_leaves_BOOK(root))
	# print_list_nodes(linked_list)
	# node2 = BinaryTreeNode(2)
	# node10 = BinaryTreeNode(10)
	# node8 = BinaryTreeNode(8, right=node2)
	# node6 = BinaryTreeNode(6, right=node10)
	# node5 = BinaryTreeNode(5)
	# node19 = BinaryTreeNode(19, node8)
	# node4 = BinaryTreeNode(4)
	# node12 = BinaryTreeNode(12, node5, node6)
	# node1 = BinaryTreeNode(1, node4, node19)
	# root = BinaryTreeNode(10, node1, node12)

	# print(inorder_iterative(root))
	# print(inorder_recursive(root))
	# print(preorder_iterative(root))
	# print(preorder_recursive(root))

	# print(has_path_sum_BOOK(root, 40))
	# print(has_specified_sum(root, 40))


	# node8 = BinaryTreeNode(8)
	# node7 = BinaryTreeNode(7)
	# node6 = BinaryTreeNode(6, node7)
	# node5 = BinaryTreeNode(5, right=node6)
	# node4 = BinaryTreeNode(4)
	# node3 = BinaryTreeNode(3, node4, node5)
	# node2 = BinaryTreeNode(2, node3)
	# root = BinaryTreeNode(1, node2, node8)

	# node7.parent = node6
	# node6.parent = node5
	# node5.parent = node3
	# node4.parent = node3
	# node3.parent = node2
	# node2.parent = root
	# node8.parent = root

	# print(lca_with_parents(node4, node7))

	# node9 = BinaryTreeNode(9)
	# node8 = BinaryTreeNode(8)
	# node4 = BinaryTreeNode(4, node8, node9)
	# node5 = BinaryTreeNode(5)
	# node2 = BinaryTreeNode(2, node4, node5)
	# root = BinaryTreeNode(1, node2)

	# print(is_height_balanced(root))

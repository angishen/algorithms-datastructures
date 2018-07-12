import collections
from sortedcontainers import SortedDict

class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

class TreeNodeWithParent(object):
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data, self.parent, self.left, self.right = data, parent, left, right

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

# 14.1 TEST IF A BINARY TREE SATISFIES THE BST PROPERTY
def is_bst(tree, left_max=float('inf'), right_min=float('-inf')):
    if tree is None:
        return True
    if tree.data > left_max or tree.data < right_min:
        return False
    return (is_bst(tree.left, tree.data, right_min) and
            is_bst(tree.right, left_max, tree.data))

def is_binary_tree_bst_BOOK(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst_BOOK(tree.left, low_range, tree.data) and
            is_binary_tree_bst_BOOK(tree.right, tree.data, high_range))

def is_binary_tree_bst_BOOK_2(tree):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))

    bfs_queue = collections.deque(
        [QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]
    return True

# 14.2 FIND THE FIRST KEYE GREATER THAN A GIVEN VALUE IN A BST
def first_greater_key(tree, value):
    smallest_greater_value = float('inf')
    while tree:
        if tree.data > value:
            smallest_greater_value = min(smallest_greater_value, tree.data)
            tree = tree.left
        else:
            tree = tree.right
    return smallest_greater_value if smallest_greater_value != float('inf') else -1

def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right
    return first_so_far

# 14.3 FIND THE K LARGEST ELEMENTS IN A BST
def k_largest_elements(tree, k):
    def inorder_traversal(tree):
        if not tree:
            return
        inorder_traversal(tree.left)
        sorted_keys.append(tree.data)
        inorder_traversal(tree.right)

    sorted_keys = []
    inorder_traversal(tree)
    return list(reversed(sorted_keys[len(sorted_keys)-k:]))

def find_k_largest_in_bst_BOOK(tree, k):
    def find_k_largest_in_bst_helper(tree):
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements

# 14.4 COMPUTE THE LCA IN A BST
def find_LCA(tree, node_0, node_1):
    if tree.data > node_1.data:
        return find_LCA(tree.left, node_0, node_1)
    if tree.data < node_0.data:
        return find_LCA(tree.right, node_0, node_1)
    if node_0.data < tree.data < node_1.data:
        return tree.data

def find_LCA_BOOK(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left
    return tree.data

# 14.5 RECONSTRUCT A BST FROM TRAVERSAL DATA
def tree_from_preorder_traversal(A):
    root = tree = TreeNodeWithParent(A[0])
    for i in range(len(A)-1):
        if A[i+1] < A[i]:
            tree.left = TreeNodeWithParent(A[i+1], tree)
            print("left", tree.left.data)
            tree = tree.left
        else:
            while tree.parent and tree.parent.right:
                tree = tree.parent
            tree.right = TreeNodeWithParent(A[i+1], tree)
            print("right", tree.right.data)
            tree = tree.right
    return root

# def rebuild_bst_from_preorder_BOOK(preorder_sequence):
#     if not preorder_sequence:
#         return None

#     transition_point = next(
#         (i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0], len(preorder_sequence))
#     return TreeNode(
#         preorder_sequence[0], 
#         rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
#         rebuild_bst_from_preorder(preorder_sequence[transition_point:]))

def rebuild_bst_from_preorder_BOOK_2(preorder_sequence):
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1

        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)

        return BinaryTreeNode(root, left_subtree, right_subtree)

    root_idx = [0]
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))

# 14.6 FIND THE CLOSEST ENTRIES IN THREE SORTED ARRAYS
# def find_closest_elements_in_sorted_arrays(sorted_arrays):
#     min_distance_so_far = float('inf')
#     iters = bintrees.RBTree()
#     for idx, sorted_array in enumerate(sorted_arrays):
#         it = iter(sorted_array)
#         first_min = next(it, None)
#         if first_min is not None:
#             iters.insert((first_min, idx), it)

#     while True:
#         min_value, min_idx = iters.min_key()
#         max_value = iters.max_key()[0]
#         min_distance_so_far = min(max_value - min_value, min_distance_so_far)
#         it = iters.pop_min()[1]
#         next_min = next(it, None)
#         if next_min is None:
#             return min_distance_so_far
#         iters.insert((next_min, min_idx), it)

def find_closest_elements(sorted_arrays):
    min_distance_so_far = float('inf')
    iters = SortedDict()
    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            iters.setdefault((first_min, idx), default=it)

    while True:
        min_value, min_idx = iters.peekitem(index=0)[0]
        max_value = iters.peekitem()[0][0]
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        it = iters.popitem(index=0)[1]
        next_min = next(it, None)
        if next_min is None:
            return min_distance_so_far
        iters.setdefault((next_min, min_idx), it)

# 14.7
# this one's dumb :(


if __name__ == "__main__":
    node11 = TreeNode(5)
    node10 = TreeNode(3)
    node9 = TreeNode(1)
    node8 = TreeNode(-1)
    node7 = TreeNode(12)
    node6 = TreeNode(8)
    node5 = TreeNode(4, node10, node11)
    node4 = TreeNode(0, node8, node9)
    node3 = TreeNode(10, node6, node7)
    node2 = TreeNode(2, node4, node5)
    root = TreeNode(6, node2, node3)

    sorted_arrays = [[5,10,15], [3,6,8,12,14], [8,16,24]]
    print(find_closest_elements(sorted_arrays))
    # traversal_order = [8,4,2,1,3,6,5,7,12,10,9,11,14,13,15]
    # tree = tree_from_preorder_traversal(traversal_order)
    # print(preorder_recursive(tree))

    # print(find_LCA(root, node8, node7))
    # print(find_LCA_BOOK(root, node8, node7))

    # print(k_largest_elements(root, 3))
    # print(find_k_largest_in_bst_BOOK(root, 3))

    # print(first_greater_key(root, -1))
    # print(find_first_greater_than_k(root, -1))

    # print(is_bst(root))
    # print(is_binary_tree_bst_BOOK(root))
    # print(is_binary_tree_bst_BOOK_2(root))

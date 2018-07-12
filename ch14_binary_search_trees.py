import collections

class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

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

    print(k_largest_elements(root, 3))
    print(find_k_largest_in_bst_BOOK(root, 3))

    # print(first_greater_key(root, -1))
    # print(find_first_greater_than_k(root, -1))

    # print(is_bst(root))
    # print(is_binary_tree_bst_BOOK(root))
    # print(is_binary_tree_bst_BOOK_2(root))

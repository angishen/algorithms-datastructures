from math import sqrt
from itertools import product
import collections
# 15.1 TOWERS OF HANOI
def compute_towers_of_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0: 
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            print('Move from peg', from_peg, 'to peg', to_peg)
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg)

    NUM_PEGS = 3
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)

# 15.2 N QUEENS PROBLEM
# Example of recursive backtracking
def n_queens(n):
    def solve_n_queens(row):
        if row == n:
            result.append(list(col_placement))
            return
        for col in range(n):
            if all(abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result

# geeks for geeks solution
global N
N = 4

def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j])
            print()


# a utility function to check if a queen can be placed on board[row][col]
# not that this function is called when "col" queens are already placed
# in columns from 0 to col -1 so we need to check only left side for 
# attacking queens
def is_safe(board, row, col):
    # check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal on left side
    for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal on left side
    for i, j in zip(range(row,N,1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    # base case: if all queens are placd, then return true
    if col >= N:
        return True

    # consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of queens
            if solveNQUtil(board, col+1) == True:
                return True

            # if placing queen in board[i][col] doesn't 
            # lead to a slolution, then remove queen 
            # from board[i][col]
            board[i][col] = 0

    # if the queen can not be plaed in any row in this col
    # return False
    return False

def solveNQ():
    board = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# 15.3 GENERATE PERMUTATIONS
def permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return 
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutations(i+1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result

# A = [1,2,3]
# dp(i=0)
#     j=0
#         swap A[0], A[0] # A = [1,2,3]
#         dp(i=1)
#             j=1
#                 swap A[1], A[1] # A = [1,2,3]
#                 dp(i=2)
#                     result.append([1,2,3]) # result = [[1,2,3]]
#                 swap back A[1], A[1] # A [1,2,3]
#             j=2
#                 swap A[2], A[1] # A = [1,3,2]
#                 dp(i=2)
#                     result.append([1,3,2]) # result = [[1,2,3], [1,3,2]]
#                 swap back A[1], A[2] # A = [1,2,3]
#     j=1
#         swap A[1], A[0] # A = [2,1,3]
#         dp(i=2)
#             result.append([2,1,3]) # result = [[1,2,3], [1,3,2], [2,1,3]]
#         swap back A[1], A[0] # A = [1,2,3]
#     j=2
#         swap A[2], A[0] # A = [3,2,1]
#             result.append()



# 15.4 GENERATE THE POWER SET
def generate_power_set(input_set):
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(list(selected_so_far))
            return
        directed_power_set(to_be_selected + 1, selected_so_far)
        directed_power_set(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])

    power_set = []
    directed_power_set(0, [])
    return power_set

# dps(0, [])
#     dps(1, [])
#         dps(2, [])
#             dps(3, [])
#                 power_set.append([]) # power_set = [[]]
#             dps(3, [2])
#                 power_set.append([2]) # power_set = [[], [2]]
#         dps(2, [1])
#             dps(3, [1])
#                 power_set.append([1]) # power_set = [[], [2], [1]]
#             dps(3, [1,2])
#                 power_set(append([1,2])) # power_set = [[], [2], [1], [1,2]]
#     dps(1, [0])
#         dps(2, [0])
#             dps(3, [0])
#                 power_set.append([0]) # power_set = [[], [2], [1], [1,2], [0]]
#             dps(3, [0,2])
#                 power_set.append([0,2]) # power_set = [[], [2], [1], [1,2], [0], [0,2]]
#         dps(2, [0,1])
#             dps(3, [0,1])
#                 power_set.append([0,1]) # power_set = [[], [2], [1], [1,2], [0], [0,2], [0,1]]
#             dps(3, [0,1,2])
#                 power_set.append([0,1,2]) # power_set = [[], [2], [1], [1,2], [0], [0,2], [0,1], [0,1,2]]


# 15.5 GENERATE ALL SIUBSETS OF SIZE K
def combinations(n, k):
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(partial_combination)
            return

        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i+1, partial_combination + [i])
            i += 1

    result = []
    directed_combinations(1, [])
    return result

# n = 4, k = 2
# d_c(1, [])
#     num_remaining = 2, i = 1
#     d_c(2, [1])
#         num_remaining = 1, i = 2
#             d_c(3, [1,2])
#                 result.append([1,2]) # result = [[1,2]]
#             i += 1 # i = 3
#             d_c(4, [1,3])
#                 result.append([1,3]) # result = [[1,2], [1,3]]
#             i += 1 # i = 4
#             d_c(5, [1,4])
#                 result.append([1,4]) # result = [[1,2], [1,3], [1,4]]
#     i += 1 # i = 2
#     d_c(3, [2])
#         num_remaining = 1, i = 3
#             d_c(4, [2,3])
#                 result.append([2,3]) # result = [[1,2], [1,3], [1,4], [2,3]]
#             i += 1 # i = 4
#             d_c(5, [2, 4])
#                 result.append([2,4]) # result = [[1,2], [1,3], [1,4], [2,3], [2,4]]
#     i += 1 # i = 3
#     d_c(4, [3])
#         num_remaining = 1, i = 3
#             d_c(4, [3,4])
#                 result.append([3,4]) # result = [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]

# 15.6 GENERATE STRINGS OF MATCHED PARENS
def generate_balanced_parens(num_pairs):
    def directed_generate_balanced_parens(num_left_parens_needed,
                                          num_right_parens_needed,
                                          valid_prefix,
                                          result=[]):
        if num_left_parens_needed > 0:
            directed_generate_balanced_parens(num_left_parens_needed - 1,
                                              num_right_parens_needed,
                                              valid_prefix + "(")

        if num_left_parens_needed < num_right_parens_needed:
            directed_generate_balanced_parens(num_left_parens_needed,
                                              num_right_parens_needed - 1,
                                              valid_prefix + ")")

        if not num_right_parens_needed:
            result.append(valid_prefix)
        return result

    return directed_generate_balanced_parens(num_pairs, num_pairs, '')

# k = 2
# dgbp(2, 2, '', result=[])
#     dgbp(1, 2, '(', result=[])
#         dgbp(0, 2, '((', result=[])
#             dgbp(0, 1, '(()', result=[])
#                 dgbp(0, 0, '(())', result=[])
#                     result.append('(())')
#                 return result # result = ['(())']
#             return result # result = ['(())']
#         dgbp(1, 1, '()', result=['(())'])
#             dgbp(0, 1, '()(', result=['(())'])
#                 dgbp(0, 0, '()()', result=['(())'])
#                     result.append('()()')
#                 return result # result = result=['(())', '()()']
#             return result # result = result=['(())', '()()']
#         return result # result = result=['(())', '()()'] 
#     return result # result = result=['(())', '()()'] 

# 15.7 GENERATE PALINDROMIC DECOMPOSITIONS
def palindromic_decomposition(st):
    def directed_palindromic_decomposition(offset, partial_palindrome):
        if offset == len(st):
            result.append(partial_palindrome)
            return
        for i in range(offset, len(st)):
            prefix = st[i:offset]
            if is_palindrome(prefix):
                directed_palindromic_decomposition(i+len(prefix), partial_palindrome + [prefix])

    result = []
    directed_palindromic_decomposition(0, [])
    return result

def palindrome_partitioning(input):
    def directed_palindrome_partitioning(offset, partial_partition):
        if offset == len(input):
            result.append(partial_partition)
            return

        for i in range(offset+1, len(input)+1):
            prefix = input[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_partitioning(i, partial_partition + [prefix])
    
    result = []
    directed_palindrome_partitioning(0, [])
    return result

# 15.8 
def generate_all_binary_trees(num_nodes):
    if num_nodes == 0:
        return [None]

    result = []
    for num_left_tree_nodes in range(num_nodes):
        num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes
        left_subtrees = generate_all_binary_trees(num_left_tree_nodes)
        right_subtrees = generate_all_binary_trees(num_right_tree_nodes)
        result += [
            BinaryTreeNode(0, left, right) 
            for left in left_subtrees for right in right_subtrees]

# 15.9 IMPLEMENT A SUDOKU SOLVER
def sudoku_solver(partial_assignment):
    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment):
            i = 0
            j += 1
            if j == len(partial_assignment[i]):
                return True

        if partial_assignment[i][j] != EMPTY_ENTRY:
            return solve_partial_sudoku(i + 1, j)

        def valid_to_add(i, j, val):
            if any(val == partial_assignment[k][j]
                    for k in range(len(partial_assignment))):
                return False

            if val in partial_assignment[i]:
                return False

            region_size = int(sqrt(len(partial_assignment)))
            I = i // region_size
            J = j // region_size
            return not any(
                val == partial_assignment[region_size * I + a][region_size * J + b]
                for a, b in product(range(region_size), repeat=2))

        for val in range(1, len(partial_assignment) + 1):
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True

        partial_assignment[i][j] = EMPTY_ENTRY # undo assignment
        return False

    EMPTY_ENTRY = 0
    return solve_partial_sudoku(0,0)

# 15.11 COMPUTE THE DIAMETER OF A TREE
class TreeNode:
    def __init__(self):
        self.edges = []

Edge = collections.namedtuple('Edge', ('root', 'length'))

def compute_diameter(T):
    HeightAndDiameter = collections.namedtuple('HeightAndDiameter', ('height', 'diameter'))

    def compute_height_and_diameter(r):
        diameter = float('-inf')
        heights = [0.0, 0.0]
        for e in r.edges:
            h_d = compute_height_and_diameter(e.root)
            if h_d.height + e.length > heights[0]:
                heights = [h_d.height + e.length, heights[0]]
            elif h_d.height + e.length > heights[1]:
                heights[1] = h_d.height + e.length
            diameter = max(diameter, h_d.diameter)
        return HeightAndDiameter(heights[0], max(diameter, heights[0] + heights[1]))

    return compute_height_and_diameter(T).diameter if T else 0.0



if __name__ == "__main__":
    input = '61116'
    print(palindrome_partitioning(input))
    # print(combinations(4, 2))
    # nums = [1,2,3]
    # print(permutations(nums))
    # print(generate_power_set(nums))






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

if __name__ == "__main__":
    nums = [1,2,3]
    print(generate_power_set(nums))





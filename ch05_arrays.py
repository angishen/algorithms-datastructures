import random
import itertools
import bisect
import math 

# 5.1 DUTCH FLAG PARTITIONING
def DFP(pivot_idx, arr):
    pivot_val = arr[pivot_idx]
    sm_boundary = 0
    for i in range(len(arr)):
        if arr[i] < pivot_val:
            arr[i], arr[sm_boundary] = arr[sm_boundary], arr[i]
            sm_boundary += 1
    lg_boundary = len(arr)-1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < pivot_val:
            break
        if arr[i] > pivot_val:
            arr[i], arr[lg_boundary] = arr[lg_boundary], arr[i]
            lg_boundary -= 1

    return arr

def DFP_BOOK(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        print(smaller, equal, larger)
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -=1
            A[equal], A[larger] = A[larger], A[equal]
    return A

# 5.2 ADD 1 TO AN ABRITRARY PRECISION INTEGER
def add_one(arr):
    roll_over = True
    idx = len(arr) - 1
    while roll_over and idx >= 0:
        if arr[idx] < 9:
            roll_over = False
            arr[idx] += 1
        else:
            arr[idx] = 0
            idx -= 1
    if roll_over:
        arr[0] = 1
        arr.append(0)
    return arr

def add_one_BOOK(A):
    # add one to least significant digit
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        # if last digit isn't 10, don't need to carry over
        if A[i] != 10:
            break
        # if A[i] = 10, do a carry over
        A[i] = 0
        A[i-1] += 1
    # if most significant digit is 10, need to add extra 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

# 5.3 MULTIPLY TWO ABITRARY PRECISION INTEGERS
def carry_over(arr): # helper function for multiply function
    new_arr = []
    amt_to_carry = 0
    for idx, num in enumerate(reversed(arr)):
        num += amt_to_carry
        if num < 10:
            amt_to_carry = 0
            new_arr.append(num)
            continue
        new_arr.append(num % 10)
        amt_to_carry = num // 10
    if amt_to_carry > 0:
        new_arr.append(amt_to_carry)
    return new_arr

def multiply_two_arrays(arr1, arr2):
    results = []
    for i in reversed(range(len(arr1))):
        temp_result = []
        temp_result.extend([0 for i in range(len(arr1)-1)])
        for j in reversed(range(len(arr2))):
            temp_result.append(arr1[i]*arr2[j])
        print(temp_result)
        temp_result = carry_over(temp_result)
        print(temp_result)
        results.append(temp_result)
    return results
    
def multiply_BOOK(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num1))):
            result[i+j+1] += num1[i] * num2[i]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10

    result = result[next((i for i, x in enumerate(result) if x!=0), len(result)):] or [0]
    return [sign * result[0]] + result[:1]

# 5.4 ADVANCING THROUGH AN ARRAY
def advance(arr):
    farthest_reach, previous_step, current_idx = 0, 0, 0
    while farthest_reach < len(arr):
        max_steps = arr[current_idx]
        if current_idx + max_steps >= len(arr)-1:
            return True
        while max_steps > 0:
            if arr[current_idx + max_steps] > 0:
                if current_idx + max_steps > farthest_reach:
                    farthest_reach = current_idx + max_steps
                current_idx += max_steps
                previous_step = current_idx -1
                continue
            else:
                max_steps -= 1
        if max_steps <= 0 and previous_step >= 0:
            current_idx = previous_step
        else:
            return False
    return True

def can_reach_end_BOOK(A):
    furthest_reach_so_far, last_index = 0, len(A)-1
    i = 0
    while i < furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i]+i)
        i += 1
    return furthest_reach_so_far >= last_index

# 5.5 DELETE DUPLICATES FROM A SORTED ARRAY
def delete_duplicates(arr):
    if not arr:
        return 0
    first_elem = arr[0]
    arr[:] = [arr[i] for i in range(1, len(arr)) if arr[i] != arr[i-1]]
    return [first_elem] + arr

def delete_duplicates_BOOK(A):
    if not A:
        return None
    first_num = A[0]
    write_idx = 1
    for i in range(1, len(A)):
        if A[write_idx - 1] != A[i]:
            A[write_idx] = A[i]
            write_idx += 1
    return [first_num] + A

# 5.6 BUY AND SELL A STOCK ONCE
def buy_sell_stock_once(arr):
    min_idx = 0
    max_profit = 0
    for idx in range(len(arr)):
        if arr[idx] < arr[min_idx]:
            min_idx = idx
        max_profit = max(max_profit, arr[idx]-arr[min_idx])
    return max_profit

def buy_sell_stock_once_BOOK(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

# 5.7 BUY AND SELL A STOCK TWICE
# O(n^2) time complexity
def buy_sell_stock_twice(arr):
    total_max_profit = 0
    for i in range(len(arr)):
        max_profit1 = buy_sell_stock_once(arr[:i])
        max_profit2 = buy_sell_stock_once(arr[i:])
        total_max_profit = max(total_max_profit, max_profit1 + max_profit2)
    return total_max_profit

# O(n) time complexity
def buy_sell_stock_twice_BOOK(prices):
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we sell on that day
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    #  Backwards phase. For each day, find the maximum profit if we make the second buy on that day
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, 
                              (max_price_so_far - price) + first_buy_sell_profits[i-1])
    return max_total_profit

# 5.8 COMPUTE AN ALTERNATION
def compute_alternation(arr):
    for i in range(len(arr)-1):
        if i % 2 == 0:
            if arr[i+1] < arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
        else:
            if arr[i+1] > arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr

def compute_altneration_BOOK(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i % 2)

# 5.9 ENUMERATE ALL PRIMES TO N
def enumerate_primes(n):
    primes = []
    single_digit_primes = [2,3,5,7]
    for num in range(2,n+1):
        is_prime = True
        if num in single_digit_primes:
            primes.append(num)
            continue
        for prime in single_digit_primes:
            if num % prime == 0: 
                is_prime = False
        if is_prime:
            primes.append(num)
    return primes

# 5.10 PERMUTE THE ELEMENTS OF AN ARRAY
def apply_permutation(perm, arr):
    new_arr = [0] * len(arr)
    for i in range(len(perm)):
        new_arr[perm[i]] = arr[i]
    return new_arr

def apply_permutation_BOOK(perm, A):
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            print("i: " + str(i))
            print("perm[next]: " + str(perm[next]))
            print(A)
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
            print("temp: " + str(temp))
            print(perm)
    perm[:] = [a + len(perm) for a in perm]
    return A

# 5.11 COMPUTE THE NEXT PERMUTATION
def compute_next_perm(perm):
    min_so_far = perm[len(perm)-1]
    for i in reversed(range(len(perm))):
        print(i)
        if perm[i] < min_so_far:
            slice_to_rotate = perm[i:]
            return perm[:i] + slice_to_rotate[-1:] + slice_to_rotate[:-1]     
        min_so_far = min(perm[i], min_so_far)
    return []

def compute_next_perm_try2(perm):
    inversion_point = [perm[len(perm)-1], len(perm)-1]
    for i in reversed(range(len(perm))):
        if perm[i] < inversion_point[0]:
            perm[i], perm[inversion_point[1]] = perm[inversion_point[1]], perm[i] 
            return perm
        inversion_point[0] = min(perm[i], inversion_point[0])
        inversion_point[1] = i if perm[i] < inversion_point[0] else inversion_point[1]
    return []

def next_permutation_BOOK(perm):
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point+1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point+1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]

    perm[inversion_point+1:] = reversed(perm[inversion_point+1:])
    return perm

# 5.12 SMAPLE OFFLINE DATA
def sample_offline_data(arr, k):
    start_idx = random.randint(0,len(arr)-1)
    if start_idx + k < len(arr):
        return arr[start_idx : start_idx+k]
    return arr[start_idx:] + arr[:(k - len(arr[start_idx:]))]

def random_sampling_BOOK(k, A):
    for i in range(k):
        r = random.randint(i, len(A)-1)
        A[r], A[i] = A[i], A[r]
    return A[:k]

# 5.13 SAMPLE ONLINE DATA
def sample_online_data(arr, k):
    sample_list = []
    for val in arr:
        get_sample = random.randint(0,1)
        if get_sample == 1:
            if len(sample_list) < k:
                sample_list.append(val)
            else:
                sample_list[random.randint(0, k-1)] = val
            print(sample_list)
    return sample_list

def online_random_sampling(it, k):
    sampling_results = list(itertools.islice(it, k))

    num_seen_so_far = k
    for x in it:
        num_seen_so_far += 1
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    return sampling_results

# 5.14 COMPUTE RANDOM PERMUTATION

def random_permutation(n):
    used_num_hash = {}
    result_arr = [0] * (n)
    for i in range(n):
        num = random.randint(0,n-1)
        while num in used_num_hash:
            num = random.randint(0,n-1)
        used_num_hash[num] = True
        result_arr[num] = i
    return result_arr

def compute_random_permutation(n):
    permutation = list(range(n))
    random_sampling_BOOK(n, permutation)
    return permutation

# 5.15 COMPUTE RANDOM SUBSET

def random_subset(n, k):
    nums = list(range(n))
    for i in range(k):
        random_idx = random.randint(i, n-1)
        nums[i], nums[random_idx] = nums[random_idx], nums[i]
    return nums[:k]

def random_subset_BOOK(n, k):
    changed_elements = {}
    for i in range(k):
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]

# 5.16 GENERATE NON-UNIFORM RANDOM NUMBERS
def generate_nonuniform_num(A, p):
    cumulative_probs = []
    sum = 0
    for prob in p:
        sum += prob
        cumulative_probs.append(sum)
    rand_num = random.uniform(0,1)
    idx_to_use = 0
    for i in range(len(cumulative_probs)):
        if rand_num <= cumulative_probs[i]:
            idx_to_use = i
            break
    return A[idx_to_use]

def nonuniform_random_number_generation(values, probabilities):
    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
    return values[interval_idx]

# 5.17 SUDOKU SOLVER PROBLEM
def sudoku_checker(sudoku):
    def is_valid(subarray):
        return len(subarray) == 9 and sum(subarray) == sum(set(subarray))

    # check rows
    for row in sudoku:
        if not is_valid(row):
            return False

    # check columns
    for i in range(len(sudoku)):
        col = [row[i] for row in sudoku]
        if not is_valid(col):
            return False

    # check subarrays
    subgrids = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = list(itertools.chain(row[j:j+3]) for row in sudoku[i:i+3])
            if not is_valid(subgrid):
                print(i, j)
                print("subgrid")
                return False

    return True

def is_valid_sudoku_BOOK(partial_assignment):
    # return True if subarray
    # partial_assignment[start_row:end_row][start_col:end_col]
    # contains any duplications in {1,2.... len(partial_assignment)}
    # otherwise return false
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    #  check row and column constraints
    if any (
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or has_duplicate([partial_assignment[j][i] for j in range(n)])
        for i in range(n)):
            return False

    # check region constraints
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I+1))
        for b in range(region_size * J, region_size * (J+1))
    ])  for I in range(region_size) for J in range(region_size))

def spiral_ordering(arr):
    n = len(arr[0])
    layer = 0
    combined_i, combined_j = [], []
    for n in range(n, 0, -2):
        if n == 1: 
            i = n * [0]
        else:
            i = n * [0] + list(range(1,n-1)) + n * [n-1] + list(reversed(range(1,n-1)))
        i = list(map(lambda x: x+layer, i))
        j = i[(n-1):] + i[:(n-1)]
        combined_i.extend(i)
        combined_j.extend(j)
        layer += 1
    i_j_tuples = zip(combined_i, combined_j)
    results = []
    for tuple in i_j_tuples:
        results.append(arr[tuple[0]][tuple[1]])
    return results

def rotate_grid(grid):
    rotated_grid = []
    for i in range(len(grid)):
        col = [row[i] for row in grid]
        rotated_grid.append(col[::-1])
    return rotated_grid

def generate_pascals_triangle(n):
    pascals_triangle = [[1], [1,1]]
    for i in range(2,n):
        prev_row = pascals_triangle[-1]
        next_row = []
        next_row.append(1)
        for j in range(len(prev_row)-1):
            next_row.append(prev_row[j] + prev_row[j+1])
        next_row.append(1)
        pascals_triangle.append(next_row)
    return pascals_triangle

def main():
    # arr = [12,11,13,9,12,20]
    # print(buy_sell_stock_twice(arr))
    # print(buy_sell_stock_twice_BOOK(arr))
    # arr = [3,9,11,12,1,5,6,7]
    # print(compute_alternation(arr))
    # print(compute_alternation(arr))
    # print(enumerate_primes(100000))

    sudoku = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]
    
    spiral_array = [[10,11,12,13,14],
                    [15,16,17,18,19],
                    [20,21,22,23,24],
                    [25,26,27,28,29],
                    [30,31,32,33,34]]

    print(rotate_grid(spiral_array))

main()


    

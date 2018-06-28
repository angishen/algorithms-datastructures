import math
import collections
import random
import operator

# 11.1 SEARCH A SORTED ARRAY FOR THE FIRST OCCURANCE OF K
def find_first_k(arr, k):
	k_candidate_indices = []
	lo, hi = 0, len(arr)-1
	while lo <= hi:
		mid = (lo + hi) // 2
		if arr[mid] > k:
			hi = mid - 1
		elif arr[mid] < k:
			lo = mid + 1
		else:
			k_candidate_indices.append(mid)
			hi = mid - 1
	return k_candidate_indices[-1] if k_candidate_indices else -1

def search_first_of_k_BOOK(A, k):
	left, right, result = 0, len(A) -1, -1
	while left <= right:
		mid = (left + right) // 2
		if A[mid] > k:
			right = mid - 1 
		elif A[mid] == k:
			result = mid
			right = mid - 1
		else:
			left = mid + 1 
	return result

# 11.2 SEARCH A SROTED ARRAY FOR AN ENTRY EQUAL TO ITS INDEX
def find_entry_equal_to_idx(arr):
	lo, hi = 0, len(arr) - 1 
	while lo <= hi:
		mid = (lo + hi) // 2
		if arr[mid] > mid:
			hi = mid - 1
		elif arr[mid] == mid:
			return arr[mid]
		else:
			lo = mid + 1
	return -1 

def search_entry_equal_to_its_index(A):
	left, right = 0, len(A) - 1
	while left <= right:
		mid = (left + right) // 2
		difference = A[mid] - mid
		if difference == 0:
			return mid
		elif difference > 0:
			right = mid - 1 
		else:
			left = mid + 1 
	return - 1 

# 11.3 SEARCH A CYCLICALLY SORTED ARRAY
def smallest_in_cyclic_array(arr):
	lo, hi = 0, len(arr) - 1
	while lo < hi:
		mid = (lo + hi) // 2 
		if arr[hi] > arr[mid]:
			hi = mid
		else:
			lo = mid + 1 
	return lo

def search_smallest(A):
	left, right = 0, len(A) - 1
	while left < right:
		mid = (left + right) // 2
		if A[mid] > A[right]:
			left = mid + 1
		else:
			right = mid
	return left

# 11.4 COMPUTE THE INTEGER SQUARE ROOT
def int_square_root(n):
	prev_sqrt = 0
	if n == 0:
		return 0
	for num in range(0, n):
		if num ** 2 > n:
			return prev_sqrt
		prev_sqrt = num

def square_root_BOOK(k):
	left, right = 0, k
	while left <= right:
		mid = (left + right) // 2 
		mid_squared = mid * mid
		if mid_squared < k:
			left = mid + 1  
		else:
			right = mid - 1
	return left - 1 

# 11.5 COMPUTE THE REAL SQUARE ROOT
def real_square_root_BOOK(x):
	left, right = (x, 1.0) if x < 1.0 else (1.0, x)

	while not math.isclose(left, right):
		mid = 0.5 * (left + right)
		mid_squared = mid * mid
		if mid_squared > x:
			right = mid
		else:
			left = mid
	return left

# 11.6 SEARCH IN A 2D SORTED ARRAY
def search_2d_array(arr, k):
	row, col = 0, len(arr[0]) - 1 
	while col >= 0 and row < len(arr):
		if k > arr[row][col]:
			row += 1 
		elif k == arr[row][col]:
			return row, col
		else:
			col -= 1 
	return -1 

def matrix_search_BOOK(A, x):
	row, col = 0, len(A[0])-1
	while row < len(A) and col >= 0:
		if A[row][col] == x:
			return True
		elif A[row][col] < x:
			row += 1
		else:
			col -= 1
	return False 

# 11.7 COMPUTE THE MIN AND MAX SIMULTANEOUSLY
def get_min_max(arr):
	min, max = float('inf'), float('-inf')
	for val in arr:
		if val < min:
			min = val
		elif val > max:
			max = val
	return min, max

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))
def find_min_max_BOOK(A):
	def min_max(a, b):
		return MinMax(a, b) if a < b else MinMax(b, a)

	if len(A) <= 1 :
		return MinMax(A[0], A[0])

	global_min_max = min_max(A[0], A[1])
	for i in range(2, len(A)-1, 2):
		local_min_max = min_max(A[i], A[i+1])
		global_min_max = MinMax(
			min(global_min_max.smallest, local_min_max.smallest),
			max(global_min_max.largest, local_min_max.largest))

	if len(A) % 2:
		global_min_max = MinMax(
						min(global_min_max.smallest, A[-1]),
						max(global_min_max.largest, A[-1]))

	return global_min_max

# 11.8 FIND THE KTH LARGEST ELEMENT
def find_kth_largest(k, A):
	def find_kth(comp):
		def partition_around_pivot(left, right, pivot_idx):
			pivot_value = A[pivot_idx]
			new_pivot_idx = left
			A[pivot_idx], A[right] = A[right], A[pivot_idx]
			for i in range(left, right):
				if comp(A[i], pivot_value):
					A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
					new_pivot_idx += 1
			A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
			return new_pivot_idx

		left, right = 0, len(A) - 1
		while left <= right:
			pivot_idx = random.randint(left, right)
			new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
			if new_pivot_idx == k - 1:
				return A[new_pivot_idx]
			elif new_pivot_idx > k - 1:
				right = new_pivot_idx - 1
			else:
				left = new_pivot_idx + 1
	return find_kth(operator.gt)

def find_missing_ip_BOOK(stream):
	NUM_BUCKET = 1 << 16
	counter = [0] * NUM_BUCKET
	stream, stream_copy = itertools.tee(stream)
	for x in stream:
		upper_part_x = x >> 16
		counter[upper_part_x] += 1

	# look for a bucket that contains less than (1 << 16) elements
	BUCKET_CAPACITY = 1 << 16
	candidate_bucket = next(i for i, c in enumerate(counter)
						if c < BUCKET_CAPACITY)

	# finds all IP addresses in he stream whose first 16 bits are equal to
	# candidate_bucket
	candidates = [0] * BUCKET_CAPACITY
	stream = stream_copy
	for x in stream_copy:
		upper_part_x = x >> 16
		if candidate_bucket == upper_part_x:
			# records the presence of 16 LSB of x
			lower_part_x = ((1 << 16) - 1) & x
			candidates[lower_part_x] = 1

	# at least one of the LSB combinations is absent, find it
	for i, v in enumerate(candidates):
		if v == 0:
			return (candidate_bucket << 16) | i

# 11.10 FIND THE DUPLICATE AND MISSING ELEMENTS
def find_missing_and_duplicate(arr):
	nums_hash = {}
	for num in arr:
		if num not in nums_hash:
			nums_hash[num] = 1
		else:
			duplicate_num = num
	num_count = len(arr) - 1
	for i in range(num_count):
		if i not in nums_hash:
			missing_num = num
	return missing_num, duplicate_num

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))

def find_duplicate_missing(A):
	miss_XOR_dup = functools.reduce(lamda v, i: v ^ i[0] ^ i[1], 
									enumerate(A), 0)

	differ_bit, miss_or_dup = miss_XOR_dup & (~(miss_XOR_dup - 1)), 0
	for i, a in enumerate(A):
		if i & differ_bit:
			miss_or_dup ^= i
		if a & differ_bit:
			miss_or_dup ^= a

	if miss_or_dup in A:
		return DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_XOR_dup)
	return DuplicateAndMissing(miss_or_dup ^ miss_XOR_dup, miss_or_dup)


if __name__ == "__main__":
	matrix = [[-1,2,4,4,6],
			  [1,5,5,9,21],
			  [3,6,6,9,22],
			  [3,6,8,10,24],
			  [6,8,9,12,25],
			  [8,10,12,13,40]]

	print(search_2d_array(matrix, 8))
	print(matrix_search_BOOK(matrix, 8))
	# arr = [1,4,7,3,9,2,5,34543,23,2,5,8,3,2432,674,-1]
	# print(get_min_max(arr))
	# print(find_min_max_BOOK(arr))
	# print(int_square_root(1342))
	# arr = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
	# print(smallest_in_cyclic_array(arr))
	# arr = [-2,0,2,2,4,5,6]
	# print(find_entry_equal_to_idx(arr))
	# print(search_entry_equal_to_its_index(arr))
	# arr = [0,1,1,1,1,1,1,1]
	# print(find_first_k(arr, 2))


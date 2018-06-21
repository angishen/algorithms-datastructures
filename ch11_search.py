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

def square_root(k):
	left, right = 0, k
	while left <= right:
		mid = (left + right) // 2 
		mid_squared = mid * mid
		if mid_squared < k:
			left = mid + 1  
		else:
			right = mid - 1
	return left - 1 


if __name__ == "__main__":
	print(int_square_root(1342))
	# arr = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
	# print(smallest_in_cyclic_array(arr))
	# arr = [-2,0,2,2,4,5,6]
	# print(find_entry_equal_to_idx(arr))
	# print(search_entry_equal_to_its_index(arr))
	# arr = [0,1,1,1,1,1,1,1]
	# print(find_first_k(arr, 2))


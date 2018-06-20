import heapq
import itertools
import math

# 10.1 MERGE SORTED FILES
def sort_stocks(dir, result_f):
	minheap = []
	for file in dir:
		with open(file, "r") as in_file:
			for line in infile:
				line = line.split(",")
				heapq.heappush(minheap, (line[0], line[1:]))

	with open(result_f, "w") as out_file:
		while heap:
			heap_entry = heapq.heappop(minheap)
			out_file.write(",".join(list(heap_entry[0]) + heap_entry[1]))

def merge_sorted_arrays_BOOK(sorted_arrays):
	min_heap = []
	sorted_arrays_iters = [iter(x) for x in sorted_arrays]

	for i, it in enumerate(sorted_arrays_iters):
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap, (first_element, i))

	result = []
	while min_heap:
		smallest_entry, smallest_array_i = heapq.heappop(min_heap)
		smallest_array_iter = sorted_arrays_iters[smallest_array_i]
		result.append(smallest_entry)
		next_element = next(smallest_array_iter, None)
		if next_element is not None:
			heapq.heappush(min_heap, (next_element, smallest_array_i))

	return result

def merge_sorted_arrays_pythonic_BOOK(sorted_arrays):
	return list(heapq.merge(*sorted_arrays))

# 10.2 SORT AN INCREASING/DECREASING ARRAY
def k_ascending_descending(arr, k):
	def split_arr_kszie_chunks(arr, k):
		for i in range(0, len(arr), k):
			yield arr[i:i+k]

	result = []
	min_heap, max_heap = [], []
	arrays = list(split_arr_kszie_chunks(arr, k))

	for i in range(len(arrays)):
		for j in range(len(arrays[i])):
			if i % 2 == 0:
				heapq.heappush(min_heap, arrays[i][j])
			else:
				heapq.heappush(max_heap, -arrays[i][j])
		if i % 2 == 0:
			while min_heap:
				result.append(heapq.heappop(min_heap))
		else:
			while max_heap:
				result.append(-heapq.heappop(max_heap))

	return result

def sort_k_increasing_decreasing_array(A):
	sorted_subarrays = []
	INCREASING, DECREASING = range(2)
	subarray_type = INCREASING
	start_idx = 0
	for i in range(1, len(A) + 1):
		if (i == len(A) or 
			(A[i - 1] < A[i] and subarray_type == DECREASING) or
			(A[i - 1] >= A[i] and subarray_type == INCREASING)):
			sorted_subarrays.append(A[start_idx:i] if subarray_type ==
									INCREASING else A[i - 1:start_idx - 1:-1])
			start_idx = isubarray_type = (DECREASING
										  if subarray_type == INCREASING else INCREASING)
	return merge_sorted_arrays_pythonic_BOOK

def sort_k_increasing_decreasing_array_pythonic(A):
	class Monotonic:
		def __init__(self):
			self._last = float('-inf')

		def __call__(self, curr):
			res = curr < self._last
			self._last = curr
			return res

	return merge_sorted_arrays_pythonic_BOOK([
		list(group)[::-1 if is_decreasing else 1]
		for is_decreasing, group in itertools.groupby(A, Monotonic())
	])

# 10.3 SORT AN ALMOST SORTED ARRAY
def sort_approx_sorted_array_BOOK(sequence, k):
	result = []
	min_heap = []

	for x in itertools.islice(sequence, k):
		heapq.heappush(min_heap, x)

	for x in sequence:
		smallest = heapq.heappushpop(min_heap, x)
		result.append(smallest)

	while min_heap:
		smallest = heapq.heappop(min_heap)
		result.append(smallest)

	return result

# 10.4 COMPUTE THE K CLOSEST STARS
class Star(object):
	def __init__(self, x, y, z):
		self.x = x 
		self.y = y
		self.z = z

	def get_distance_from_earth(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def __str__(self):
		return "(" + str(self.x) +", " + str(self.y) + ", " + str(self.z) + ")"

	__repr__ = __str__

def get_k_closest_stars(star_arr, k):
	max_heap = []

	for star in itertools.islice(star_arr, k):
		heapq.heappush(max_heap, (-star.get_distance_from_earth(), star))

	for star in star_arr[k:]:
		distance = star.get_distance_from_earth()
		if -distance > max_heap[0][0]:
			heapq.heappushpop(max_heap, (-distance, star))

	result = []
	while max_heap:
		result.append(heapq.heappop(max_heap)[1])

	return result

# 10.5 COMPUTE THE MEDIAN OF ONLINE DATA
def online_median_BOOk(sequence):
	min_heap = []
	max_heap = []
	result = []

	for x in sequence:
		heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))

		if len(max_heap) > len(min_heap):
			heapq.heappush(min_heap, -heapq.heappop(max_heap))

		result.append(0.5 * (min_heap[0] + (-max_heap[0]))
			if len(min_heap) == len(max_heap) else min_heap[0])

	return result

# 10.6 COMPUTE THE K LARGEST ELEMENTS IN A MAX HEAP
def k_largest_in_max_heap(arr, k):
	if k <= 0:
		return []

	candidate_max_heap = []
	candidate_max_heap.append((-A[0], 0))
	result = []

	for _ in range(k):
		candidate_idx = candidate_max_heap[0][1]
		result.append(heapq.heappop(candidate_max_heap)[0])

		left_child_idx = 2 * candidate_idx + 1
		if left_child_idx < len(arr):
			heapq.heappush(candidate_max_heap, (arr[left_child_idx], left_child_idx))

		right_child_idx = 2 * candidate_idx + 2
		if right_child_idx < len(arr):
			heapq.heappush(candidate_max_heap, (arr[right_child_idx], right_child_idx))

	return result



if __name__ == "__main__":

	seq = [1,0,3,5,2,0,1]
	print(online_median_BOOk(seq))

	# star1 = Star(1,1,1)
	# star2 = Star(2,2,2)
	# star3 = Star(3,3,3)
	# star4 = Star(4,4,4)
	# star5 = Star(5,5,5)
	# star6 = Star(6,6,6)

	# star_arr = [star6, star3, star2, star5, star4, star1]

	# print(str(get_k_closest_stars(star_arr, 2)))


	# arr = [3,-1,2,6,4,5,8]
	# print(sort_approx_sorted_array_BOOK(arr, 2))

	# arr = [5,9,2,3,8,11,13,6,2,1]
	# print(k_ascending_descending(arr, 3))
	# print(sort_k_increasing_decreasing_array(arr))
	# print(sort_k_increasing_decreasing_array_pythonic(arr))





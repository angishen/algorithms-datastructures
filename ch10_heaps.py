import heapq
import itertools

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

if __name__ == "__main__":
	arr = [5,9,2,3,8,11,13,6,2,1]
	print(k_ascending_descending(arr, 3))
	print(sort_k_increasing_decreasing_array(arr))
	print(sort_k_increasing_decreasing_array_pythonic(arr))





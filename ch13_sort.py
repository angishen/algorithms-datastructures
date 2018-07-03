# 13.1 COMPUTE THE INTERSECTION OF TWO SORTED ARRAYS
def find_intersection(arr1, arr2):
	def is_present(x):
		lo, hi = 0, len(arr2) - 1
		while lo <= hi:
			mid = (lo + hi) // 2
			if arr2[mid] > x:
				hi = mid - 1
			elif arr2[mid] == x:
				return True
			else:
				lo = mid + 1
		return False

	intersection = set()
	if len(arr1) > len(arr2):
		arr1, arr2 = arr2, arr1
	for val in arr1:
		if is_present(val):
			intersection.add(val)

	return intersection

def intersect_two_sorted_arrays_BOOK(A, B):
	def is_present(k):
		i = bisect.bisect_left(B, k)
		return i < len(B) and B[i] == k

	return [
		a for i, a in enumerate(A)
		if (i == 0 or a != A[i-1] and is_present(a))
	]

def intersect_two_sorted_arrays_optimized_BOOK(A, B):
	i, j, intersection_A_B = 0, 0, []
	while i < len(A) and j < len(B):
		if A[i] == B[j]:
			if i == 0 or A[i] != A[i-1]:
				intersection_A_B.append(A[i])
			i, j = i + 1, j + 1
		elif A[i] < B[j]:
			i += 1
		else:
			j += 1
	return intersection_A_B

#13.2 MERGE TWO SORTED ARRAYS
def merge_two_arrays(A,B):
	C = []
	i = j = 0
	while i < len(A) and j < len(B):
		if A[i] <= B[j]:
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1

	if i < len(A):
		C.extend(A[i:])
	if j < len(A):
		C.extend(B[j:])
	return C

def merge_two_sorted_arrays_BOOK(A, B):
	m, n = len(A), len(B)
	a, b, write_idx = m - 1, n - 1 , m + n - 1
	while a >= 0 and b >= 0:
		if A[a] > B[b]:
			A[write_idx] = A[a]
			a -= 1
		else:
			A[write_idx] = B[b]
			b -= 1
		write_idx -= 1
	while b >= 0:
		A[write_idx] = B[b]
		write_idx, b = write_idx - 1, b - 1
	return A

#13.3 REMOVE FIRST NAME DUPLICATES
class Name(object):
	def __init__(self, first, last):
		self.first = first
		self.last = last
		self.full_name = (self.first, self.last)

	def __lt__(self, other):
		return self.first < other.first

	def __eq__(self, other):
		return self.first == other.first

	def __str__(self):
		return self.first + " " + self.last


def remove_first_name_duplicates(names):
	names = sorted(names)
	for i in range(len(names)-1):
		if names[i] == names[i+1]:
			del names[i+1]
	return names

class Name_BOOK:
	def __init__(self, first_name, last_name):
		self.first_name, self.last_name = first_name, last_name

	def __eq__(self, other):
		return self.first_name == other.first_name

	def __lt__(self, other):
		return (self.first_name < other.first_name
				if self.first_name != other.first_name else
				self.last_name < other.last_name)

def eliminate_duplicates(A):
	A.sort()
	write_idx = 1
	for cand in A[1:]:
		if cand != A[write_idx - 1]:
			A[write_idx] = cand
			write_idx += 1
	del A[write_idx:]

# 13.4 SMALLEST NON-CONSTRUCTIBLE VALUE
def smallest_nonconstructible_value(A):
	max_num_possible = 0
	for num in sorted(A):
		if num > max_num_possible + 1:
			break
		max_num_possible += num
	return max_num_possible + 1

def smallest_nonconstructible_value_BOOK(A):
	max_constructible_value = 0
	for a in sorted(A):
		if a > max_constructible_value + 1:
			break
		max_constructible_value += a
	return max_constructible_value + 1

if __name__ == "__main__":
	A = [1,1,1,1,1,5,10,25]
	print(smallest_nonconstructible_value(A))
	# names = [Name("Angi", "Shen"), Name("Babs", "McBab"), Name("Babs", "McCool"), Name("Austin", "Stone")]
	# dups_removed = remove_first_name_duplicates(names)
	# for name in dups_removed:
	# 	print(str(name))
	# A = [1,3,9,11,12,13]
	# B = [2,4,5,8,12,15]
	# print(merge_two_arrays(A, B))
	# print(merge_two_sorted_arrays_BOOK(A, B))
	# arr1 = [2,3,3,5,5,6,7,7,8,12]
	# arr2 = [5,5,6,8,8,9,10,10]
	# print(find_intersection(arr1, arr2))


import collections

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

# 13.5 RENDER A CALENDAR
Event = collections.namedtuple('Event', ('start_time', 'end_time'))

def render_calendar(events):
	max_overlapping_events = 1
	sorted_events = sorted(events, key=lambda x: x.start_time)
	for i in range(len(sorted_events)-1):
		overlapping_events = 1
		event_idx = i + 1
		while (sorted_events[event_idx].start_time >=sorted_events[i].start_time
		  and sorted_events[event_idx].start_time <= sorted_events[i].end_time
		  and event_idx < len(sorted_events) - 1):
			overlapping_events += 1
			event_idx += 1
		max_overlapping_events = max(max_overlapping_events, overlapping_events)
	return max_overlapping_events

Event_BOOK = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events_BOOK(A):
	E =  ([Endpoint(event.start_time, True) for event in A] + 
		  [Endpoint(event.end_time, False) for event in A])
	E.sort(key=lambda e: (e.time, not e.is_start))

	max_num_simultaneous_events, num_simultaneous_events = 0, 0
	for e in E:
		if e.is_start:
			num_simultaneous_events += 1
			max_num_simultaneous_events = max(num_simultaneous_events, max_num_simultaneous_events)
		else:
			num_simultaneous_events -= 1
	return max_num_simultaneous_events

# 13.6 MERGING INTERVALS
Interval = collections.namedtuple('Interval', ('start', 'end'))
def merge_intervals(intervals, new_interval):
	result = []
	new_start, new_end = None, None
	for interval in intervals:
		if interval.end < new_interval.start or interval.start > new_interval.end:
			result.append(interval)
		else:
			if interval.start < new_interval.start and interval.end < new_interval.end:
				new_start = interval.start
			elif interval.end > new_interval.start and interval.end > new_interval.end:
				new_end = interval.end
	if not new_start:
		new_start = new_interval.start
	if not new_end:
		new_end = new_interval.end
	result.append(Interval(new_start, new_end))
	return result

def add_interval_BOOK(disjoint_intervals, new_interval):
	i, result = 0, []

	while (i < len(disjoint_intervals) and 
		   new_interval.start > disjoint_intervals[i].end):
		result.append(disjoint_intervals[i])
		i += 1

	while (i < len(disjoint_intervals) and
		   new_interval.end >= disjoint_intervals[i].start):
		new_interval = Interval(
			min(new_interval.start, disjoint_intervals[i].start),
			max(new_interval.end, disjoint_intervals[i].end))
		i += 1

	return result + [new_interval] + disjoint_intervals[i:]

if __name__ == "__main__":
	intervals = [Interval(-4, -1), Interval(0, 2), Interval(3, 6), Interval(11, 12), Interval(14, 17)]
	new_interval = Interval(1, 8)
	print(merge_intervals(intervals, new_interval))
	print(add_interval_BOOK(intervals, new_interval))
	# events = [Event(7, 10), Event(8, 9), Event(12, 17), Event(13, 13.5), Event(7.5, 8.5), Event(20, 23), 
	# 			Event(13, 14), Event(15, 15.5), Event(14, 17)]

	# print(find_max_simultaneous_events_BOOK(events))
	# print(render_calendar(events))
	# E =  ([Endpoint(event.start_time, True) for event in events] + 
	# 	  [Endpoint(event.end_time, False) for event in events])
	# E.sort(key=lambda e: (e.time, not e.is_start))
	# print(E)
	
	# print(render_calendar(events))
	# A = [1,1,1,1,1,5,10,25]
	# print(smallest_nonconstructible_value(A))
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


import collections
import re
import heapq
import operator

# 12.1 TEST FOR PALINDROMIC PERMUATIONS
def palindrome_permutation(st):
	char_dict = {}
	for char in st:
		if char not in dict:
			dict[char] = 1 
		else:
			dict[char] += 1 
	odd_count, even_count = 0, 0
	for key, value in char_dict.items():
		if value % 2 == 0:
			even_count += 1 
		else:
			odd_count += 1 
	if len(st) % 2 == 0:
		return odd_count < 1 
	else:
		return odd_count == 1 

def can_form_palindrome(s):
	return sum(v % 2 for v in collections.Counter(s).values()) <= 1

#12.2 IS AN ANONYMOUS LETTER CONSTRUCTIBLE
def anonymous_letter(letter, magazine):
	import re
	let = collections.Counter(re.sub(r'\W+', '', letter))
	mag = collections.Counter(re.sub(r'\W+', '', magazine))
	return len(mag - let) > 0

def is_letter_constructible_from_magazine_BOOK(letter_text, magazine_text):
	char_frequency_for_letter = collections.Counter(letter_text)

	for c in magazine_text:
		if c in char_frequency_for_letter:
			char_frequency_for_letter[c] -= 1
			if char_frequency_for_letter == 0:
				del char_frequency_for_letter[c]
				if not char_frequency_for_letter:
					return True
	return not char_frequency_for_letter

# pythonic solution
def is_letter_constructible_from_magazine_pythonic_BOOK(letter_text, magazine_text):
	return (not collections.Counter(letter_text) - collections.Counter(magazine_text))

# 12.3 IMPLEMENT AN ISBN CACHE
class IsbnCache(object):
	def __init(self):
		self.cache = {}

	def insert(self, isbn, price):
		self.chace[isbn] = price

	def remove(self, isbn):
		del self.cache[isbn]

	def lookup(self, isbn):
		if isbn in self.cache:
			return isbn, price
		return "entry not found"

# book solution
class LRUCache:
	def __init__(self, capacity):
		self._isbn_price_table = collections.OrderedDict()
		self._capacity = capacity

	def lookup(self, isbn):
		if isbn not in self._isbn_price_table:
			return None
		price = self._isbn_price_table.pop(isbn)
		self._isbn_price_table[isbn] = price
		return True, price

	def insert(self, isbn, price):
		if isbn in self._isbn_price_table:
			price = self._isbn_price_table.pop(isbn)
		elif self._capacity <= len(self._isbn_price_table):
			self._isbn_price_table.popitem(last=False)
		self._isbn_price_table[isbn] = price

	def erase(self, isbn):
		return self._isbn_price_table.pop(isbn, None) is not None

#12.4 COMPUTE THE LCA, OPTIMIZING FOR CLOSE ANCESTORS
def get_lca(node0, node1):
	node_table = {}
	while node0:
		node_table[node0] = True
		node0 = node0.parent
	while node1:
		if node1 in node_table:
			return node1

def lca(node_0, node_1):
	iter_0, iter_1 = node_0, node_1
	nodes_on_path_to_root = set()
	while iter_0 or iter_1:
		if iter_0:
			if iter_0 in nodes_on_path_to_root:
				return iter_0
			nodes_on_path_to_root.add(iter_0)
			iter_0 = iter_0.parent
		if iter_1:
			if iter_1 in nodes_on_path_to_root:
				return iter_1
			nodes_on_path_to_root.add(iter_1)
			iter_1 = iter_1.parent
	raise ValueError('node_0 and node_1 are not in the same tree')

# 12.5 COMPUTE THE K MOST FREQUENT QUERIES
def k_most_frequent_strings(arr, k):
	return collections.Counter(arr).most_common(k)

# 12.6 FIND NEAREST REPEATED ENTRIES IN AN ARRAY
def get_closest_words(arr):
	distance_dict = {}
	min_distance_word = None
	min_distance = float('inf')
	for idx, word in enumerate(arr):
		if word not in distance_dict:
			distance_dict[word] = idx
		else:
			distance_btw_words = idx - distance_dict[word] - 1
			distance_dict[word] = idx
			if distance_btw_words < min_distance:
				min_distance_word = word
				min_distance = distance_btw_words
	return min_distance_word

def find_nearest_repetition_BOOK(paragraph):
	word_to_latest_idx, nearest_repeated_distance = {}, float('inf')
	for i, word in word_to_latest_idx:
		latest_equal_word = word_to_latest_idx[word]
		nearest_repeated_distance = min(nearest_repeated_distance, 
										i - latest_equal_word)

		word_to_latest_idx[word] = i
	return nearest_repeated_distance

# 12.7 FIND THE SMALLEST SUBARRAY
def find_smallest_subarray_covering_set_BOOK(paragraph, keywords):
	keywords_to_cover = collections.Counter(keywords)
	result = (-1, -1)
	remaining_to_cover = len(keywords)
	left = 0
	for right, p in enumerate(paragraph):
		if p in keywords:
			keywords_to_cover[p] -= 1 
			if keywords_to_cover[p] == 0:
				remaining_to_cover -= 1 

		while remaining_to_cover == 0:
			if result == (-1, -1) or right - left < result[1] - result[0]:
				result = (left, right)
			p1 = paragraph[left]
			if p1 in keywords:
				keywords_to_cover[p1] += 1
				if keywords_to_cover[p1] > 0:
					remaining_to_cover += 1
			left += 1
	return result

def find_smallest_subarray_covering_set_streaming_BOOK(stream, query_strings):
	class DoublyLinkedList:
		def __init__(self, data=None):
			self.data = data
			self.next = self.prev = None

	class LinkedList:
		def __init__(self):
			self.head = self.tail = None
			self._size = 0

		def __len__(self):
			return self._size

		def insert_after(self, value):
			node = DoublyLinkedList(value)
			node.prev = self.tail
			if self.tail:
				self.tail.next = node
			else:
				self.head = node
			self.tail = node
			self._size += 1 

		def remove(self, node):
			if node.next: 
				node.next.prev = node.prev
			else:
				self.tail = node.prev
			if node.prev:
				node.prev.next = node.next
			else:
				self.head = node.next
			node.next = node.prev = None
			self._size -= 1 

	loc = LinkedList()
	d = {s: None for s in query_strings}
	res = (-1, -1)
	for idx, s in enumerate(stream):
		if s in d:
			it = d[s]
			if it is not None:
				loc.remove(it)
			loc.insert_after(idx)
			d[s] = loc.tail

			if len(loc) == len(query_strings):
				if res == (-1, -1) or idx - loc.head.data < res[1] - res[0]:
					res = (loc.head.data, idx)
	return res

# 12.8 FIND SMALLEST SUBARRAY SEQUENTIALLY COVERING ALL VALUES
Subarray = collections.namedtuple('Subarray', ('start', 'end'))
def find_smallest_sequentially_covering_subset(paragraph, keywords):
	keyword_to_idx = {k: i for i, k in enumerate(keywords)}
	latest_occurence = [-1] * len(keywords)
	shortest_subarray_length = [float('inf')] * len(keywords)

	shortest_distance = float('inf')
	result = Subarray(-1, -1)
	for i, p in enumerate(paragraph):
		if p in keyword_to_idx:
			keyword_idx = keyword_to_idx[p]
			if keyword_idx == 0:
				shortest_subarray_length[keyword_idx] = 1
			elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
				distance_to_previous_keyword = (
					i - latest_occurence[keyword_idx - 1])
				shortest_subarray_length[keyword_idx] = (
					distance_to_previous_keyword + 
					shortest_subarray_length[keyword_idx - 1])
				latest_occurence[keyword_idx] = i
			latest_occurence[keyword_idx] = i

			if (keyword_idx == len(keywords) - 1 and 
					shortest_subarray_length[-1] < shortest_distance):
				shortest_distance = shortest_subarray_length[-1]
				result = Subarray(i - shortest_distance + 1, i)
		print(i, p, latest_occurence, shortest_subarray_length)
	return result

# 12.9 FIND THE LONGEST SUBARRAY WITH DISTINCT ENTRIES
def longest_distinct_subarray(arr):
	start = max_start = 0
	max_len = float('-inf')
	letters_seen = {}
	for i, letter in enumerate(arr):
		if len(arr) - 1 - i < max_len:
			return (max_start, max_start + max_len - 1)
		if letter in letters_seen:
			start = letters_seen[letter] + 1
		letters_seen[letter] = i
		if i - start + 1 > max_len:
			max_len = i - start + 1
			max_start = start
	# return (max_start, max_start + max_len - 1)

def longest_subarray_with_distinct_entries(A):
	most_recent_occurences = {}
	longest_dup_free_subarray_start_idx = result = 0
	for i, a in enumerate(A):
		if a in most_recent_occurences:
			dup_idx = most_recent_occurences[a]
			if dup_idx >= longest_dup_free_subarray_start_idx:
				result = max(result, i - longest_dup_free_subarray_start_idx)
				longest_dup_free_subarray_start_idx = dup_idx + 1
		most_recent_occurences[a] = i
	return max(result, len(A)-longest_dup_free_subarray_start_idx)
# 12.10 FIND LENGTH OF THE LONGEST CONTAINED INTERVAL
def longest_contained_range(A):
	unprocessed_entries = set(A)
	max_interval_size = 0

	while unprocessed_entries:
		a = unprocessed_entries.pop()

		lower_bound = a - 1
		while lower_bound in unprocessed_entries:
			unprocessed_entries.remove(lower_bound)
			lower_bound -= 1 

		upper_bound = a + 1 
		while upper_bound in unprocessed_entries:
			unprocessed_entries.remove(upper_bound)
			upper_bound += 1

		max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)
	return max_interval_size

# 12.11 FIND THE STUDENT WITH THE TOP 3 SCORES
def get_top_student(score_data):
	student_scores = collections.defaultdict(list)

	for line in score_data:
		name, score = line.split()
		if len(student_scores[name]) < 3:
			heapq.heappush(student_scores[name], int(score))
		else:
			heapq.heappushpop(student_scores[name], int(score))

	return max([(sum(scores), name) for name, scores in student_scores.items()
					if len(scores) == 3],
					key = operator.itemgetter(0),
					default = 'no such student')[1]
 
 # 12.12 COMPUTE ALL STRING DECOMPOSITIONS
def string_decomposition(sentence, words):
	word_len = len(words[0])
	phrase_len = len(",".join(words))
	starting_idxs = []
	for i, char in enumerate(sentence):
		words_to_match = collections.Counter(words)
		start_idx = i
		while words_to_match:
			phrase = sentence[start_idx:start_idx+word_len]
			if phrase not in words_to_match:
				break
			else:
				words_to_match[phrase] -= 1
				if words_to_match[phrase] == 0:
					del words_to_match[phrase]
				start_idx += word_len
		if not words_to_match:
			starting_idxs.append(i)
	return starting_idxs

def find_all_substrings(s, words):
	def match_all_words_in_dict_BOOK(start):
		curr_string_to_freq = collections.Counter()
		for i in range(start, start + len(words) * unit_size, unit_size):
			curr_word = s[i:i + unit_size]
			it = word_to_freq[curr_word]
			if it == 0:
				return False
			currn_string_to_freq[curr_word] += 1
			if cur_string_to_freq[curr_word] > it:
				return False
		return True

	word_to_freq = collections.Counter(words)
	unit_size = len(words[0])
	return [
		i for i in range(len(s) - unit_size * len(words) + 1)
		if match_all_words_in_dict(i)
	]

# 12.3 TEST THE COLLATZ CONJECTURE
def collatz(n):
	proven_nums = set()
	def prove_num(m):
		while m > 1:
			if m in proven_nums:
				return True
			else:
				if m % 2 != 0:
					m = m * 3 + 1
				else:
					m = m // 2
		if m == 1:
			return True

	for i in range(1, n+1):
		if prove_num(i):
			proven_nums.add(i)
			print(proven_nums)

def test_collatz_conjecture(n):
	verified_numbers = set()

	for i in range(3, n+1):
		test_i = i
		while test_i >= i:
			if test_i in sequence:
				return False
			sequence.add(test_i)

		if test_i % 2:
			if test_i in verified_numbers:
				break
			verified_numbers.add(test_i)
			test_i = 3 * test_i + 1
		else:
			test_i //= 2
	return True
	


if __name__ == "__main__":
	# sentence = "amancancananacanaplal"
	# words = ['can', 'can', 'ana']
	# print(string_decomposition(sentence, words))
	collatz(120)
	# score_data = ["angi 67", "angi 95", "angi 10", "angi 98", "bab 100", "bab 65", "arthur 30",
	# 			  "bab 85", "arthur 10", "julia 67", "arthur 94", "bab 89", "george 80"]
	# print(get_top_student(score_data))
	# letters = ['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e']
	# print(longest_distinct_subarray(letters))
	# print(longest_subarray_with_distinct_entries(letters))
	# paragraph = ["what", "the", "fuck", "hello", "banana", "banana", "cucumber", "cat"]
	# keywords = ["banana", "cat"]
	# print(find_smallest_sequentially_covering_subset(paragraph, keywords))
	# strings = ['All', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'fun', 'and', 'no', 'results']
	# print(get_closest_words(strings))
	# strings = ["beatles", "beatles", "blondie", "fleetwood mac", "blondie", "beatles", "judas priest", "beatles", "blondie"]
	# print(k_most_frequent_strings(strings, 3))
	# magazine = "hello my name is angi"
	# letter = "hello angi"
	# print(anonymous_letter(magazine, letter))
	# print(palindrome_permutation(st))
	# print(can_form_palindrome(st))

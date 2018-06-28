import collections
import re

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
	

if __name__ == "__main__":
	strings = ['All', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'fun', 'and', 'no', 'results']
	print(get_closest_words(strings))
	# strings = ["beatles", "beatles", "blondie", "fleetwood mac", "blondie", "beatles", "judas priest", "beatles", "blondie"]
	# print(k_most_frequent_strings(strings, 3))
	# magazine = "hello my name is angi"
	# letter = "hello angi"
	# print(anonymous_letter(magazine, letter))
	# print(palindrome_permutation(st))
	# print(can_form_palindrome(st))

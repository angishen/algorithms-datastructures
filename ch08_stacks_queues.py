import collections

class Stack(object):
	def __init__(self):
		self._stack = []

	def empty(self):
		return len(self._stack) == 0

	def push(self, x):
		self._stack.append(x)

	def pop(self):
		return self._stack.pop()

# 8.1 IMPLEMENT A STACK WITH A MAX API
class MaxStack(object):
	def __init__(self):
		self.stack = []
		self.max = [float('-inf')]

	def push(self, data):
		self.stack.append(data)
		if data >= self.max[-1]:
			self.max.append(data) 

	def pop(self):
		if self.max[-1] == self.stack[-1]:
			self.max.pop()
		return self.stack.pop()

	def get_max(self):
		if self.max[-1] == float('-inf'):
			return None
		return self.max[-1]

	def print_stack(self):
		return [num for num in self.stack]

# 8.2: EVALUATE RPN EXPRESSIONS
def eval_RPN(expr):
	my_stack = Stack()
	operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, 
				  "*": lambda x, y: x * y, "/": lambda x, y: x / y}
	expr = expr.split(",")
	for char in expr:
		if char.isdigit() or char.startswith('-') and char[1:].isdigit():
			my_stack.push(int(char))
		else:
			opr = operations[char]
			y = my_stack.pop()
			x = my_stack.pop()
			my_stack.push(opr(x, y))
	return my_stack.pop()

def evaluate_RPN_BOOK(RPN_expression):
	intermediate_results = []
	DELIMITER = ','
	OPERATORS = {"+": lambda y, x: x + y, "-": lambda y, x: x - y, 
				 "*": lambda y, x: x * y, "/": lambda y, x: int(x / y)}
	for token in RPN_expression.split(DELIMITER):
		if token in OPERATORS:
			intermediate_results.append(OPERATORS[token](
				intermediate_results.pop(), intermediate_results.pop()))
		else:
			intermediate_results.append(int(token))
	return intermediate_results[-1]

# 8.3 TEST A STRING OVER '[,],(,),{,}' FOR WELL-FORMEDNESS
def well_formed(expr):
	PARENS = {'(': ')', '{': '}', '[': ']'}
	stack = []
	for char in expr:
		print(stack)
		if char in PARENS:
			stack.append(char)
		elif len(stack) == 0 or PARENS[stack.pop()] != char:
			return False
	return len(stack) == 0

def is_well_formed_BOOK(s):
	left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
	for c in s:
		if c in lookup:
			left_chars.append(c)
		elif not left_chars or lookup[left_chars.pop()] != c:
			return False
	return not left_chars

# 8.4 NORMALIZE PATH NAMES
def normalize_pathname(path):
	if not path:
		return None

	normalizer = []
	symbols = [".", "..", ""]

	path = path.split("/")
	for elt in path:
		if elt not in symbols:
			normalizer.append(elt)
		elif elt == ".." and len(normalizer) > 0:
			normalizer.pop()
	return "/".join(normalizer)

def shortest_equivalent_path(path):
	if not paths:
		raise ValueError("Empty string is not valid path")
	path_names = [] # use list as a stack
	# special case starts with "/" which is an absolute path
	if path[0] == '/':
		path_names.append('/')
	for token in (token for token in path.split('/') if token not in ['.', '']):
		if token == '..':
			if not path_names or path_names[-1] == '..':
				path_names.append(token)
			else:
				if path_names[-1] == '/':
					raise ValueError("Path error")
				path_names.pop()
		else: # must be a name
			path_names.append(token)
	result = '/'.join(path_names)
	return result[result.startswith('//'):]

# 8.5: COMPUTE BUILDINGS WITH A SUNSET VIEW
def sunset_view(heights):
	can_see_sunset = []
	for idx, height in enumerate(heights):
		while can_see_sunset and height >= can_see_sunset[-1][1]:
			can_see_sunset.pop()
		can_see_sunset.append((idx, height))
	return can_see_sunset[::-1]

def examine_buildings_with_sunset(sequence):
	BuildingWithHeight = collections.namedtuple('BuildingWithHeight', ('id', 'height'))

	candidates = []
	for building_idx, building_height in enumerate(sequence):
		while candidates and building_height >= candidates[-1].height:
			candidates.pop()
		candidates.append(BuildingWithHeight(building_idx, building_height))
	return [(candidate.id, candidate.height) for candidate in reversed(candidates)]

# 8.8 IMPLEMENT A QUEUE WITH A MAX API
class QueueWithMax(object):
	def __init__(self):
		self._queue = []
		self._max = []

	def max(self):
		if not self._max:
			raise IndexError("Empty queue")
		return self._max[0]

	def enqueue(self, data):
		self._queue.append(data)
		while self._max and data > self._max[0]:
			self._max.pop(0)
		self._max.append(data)

	def dequeue(self):
		if not self._queue:
			raise IndexError("Empty queue")
		if self._queue[0] == self._max[0]:
			self._max.pop(0)
		return self._queue.pop(0)


def main():
	myQueue = QueueWithMax()

	myQueue.enqueue(9)
	print(myQueue.max())
	myQueue.enqueue(10)
	print(myQueue.max())
	myQueue.dequeue()
	myQueue.enqueue(7)
	myQueue.dequeue()
	myQueue.dequeue()
	print(myQueue.max())

	# heights = [10, 19, 18, 15, 5, 10, 20]
	# print(sunset_view(heights))
	# path = "//./../scripts/awkscripts/././hello/../goodbye/././"
	# print(normalize_pathname(path))
	# expr = "())))))))"
	# print(is_well_formed_BOOK(expr))
	# RPN = "-641,6,/,28,/"
	# print(eval_RPN(RPN))
	# print(evaluate_RPN_BOOK(RPN))
	# myStack = Stack()
	# nums = [1,3,9,5,2,20,20,21]
	# for num in nums:
	# 	myStack.push(num)
	# 	print(myStack.print_stack())
	# 	print(myStack.get_max())
	# for i in range(len(nums)):
	# 	myStack.pop()
	# 	print(myStack.print_stack())
	# 	print(myStack.get_max())

main()
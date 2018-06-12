import functools

# 6.1 Interconvert strings and ints
def str_to_int(string):
    sum = 0
    for i in range(len(string)):
        ord_of_magnitude = len(string) - i - 1
        num = ord(string[i]) - 48
        sum += num * (10 ** ord_of_magnitude)
    return sum

def int_to_str(integer):
    string = ""
    while integer > 0:
        char = chr((integer % 10) + 48)
        string += char
        integer = integer // 10
    return string[::-1]

def base_converter(st, b1, b2):
    def base_to_decimal(st, b1):
        sum = 0
        current_place = len(st) - 1
        while current_place >= 0:
            if st[current_place].isalpha():
                dig = ord(st[current_place]) - 55
            else:
                dig = int(st[current_place])
            sum += dig * b1 ** (len(st) - current_place - 1)
            current_place -= 1
        return sum

    def decimal_to_base(b2):
        decimal_int = base_to_decimal(st,b1)
        result_st = ""
        while decimal_int > 0:
            remainder = decimal_int % b2
            if remainder > 9:
                remainder = chr(remainder + 55)
            result_st += str(remainder)
            decimal_int //= b2
        return result_st[::-1]
    return decimal_to_base(b2)

# 6.3 COMPUTE THE SPREADSHEET ENCODING

def spreadsheet_encoding(column_name):
    int_val = 0
    for i, letter in enumerate(column_name):
        letter = letter.upper()
        ascii_val = ord(letter) - 64
        power = len(column_name) - 1 - i
        val = 26 ** power * ascii_val
        int_val += val
    return int_val

# 6.4 REPLACE AND REMOVE
def replace_and_remove(st, count):
    idx, count = 0, count
    result_arr = []
    while count > 0 and idx < len(st):
        if st[idx] == "b":
            count -= 1
            idx += 1
            continue
        elif st[idx] == "a":
            result_arr.extend(["d", "d"])
            count -= 1
        else:
            result_arr.append(st[idx])
        idx += 1
    return ("").join(result_arr)

# 6.5 TEST FOR PALINDROMICITY
def is_palindrome(st):
    for i in range(len(st) // 2):
        if st[i] != st[len(st)-1-i]:
            return False
    return True

# 6.6 REVERSE ALL WORDS IN A SENTENCE
def reverse_sentence(sentence):
    return (" ").join(sentence.split(" ")[::-1])

def reverse_sentence2(sentence):
    reversed_sentence = ""
    sentence += " "
    start_idx = 0
    for i in range(len(sentence)):
        if sentence[i].isspace() or i == len(sentence)-1:
            reversed_sentence = sentence[start_idx:i] + " " + reversed_sentence
            start_idx = i+1
    return reversed_sentence

def reverse_sentence_BOOK(s):
    # assume s is a string encoded as a bytearray
    def reverse_words(s):
        # first, reverse the whole string
        s.reverse()

        def reverse_range(s, start, end):
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

        start = 0
        while True:
            end = s.find(b' ', start)
            if end < 0:
                break
            #.reverse each word in the string
            reverse_range(s, start, end-1)
            start = end + 1
        # reverses the last word
        reverse_range(s, start, len(s)-1)

def look_and_say(n):
    def next_num(prev_num):
        result, i = [], 0
        while i < len(prev_num):
            num_occurances = 1
            while i + 1 < len(prev_num) and prev_num[i] == prev_num[i+1]:
                num_occurances += 1
                i += 1
            result.append(str(num_occurances) + prev_num[i])
            i += 1
        return ''.join(result)

    prev_num = '1'
    for i in range(1, n):
        prev_num = next_num(prev_num)
    return prev_num

def look_and_say_BOOK(n):
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i+1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)

    s = '1'
    for i in range(1, n):
        s = next_number(s)
    return s

def phone_mnemonic_BOOK(phone_number):
    
    MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)

    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics

def roman_to_int(roman_num):
    mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    exceptions = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}

    sum = 0
    for letter in roman_num:
        sum += mapping[letter]
    for i in range(len(roman_num)-1):
        if roman_num[i] in exceptions and roman_num[i+1] in exceptions[roman_num[i]]:
            sum -= mapping[roman_num[i]] * 2
    return sum

def roman_to_integer_BOOK(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]),
        reversed(range(len(s)-1)), T[s[-1]])

# 6.10 COMPUTE ALL VALID IP ADDRESSES
def all_valid_ips(s):
    def is_valid(substr):
        return int(substr) < 256

    valid_ips = []
    for i in range(len(s)-1):
        ip = [0] * 4
        if not is_valid(s[0:i+1]):
            continue
        for j in range(i+1, len(s)-1):
            if not is_valid(s[i+1:j+1]):
                continue
            for k in range(j+1, len(s)-1):
                if not is_valid(s[j+1:k+1]) or not is_valid(s[k+1:]):
                    continue
                ip[0] = s[0:i+1]
                ip[1] = s[i+1:j+1]
                ip[2] = s[j+1:k+1]
                ip[3] = s[k+1:]
                valid_ips.append(".".join(ip))
    return valid_ips

# 6.11 WRITE A STRING SINUSOIDALLY
def snake_letters(st):
    snake = [0] * len(st)
    num_top = len(st) // 2 // 2
    num_middle = len(st) // 2 if len(st) % 2 == 0 else len(st) // 2 + 1
    top_idx, mid_idx, bottom_idx = 0, num_top, num_top + num_middle
    odd_top = True
    for i in range(len(st)):
        if i % 2 == 0:
            snake[mid_idx] = st[i]
            mid_idx += 1
        else:
            if odd_top:
                snake[top_idx] = st[i]
                top_idx += 1
            else:
                snake[bottom_idx] = st[i]
                bottom_idx += 1
            odd_top = not odd_top
    print(snake)
    return "".join(snake)
           
# 6.12 IMPLEMENT RUN LENGTH ENCODING
def encode(st):
    result = []
    count = 1
    if len(st) == 1:
        result.append(str(count) + st)
    else:
        for i in range(len(st)-1):
            if st[i] == st[i+1]:
                count += 1
            else:
                result.append(str(count) + st[i])
                count = 1
    return "".join(result)

def decode(st):
    result = []
    for i in range(len(st)-1):
        if st[i].isdigit():
            result.append(st[i+1] * int(st[i]))
    return "".join(result)

# 6.13 FIND THE FIRST OCCURANCE OF A SUBSTRING
def find_substring(s, t):
    for i in range(len(t)-len(s)+1):
        slice = t[i:i+len(s)]
        if slice == s:
            return i, i+len(s)
    return None

def main():
    s = "world"
    t = "Hello, world, this is me, Angi, world"

    print(find_substring(s, t))

main()
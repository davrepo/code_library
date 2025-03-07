# ------------------- Recursion -----------------------------------------
# A function that calls itself until a base case is reached
# Divide and Conquer: reduce a large problem into smaller problems
# Iteration is about twice as fast as Recursion, bc fxn call costs overhead

# Fibonacci
#   idx:   0   1   2   3   4   5   6   7   8   9
#   num:   0   1   1   2   3   5   8  13  21  34

import time
def fib_iter(idx):      # iteration
    seq = [0, 1]         # -2 bc first 2 elements in seq are given beforehand
    for i in range(idx):
        seq.append(seq[-1] + seq[-2])

    return seq[-2]

# DTU professor fibonnaci iteration algorithm
def fib_iter2(n):
    if n == 0 or n == 1:
        return 1
    val = 1
    m = 1
    prev = 1
    while val != n:
        val, prev = val + prev, val
        m += 1
    return val


def fib_recur(idx):     # recursion
    if idx <= 1:        # base case
        return idx
    else:
        # recursion: fxn that calls itself
        return fib_recur(idx-1) + fib_recur(idx-2)


print(fib_iter(8))  # 21
print(fib_recur(8))  # 21


# Combination algorithm with recursion using pascal identity C(n, k) = C(n-1, k-1) + C(n-1, k)
def combination_recursive(n, k):
    if k == 0:    # when k = 0, there is only 1 combination
        return 1
    if k > n or k < 0:     # when k is greater than n, there is no combination
        return 0
    else:
        return combination_recursive(n-1, k) + combination_recursive(n-1, k-1)


# Fibconacci with memoization / cache internal in class structure - cache is now an instance variable
class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    # __call__() special method allows class instances to behave like functions
    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')
        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)
        return self.cache[n]


fib_instance = Fibonacci()
fib_instance(5)  # 5
fib_instance(8)  # 21  - fibonacci number at index 8


def time_wrapper(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        return (f'{t2 - t1:.3f} secs'), res
    return wrapper


def fib(n):     # this is expensive to calculate
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@ time_wrapper
def memoization(n, memo={}):     # memo is a mutable default, stored in function object
    try:
        value = memo[n]
    except KeyError:
        value = fib(n)
        # function call with unseen argument is stored in memo
        memo[n] = value
    return value


memoization(35)  # ('2.149 secs', 14930352)
memoization(36)  # ('3.689 secs', 24157817)
memoization(36)  # ('0.000 secs', 24157817)
memoization(35)  # ('0.000 secs', 14930352)


# Factorial
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(4))  # 24

# Count length of string


def customLen(string):
    if not string:
        return 0
    else:
        return customLen(string[1:]) + 1


print(customLen('wordlist'))  # 8

# Filter out all vowels in a string
vowel = ['a', 'e', 'i', 'o', 'u']


def customLen(string):
    if not string:
        return ''
    else:
        # note the reverse splicing
        return customLen(string[:-1]) + (string[-1] if string[-1] not in vowel else '')


print(customLen('wordlistplusalotofvowels'))  # wrdlstplsltfvwls

# Palindrome


def isPalindrome(string):
    if (len(string) <= 1):
        return True
    if (string[0] == string[-1]):
        return isPalindrome(string[1:-1])
    else:
        return False

# Hangman game
# example of internal memoization


def hangman(string, guessNum=8, memo=''):     # default num of guesses is 8
    if guessNum < 1:
        print("You fail.")
        return False
    if not memo:      # print option when first started game
        print(f'You have maxinum of {guessNum} guesses that you can make')
        print('The word is: ' + '_ ' * len(string))
    else:                       # print option for subsequence guesses
        print('-' * 20)
        print(f'You have {guessNum} incorrect guess remaining')
        print('The word is: ')
        for char in memo:
            print(char + ' ', end='')
        print('_ ' * len(string), end='')

    char = input('Enter a letter: ')

    if len(string) == 1 and char == string[0]:
        memo += char
        print('You guessed correctly. The hidden word is - ' + memo)
        return True
    elif char == string[0]:
        memo += char
        print('You have guessed so far: ' + memo)
        return hangman(string[1:], guessNum, memo)
    else:
        print('You have guessed so far: ' + memo)
        return hangman(string[0:], guessNum-1, memo)


word_hidden = 'hello'
hangman(word_hidden)

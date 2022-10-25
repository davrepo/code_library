# ------------------- string format, f-string ----------------------------

# {} is placeholder
num1 = 5
num2 = 3                
print(f'{num1} times {num2} is {num1 / num2:.2f}')  #f is presentation type float, 2 is 2 decimal precision
#5 times 3 is 1.67

# Presentation types "Intro to Python" p285
# f = float, d = int to string, c = char, s = string, e = exponential scientific notation

'{:.2f}'.format(17.489) #{} is placeholder, : is start of format specifiers, .2 is 2 decimal precision, f is float presentation type
#'17.49'

#explicit call format() method
number1 = 'One'
number2 = 'Two'
number3 = 'Three'

# default(implicit) order
default_order = "{}, {} and {}".format(number1,number2,number3)
print(default_order)
# One, Two and Three

# order using positional argument
positional_order = "{1}, {0} and {2}".format(number1,number2,number3)
print(positional_order)
# Two, One and Three

'{0} {0} {1}'.format('Happy', 'Birthday')   #can reference each argument as often as one like
#'Happy Happy Birthday'

# order using keyword argument
keyword_order = "{i}, {j} and {k}".format(j=number1,k=number2,i=number3)
print(keyword_order)
# Three, One and Two

# String formatting %e for exponent
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'))
# 0001 Derek 1.23 A

# Formatted print with dictionary mapping
d1 = {"name": "Bread", "price": .88}
print("%(name)s costs $%(price).2f" % d1)
# Bread costs $0.88

# -------------------- string Tokenization ---------------------------------

from collections import Counter
# Counter: Elements are stored as dictionary keys and their counts are stored as dictionary values.

text = ('this is is is text text with with with with several words')

print(text.split())         #str.split() returns a list of words, delimiter separated
# ['this', 'is', 'is', 'is', 'text', 'text', 'with', 'with', 'with', 'with', 'several', 'words']

counter = Counter(text.split())

#Loop implementation
# word_counts = {}
# for word in text.split():
#     if word in word_counts:
#         word_counts[word] += 1      #update existing key-value pair
#     else:
#         word_counts[word] = 1       # insert new key-value pair

# for word, count in sorted(word_counts.items()):
#     print(f'{word:<12}{count}')
# # is          3
# # several     1
# # text        2
# # this        1
# # with        4
# # words       1

#Counter implementation
#returns a dictionary-like object, keys = unique words, value = word frequency
#Counter.items() returns each word and its associated count as a tuple
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')
    
# is          3
# several     1
# text        2
# this        1
# with        4
# words       1

print('Number of unique keys:', len(counter.keys()))
# Number of unique keys: 6
# Collections
# Counter, namedtuple, defaultdict, deque
# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=WL&index=7
# Counter, namedtuple, OrderedDict, defaultdict, deque


# ------------- Counter ------------------------------------------------------
# frequency map the iterable object
# returns a dictionary of key (item): value (frequency) pairs

from collections import Counter

a = 'aabbaaccaabcccccaaccccc'
my_counter = Counter(a)
print(my_counter)
# Counter({'c': 12, 'a': 8, 'b': 3})     all the dictionary functions work in this
print(my_counter.most_common(1))
# [('c', 12)]
print(list(my_counter.elements()))  #element() returns an itertool of all known elements in Counter object
# ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
# Counter object has MANY functions... like update(), most_common()
my_counter.update()
my_counter.most_common()



# ------------ deque -----------------------------------------------------------
# a double ended queue, can add/remove elements from both ends
# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=WL&index=7  - under collections chapter
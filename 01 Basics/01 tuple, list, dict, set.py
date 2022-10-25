#Tuples (), immutable
tuple1 = ("disco",10,1.2)
print(type(tuple1))        #:<class 'tuple'>

    #one element tuple
a_singleton_tuple = ("red",)    # note the comma

    #indexing
print(tuple1[0],tuple1[-1])       #:disco 1.2
tuple2 = tuple1 + ("hard rock",11)
print(tuple2)       #:('disco', 10, 1.2, 'hard rock', 11)

    #mutable objects in tuple are still mutable
ex_tuple = ('ele1', [1, 2, 3])
ex_tuple[1][2] = 55
print(ex_tuple)         #('ele1', [1, 2, 55])

    #slcing syntax arr[start:stop:step]
tuple3 = (0,1,2,3,4,5)
print(tuple3[1:3])       #:(1, 2)
print(tuple3[0:6])      #:(0, 1, 2, 3, 4, 5) - NB! last index is one larger
#than the length of the tuple

    #reverse slice a subset
print(tuple3[::-1])		#(5, 4, 3, 2, 1, 0)
print(tuple3[:1:-1])	#(5, 4, 3, 2) 	#NB! index 1 is not included
print(tuple3[4:1:-1])	#(4, 3, 2)		#NB! index 1 is not included
    
    #len()
print(len(tuple3))      #6
    
    #immutable. each variable does not contain a tuple but reference
    #the same immutable tuple object. 
Ratings1 = (10,9,6,5,10,8,9,6,2)
Ratings2 = Ratings1    #Aliasing: Ratings2 now refer to the same tuple object
print(id(Ratings1))     #1626097282736
print(id(Ratings2))     #1626097282736
#Ratings1[2] = 4 #immutable #TypeError: 'tuple' object does not support item assignment
Ratings1 = (2,10,1)     #Ratings1 now refer to a different tuple object
RatingsSorted = sorted(Ratings2)    #sorted() returns a new list, can assign List to a Tuple
     # The sorted() function will create a new list (not Tuple), i.e. Ratings2 is unchanged    
     # The sort() function will modify the list it is called on. 
myList = [3, 2, 1]
myList.sort()           #sort() changes myList
print(myList)           #[1, 2, 3]
print(RatingsSorted)    #[2, 5, 6, 6, 8, 9, 9, 10, 10]
print(Ratings2)         #(10, 9, 6, 5, 10, 8, 9, 6, 2)
myTuple = [1,2,3]       #can assign List to a Tuple
print(myTuple)
print(type(RatingsSorted))      
    
    #nesting:tuple can contain other tuples and complex data types
nestedTuple = (1,2,("pop","rock"),(3,4),("disco",(1,2)))
print(nestedTuple[2])    #('pop', 'rock')
print(nestedTuple[2][1])    #rock
    
    #index - find 1st index of 2
print(nestedTuple.index(2))     #1

# -------------------------------------------------------------------

#List [], mutalbe

# Difference between List append() and List extend() method
# append() adds an single object to the list
# extend() unpacks the passed object and adds all elements in that object individually to the list

# append() method 
a = [1,2]
b = [3,4]
a.append(b)		#append() adds one element to the list
print("Using append() method", a)	#[1, 2, [3, 4]]

# extend() method
x =[1,2]
y= [3,4]
x.extend(y)		#extend() adds multiple elements
print("Using extend() method", x)	#[1, 2, 3, 4]

sample_list = []
sample_list.extend('abc')       #extend() unpacks the string and pass each char individually
print(sample_list)              #['a', 'b', 'c']

# plus assignment, augmented assignment, concatenate merge the 2 lists, works like extend()
c =[1,2]
d = [3,4]
print(c + d)      #[1, 2, 3, 4]   #concatenate works like extend()
c += d
print("Using augmented assignment method", c)	#[1, 2, 3, 4]

    #mutable
myList1 = [2, 3, 5, 7, 11, 13, 17, 19]
myList1[0] = "hard rock"    #['hard rock', 3, 5, 7, 11, 13, 17, 19]
    
    #delete
del myList1[0]      #[3, 5, 7, 11, 13, 17, 19]
del myList1[0:2]    #[7, 11, 13, 17, 19]
myList1[2:5] = []   #[7, 11]
    #delete the entire list
myList1.clear()     #[]
myList1[:] = []     #[]  NB! this is not assignment, as pointed object is actually an empty list (by value)
del myList1[:]      #works the same way


    #split      string.split() separates a string into list based on
    #argument, default delimiter is space. 
print("Hello Mike".split())     #['Hello', 'Mike']
print("A,B,C,D".split(","))     #['A', 'B', 'C', 'D']
    
    #aliasing - multiple variables refer to the same object
myList1 = ["hard rock",10,1.2]
myList2 = myList1       #aliasing      #['hard rock', 10, 1.2]
myList2[0]="banana"     #changing myList2 changes myList1
print(myList1)          #side effect   #['banana', 10, 1.2]
    
    #cloning - avoid aliasing
myList1 = ["hard rock",10,1.2]
myList2 = myList1[:]    #myList2 points to a new object of the cloned list
myList1[0] = "banana"   #myList2 will not change
print(myList2)          #['hard rock', 10, 1.2]


# --------------------------------------------------------------------

#Filter list, Map list, Reduce list        "Intro to Python" p182

#filter()
#filter(function or None, iterable) --> filter object
#Return an iterator yielding those items of iterable for which function(item) is true. 
#If function is None, return the items that are true.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(x):
    """Returns True only if x is odd."""
    return x%2 != 0

print(list(filter(is_odd, numbers)))    #filter() takes another fxn as argument, see higher order function
# [1, 3, 5, 7, 9]

print(list(filter(lambda x: x%2 != 0, numbers)))    #inline lamba expression
# [1, 3, 5, 7, 9]

#list comprehension can generate the same effect
print([item for item in numbers if is_odd(item)]) 
# [1, 3, 5, 7, 9]

#map()
numbers =  [0, -1, 2, 3, -4]

def square_func(n):
    return n*n
 
new_numbers = list(map(square_func, numbers))
#[0, 1, 4, 9, 16]
new_numbers1 = list(map(lambda x: x*x, numbers))
#[0, 1, 4, 9, 16]


#reduce()
# https://docs.python.org/3/library/functools.html
from functools import reduce
lis = [1, 3, 5, 6, 2, ]
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(reduce(lambda a, b: a+b, lis))
# The sum of the list elements is : 17
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))
# The maximum element of the list is : 6

# --------------------------------------------------------------------

#zip() - for parallel iteration
#iterate over multiple iterables at the same time
#unpack pairing elements into a iteratable zip class of tuples
#https://realpython.com/python-zip-function/

#zip(*iterables) --> A zip object yielding tuples until an input is exhausted.
#The zip object yields n-length tuples, where n is the number of iterables passed as 
#positional arguments to zip(). 
#The i-th element in every tuple comes from the i-th iterable argument to zip(). 
#This continues until the shortest argument is exhausted.

#zip iterator, like other object iterators can only be used once, then it's exhausted
# https://www.youtube.com/watch?v=zdJEYhA2AZQ

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(type(zipped))     #<class 'zip'>
print(zipped)           #<zip object at 0x00000236638B7500>

zipped_list=list(zipped)
print(zipped_list)      #[(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zip(x, y))    # *zip(x, y) is unpacked into (1,4), (2,5), (3,6), i.e. 3 tuples
x == list(x2) and y == list(y2)     #True

#what is length of iterables do not match? zip() continues until the shortest argument is exhausted
x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
zipped = zip(x, y)
zipped_list=list(zipped)
print(zipped_list) 
#[(1, 4), (2, 5), (3, 6)]

#use case
names = ['Bob', 'Mike', 'Peter']
grades = [3.5, 4.0, 3.75]

for name, grades in zip(names, grades):
    print(f'Name={name}; Grades={grades}')
# Name=Bob; Grades=3.5
# Name=Mike; Grades=4.0
# Name=Peter; Grades=3.75


# ----------------------------------------------------------------------

#Multidimensional list

a = [[77, 68, 86, 73], 
     [96, 87, 89, 81], 
     [70, 90, 86, 81]]

#by convention, 1st idx is row, 2nd idx the element's column
print(a[1][2])      #89

for row in a:
    for item in row:
        print(item, end=' ')
    print()
# 77 68 86 73 
# 96 87 89 81 
# 70 90 86 81 

for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}]={item} ', end=' ')
    print()
# a[0][0]=77  a[0][1]=68  a[0][2]=86  a[0][3]=73  
# a[1][0]=96  a[1][1]=87  a[1][2]=89  a[1][3]=81  
# a[2][0]=70  a[2][1]=90  a[2][2]=86  a[2][3]=81  

# -------------------------------------------------------------------

#Dictionary - {} key value pairs, keys are immutable+unique
#immutable objects are: strings, integer, float, tuple, bool
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), (0, 1): 6}

#key access
print(Dict["key1"])     #1      #access value by the key     
print(Dict[(0,1)])      #6
print(Dict.get('key3')) #[3, 3, 3]  #.get() prevents KeyError exception, if not found, return None by default
print(Dict.get('nonkey', 'key not found'))  #key not found
print("key3" in Dict)           #True  
print('nonkey' not in Dict)     #True

# is dictionary empty?
if Dict:        # a non-empty dictionary evalutes to True
    print('Dict is not empty')
else:
    print('Dict is empty')
# Dict is not empty
empty_Dict = {}
bool(Dict)          #True
bool(empty_Dict)    #False

#add, delete entry
Dict["added"] = "extra"   #add an entry of "added":"extra"      bc 'added' key does not already exist
print(Dict)
# {'key1': 1, 'key2': '2', 'key3': [3, 3, 3], 'key4': (4, 4, 4), (0, 1): 6, 'added': 'extra'}
del Dict["key4"]     #delete an entry
print(Dict)        
# {'key1': 1, 'key2': '2', 'key3': [3, 3, 3], (0, 1): 6, 'added': 'extra'}

#update() - merging dictionaries 
d = {1: "one", 2: "three"}
d1 = {2: "two"}
d2 = {4: 'four', 5: 'five'}

d.update(d1)    # updates the value of key 2
print(d)        #{1: 'one', 2: 'two'}

d1 = {3: "three"}
d.update(d1)    # adds element with key 3
print(d)        #{1: 'one', 2: 'two', 3: 'three'}

d.update(d2)    # adds more than one key-value pair
print(d)        #{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


#iteration
#.items() unpacks each key-value pair as a tuple

for key, value in Dict.items():
    print(f'key = {key}, value = {value}')

# key = key1, value = 1
# key = key2, value = 2
# key = key3, value = [3, 3, 3]
# key = (0, 1), value = 6
# key = added, value = extra

#iterate through keys
for key in Dict:            # Dict.keys() give the same effect
    print(key, end=', ')
# key1, key2, key3, (0, 1), added,

for value in Dict.values():
    print(value, end=', ')
# 1, 2, [3, 3, 3], 6, extra,


#Counting frequency in a list using dictionary get() method
#if word is not in freqMap, get() returns 1, thus adding an entry key to dict
freqMap = {}
wordList = ['one', 'two', 'two', 'three', 'three', 'three']
for word in wordList:
  freqMap[word] = freqMap.get(word, 1) 

print(freqMap)
# {'one': 1, 'two': 2, 'three': 3}


# Loop through dictionary in key order
di = {'b': 2, 'c': 3, 'a': 1}
for k, v in sorted(di.items()):     #sorted() returns a list of key:value pair tuples
    print(k, v)
# a 1
# b 2
# c 3

# Loop through dictionary in value order
di = {'a': 3, 'b': 1, 'c': 2}
tmp = sorted( [(v, k) for k, v in di.items()] )
print(tmp)
# [(1, 'b'), (2, 'c'), (3, 'a')]


# -----------------------------------------------------------------------

#Sets - {}
#unordered, do not record element position, only have unique elements
#contain only immutable elements, eg strings, ints, floats, tuples
#Dictionary and sets are unordered
#Dictionary does not support slicing
#Set does not support indexing and slicing

mySet = {1, 4, 5, 1}    #duplicates in set delaration does not cause error
print(mySet)    #{1, 4, 5} when set created, duplicate items are not ignored

#duplicate elimination
mySet1 = set([1, 1, 1, 2, 3])  #{1, 2, 3}   #convert list to a set, no duplicates
print(mySet1) 

mySet1.add(4)   #{1, 2, 3, 4}    #no append(), extend(), b/c no indexing
mySet1.remove(2)    #{1, 3, 4}
print(1 in mySet1)  #True


#Set comparison
{1, 3, 5} == {3, 5, 1}      #True
{1, 3, 5} != {3, 5, 1}      #False

#proper subset
# < operator tests the left set is a proper subset of the right set
#i.e. all elements in the left operand are in the right operand, and the sets are not equal
{1, 3, 5} < {3, 5, 1}       #False     
{1, 3, 5} < {7, 3, 5, 1}    #True
{1, 3, 5} <= {3, 5, 1}      #True
{1, 3} <= {3, 5, 1}         #True

#proper superset
# > operator tests the left set is a proper superset of the right set
#i.e. all elements in the right operand are in the left operand, and the sets are not equal
{1, 3, 5} > {3, 5, 1}       #False
{1, 3, 5, 7} > {3, 5, 1}    #True
{1, 3, 5} >= {3, 5, 1}      #True
{1, 3, 5} >= {3, 1}         #True
{1, 3} >= {3, 1, 7}         #False

{1, 3, 5}.issubset({3, 5, 1})   #True
{1, 2}.issubset({3, 5, 1})      #False

{1, 3, 5}.issuperset({3, 5, 1})     #True
{1, 3, 5}.issuperset({3, 2})        #False


#Mathematical Set operations

# Union 
{1, 3, 5} | {2, 3, 4}           #{1, 2, 3, 4, 5}
{1, 3, 5}.union([2, 3, 4])      #{1, 2, 3, 4, 5}

# Intersection 
{1, 3, 5} & {2, 3, 4}           #{3}
{1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4])   #{1, 3}

# Difference 
{1, 3, 5} - {2, 3, 4}           #{1, 5}
{1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4])     #{1, 5, 7}

# Symmetric Difference 
# a set consisting of elements of both sets that are not in common with one another
{1, 3, 5} ^ {2, 3, 4}           #{1, 2, 4, 5}
{1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4])       #{1, 2, 4, 5, 7}

# Disjoint
# two sets are disjoint if they do not have any common elements
{1, 3, 5}.isdisjoint({2, 4, 6})     #True
{1, 3, 5}.isdisjoint({4, 6, 1})     #False


#Mutable mathematical set operations

numbers = {1, 3, 5}

# augmented assignment |= (union), &= (interset), -= (difference), ^= (symmetric difference)
numbers |= {2, 3, 4}        #{1, 2, 3, 4, 5}

# add, remove elements
numbers.update(range(10))   #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numbers.add(17)     #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 17}
numbers.add(3)      #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 17} - adding duplicate does nothing
numbers.remove(3)   #{0, 1, 2, 4, 5, 6, 7, 8, 9, 17}
numbers.pop()       #{1, 2, 4, 5, 6, 7, 8, 9, 17}   - set is unordered, so you don't know which is popped
numbers.clear()     #set()  - empties the set


# ------------------------------------------------------------------------

#unpacking assignment

#tuple
student_tuple = ('Amanda', [1, 2, 3])
name, grades = student_tuple            #unpacking a tuple
print(name)
print(grades)
# Amanda
# [1, 2, 3]

#strings
first, second = 'hi'                #unpacking a string
print(f'{first}    {second}')
#h    i

#list
num1, num2, num3 = [2, 3, 5]        #unpacking a list
print(f'{num1}    {num2}    {num3}')
#2    3    5

#range
num1, num2, num3 = range(10,40,10)  #unpacking range
print(f'{num1}    {num2}    {num3}')
#10    20    30


#-------------------------------------------------------------------------

#Search

numbers = [3, 7, 1, 4, 2, 8, 5, 6]

#index - returns the index of the searched element
print(numbers.index(5))         #6
print(numbers.index(16))        #ValueError: 16 is not in list

# in, not in    for conditionals
1000 in numbers         #False
5 in numbers            #True
1000 not in numbers     #True
5 not in numbers        #False
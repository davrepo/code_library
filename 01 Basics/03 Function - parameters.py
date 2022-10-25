#functions
# parameters: are the variables inside parentheses while defining a function
# arguments: are the values passed for function invokation

def fxn(a):     #a is parameter
    return a+1

c = fxn(3)      # 3 is argument
print("c is", c)        

# ---------------------------------------------------------------------------

def NoWork():       #a fxn that does nothing, returns None
    pass            #Python does not allow fxn without body
                    #return keyword is not compulsary
def NoWork1():
    return None

print(type(d))      #<class 'NoneType'>
print(NoWork())     #None
print(NoWork1())    #None

# -----------------------------------------------------------------------------

#Positional arguments vs Keyword arguments, Default parameters
def foo(a, b, c):
    print(a, b, c)

#Positional arg: are arguments passed to fxn in a specific order
foo(1, 2, 3)        #1 2 3
#Keyword argument: can pass arguments out of order using keywords
foo(b=1, a=3, c=2)  #3 1 2
#Mixed
foo(1, c=2, b=3)    #1 3 2
#Cannot use positional argument after a keyword argument
# foo(b=2, 1, 3)
# SyntaxError: positional argument follows keyword argument


#default parameter:
def foo(a, b=4):    # b has default value of 4
    print(a, b)

foo(1)      #1 4
# default parameter must be at the end, i.e. non-default parameter cannot follow default parameter
# def foo(a=4, b):
#     print(a, b)



# ----------------------------------------------------------------------------

# Variable length arguments, *args, **args + Packing arguments
# *arg is positional argument. **kwarg is keyword argument
# * is packing an unpacking operator. Same for **
    # here we show only packing. For unpacking, see "01b unpacking operator"
# * can be used with any iterable (eg tuple, list, string); ** can only be used on dictionary
# arg and kwarg are conventions. Any identifier can be used
# https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749
# https://calmcode.io/args-kwargs/introduction.html

# * pack function paramenters into a tuple, can be accessed with indexing etc. 
def foo(*args):
    print(args[0], end = " ")
    args = list(args)   # Convert args tuple to a list so we can modify it
    args[1] = 'Academy'
    print(args)
 
foo('Python', 'programming', 'prep')     # passed into foo() are positional arguments, without keywords
#Python ['Python', 'Academy', 'prep']

# ** pack function parameters into a dictionary
def printDictionary(**kwargs):
    print(kwargs)       # printing the kwarg dictionary
    for key in kwargs:  #iterate through the dictionary keys
        print(key + " : " + kwargs[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
# {'Country': 'Canada', 'Province': 'Ontario', 'City': 'Toronto'}
# Country : Canada
# Province : Ontario
# City : Toronto


#-------------------------------------------------------------------------------


# Ordering arguments
# When ordering arguments within a function call, arguments need to occur in a particular order: 
    # Formal positional arguments
    # *args
    # Keyword arguments
    # **kwargs
# i.e. function looks like this
def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
    pass

# The first two values are given to a and b. The remaining values are stored in the args tuple.
def arg_printer(a, b, *args):
   print(f'a is {a}')
   print(f'b is {b}')
   print(f'args are {args}')
   
arg_printer(3, 4, 5, 8, 3)
# a is 3
# b is 4
# args are (5, 8, 3)

# See ordering. Positional arguments must be passed before keyword argument.
arg_printer(a=4, 2, 4, 5)   # SyntaxError: positional argument follows keyword argument
# arg_printer does not allow keyword 
arg_printer(4, 2, 4, 5, 7, a=8)   # TypeError: arg_printer() got multiple values for argument 'a'

# adding keyword argument
def addition(a, b, *args, option=True):
   result = 0
   if option:
      for i in args:
      result += i
      return a + b + result
   else:
      return result

print(addition(1,4,5,6,7))      #23
print(addition(1,4,5,6,7, option=False))    #0

# **kwargs collect all the keyword arguments that are not explicitly defined. 
# Thus, it does the same operation as *args but for keyword arguments
def arg_printer(a, b, *args, option=True, **kwargs):
    print(a)
    print(b)
    print(args)
    print(f'Option is: {option}')
    print(kwargs)

arg_printer('a', 'b', 'c', 'd', param1 = 5, param2 = 6)    # option takes on default value True
# a
# b
# ('c', 'd')                  # *args pack remaining parameters into tuple
# Option is: True
# {'param1': 5, 'param2': 6}  # **kwargs packing remaining parameters into dictionary

# can pass keyword argument after **kwargs, actually anywhere as long as after *args
arg_printer('a', 'b', 'c', 'd', param1 = 5, param2 = 6, option=False)
# a
# b
# ('c', 'd')
# Option is: False              
# {'param1': 5, 'param2': 6}

# arg_printer('a', 'b', option=False, 'c', 'd', param1 = 5, param2 = 6)
# SyntaxError: positional argument follows keyword argument


#--------------------------------------------------------------------------------

#Forced keyword parameter
def foo(a, b, *, c, d):      # all parameters after * must be keyword arguments
    print(a, b, c, d)

foo(1, 2, c=3, d=4)     #1 2 3 4
# foo(1, 2, 3, 4)       #TypeError: foo() takes 2 positional arguments but 4 were given

def foo(*args, last):
    for arg in args:
        print(arg, end = ' ')
    print(last)

foo(1, 2, 3)        #TypeError: foo() missing 1 required keyword-only argument: 'last'
foo(1, 2, 3, last=100)  #1 2 3 100
  

# --------------------------------------------------------------------------------
#Annotations
#https://www.geeksforgeeks.org/function-annotations-python/
def increment(n: int) -> int:
    ''' increment() takes an int, returns an int'''
    return n+1
count: int = 0

# Python program to print Fibonacci series
def fib(n:'int', output:'list'=[])-> 'list':
    if n == 0:
        return output
    else:
        if len(output)< 2:
            output.append(1)
            fib(n-1, output)
        else:
            last = output[-1]
            second_last = output[-2]
            output.append(last + second_last)
            fib(n-1, output)
        return output
print(fib(5))
# [1, 1, 2, 3, 5]
print(fib.__annotations__)
# {'n': 'int', 'output': 'list', 'return': 'list'}


# --------------------------------------------------------------------------------


# Pass-by-value, pass-by-reference
# Pass-by-value: function receives a COPY of the argument's value and works exclusively with that copy
    # this may be slow
# Pass-by-reference: function can ACCESS the argument's value and modify the value if it's mutable
    # this is fast
# Python arguments are always passed by reference, hence can modify passed mutable objects. - "Intro to Python", p142


# Passing immutable object as argument - no global effect
def foo(x):
    x = 5       # var is passed here, b/c var is int immutable, a local variable is created

var = 10
foo(var)
print(var)      # 10
# var is int, immutable, instead foo() will create a local variable called x, 
# despite when var is passed as argument


# Passing mutable object as argument - yes global effect
def foo(a_list):
    a_list.append(4)
    
my_list = [1, 2, 3]
foo(my_list)
print(my_list)  #[1, 2, 3, 4]

# Immutable object within a mutable object can also be changed
def foo(a_list):
    a_list[0] = -100
    
my_list = [1, 2, 3]
foo(my_list)
print(my_list)  #[-100, 2, 3]

# Rebinding reference - no more global effect
def foo(a_list):
    a_list = [100, 200, 300]    # rebinding reference, my_list, to a local variable
    a_list.append(4)
    
my_list = [1, 2, 3]
foo(my_list)
print(my_list)      #[1, 2, 3]

#Augmented assignment - yes global effect
def foo(a_list):
    a_list += [100, 200, 300]    
    
my_list = [1, 2, 3]
foo(my_list)
print(my_list)      #[1, 2, 3, 100, 200, 300]

#However, plus assignment is rebinding - no global effect
def foo(a_list):
    a_list = a_list + [100, 200, 300]    
    
my_list = [1, 2, 3]
foo(my_list)
print(my_list)      #[1, 2, 3]


# Mutable object as Default argument
# Least astonishment - means things should work exactly as you expect them to
# https://www.youtube.com/watch?v=_JGmemuINww
# https://www.youtube.com/watch?v=kgkms3xF5ZE
# Default values (here, the empty list []) are only created once at first function call. 
# If that value is a mutable object and got modified in the function body,
# in subsequence function calls, default value resumes an updated value (and is passed to a). 
# if that default parameter is an immutable object, it cannot be modified, and 
# hence it resumes the same value. 
# This is because in Python, functions are first class objects, i.e. they maintain their states
# Default value is an attribute of the function object, once you modify it, it sticks in memory. 

def foo(num, a=[]):     #Goal: pass a as an list, if a not specified, make an empty list
    a.append(num)
    return a

#foo() only creates that default empty list one time
print(foo.__defaults__)     #([],)  => Here shows "default" for foo() is an empty list. 
b = foo(5)      
print(b)        # [5]
print(foo.__defaults__)     #([5],) => "Default" for foo() is updated in previous fxn body call
                            # and in future calls, this value [5] will be passed as default to a. 
c = foo(5)
print(c)        # [5, 5]
print(foo.__defaults__)     #([5, 5],)
d = foo(5)       
print(d)        # [5, 5, 5]
print(foo.__defaults__)     #([5, 5, 5],)
print(id(b) == id(c) == id(d) == id(foo.__defaults__[0]))   #True
#So in each function call, since no argument is passed as in foo() for a, 
#"default" is passed to a, then passed to b, c, d, respectively. 
# so b, c, d, and "default" all point to the same object, the default list. 
# To hack it:
foo.__defaults__[0][:] = []
print(foo.__defaults__)     #([],)
e = foo(5)
print(e)        #[5]


#How to fix it? - change default argument to an immutable object
def foo_fixed(num, a=None):
    if a is None:
        a = []
    a.append(num)
    return a

# None does not change with each function call, bc None is immutable, unlike list
print(foo_fixed.__defaults__)   #(None,)
foo_fixed(5)    #[5]
print(foo_fixed.__defaults__)   #(None,)
foo_fixed(5)    #[5]
print(foo_fixed.__defaults__)   #(None,)
foo_fixed(5)    #[5]

# Example 2:
import time
from datetime import datetime

# datetime.now() gets evaluated one time and get set to "default"
# in subsequent calls, "default" is the original datetime.now() value set the first time
def display_time(time_to_print = datetime.now()):
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

print(display_time.__defaults__)    #(datetime.datetime(2022, 8, 16, 11, 16, 55, 60218),)
display_time()
# August 16, 2022 11:13:15
time.sleep(1)
print(display_time.__defaults__)    #(datetime.datetime(2022, 8, 16, 11, 16, 55, 60218),)
display_time()
# August 16, 2022 11:13:15      <= value is not incrementing despite sleep for 1 sec
time.sleep(1)
print(display_time.__defaults__)    #(datetime.datetime(2022, 8, 16, 11, 16, 55, 60218),)
display_time()
# August 16, 2022 11:13:15

# Fix
def display_time(time_to_print = None):
    if time_to_print is None:
        time_to_print = datetime.now()
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))
    
display_time()
# August 16, 2022 11:21:07
time.sleep(1)
display_time()
# August 16, 2022 11:21:08     
time.sleep(1)
display_time()
# August 16, 2022 11:21:09


# Example 3:
def append_one(value, _list=[]):
    _list.append(value)
    return _list

a = append_one(1)
print(a)
b = append_one(2)
print(b)

# Now, both a and b points to the same list. 
a   #[1, 2]
b   #[1, 2]
id(a)   #1965035380288
id(b)   #1965035380288
append_one.__defaults__     #([1, 2],)
id(append_one.__defaults__[0])  #1965035380288
# This is because "default" is passed to _list, _list is passed to both a and b
# i.e. a and b points to the same object, which is default. 


# Example 4 (Use case): Memoization - Fibonacci implementation
# Memoization: an optimization technique by storing computation results in cache,
# retrieving the same info from the cache the next time it's needed instead of 
# executing expensive function calls. 
# Goal: use default parameter to store memoization. 

import time

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
        memo[n] = value         # function call with unseen argument is stored in memo
    return value

memoization(35)     #('2.149 secs', 14930352)
memoization(36)     #('3.689 secs', 24157817)
memoization(36)     #('0.000 secs', 24157817)
memoization(35)     #('0.000 secs', 14930352)


# ----------------------------------------------------------------------------------


# Multiple inheritance + Method resolution order (MRO)
# https://www.youtube.com/watch?v=X1PQ7zzltz4&list=WL&index=1
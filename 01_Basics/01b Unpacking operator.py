# (*) unpacking operator
    # for positional vs keyword argument, see "03 functions"
    # for packing, see "03 functions"       
# * can unpack iterables eg tuple, list, strings etc to its elements. 
# ** can only unpack dictionary

# https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749
# https://calmcode.io/args-kwargs/introduction.html

# convert range til list
l1 = [range(5)]     
print(l1)
#[range(0, 5)]

l = [*range(5)]     # * unpacking operator
print(l)
#[0, 1, 2, 3, 4]


# unpacking a collection
my_tuple = (1, 2, 3, 4, 5, 6, 7)
i1, *i2, i3, i4 = my_tuple      # the middle part of the tuple gets unpacked into a list in i2
print(i1)   # 1
print(i2)   # [2, 3, 4, 5]
print(i3)   # 6
print(i4)   # 7

# merge containers
my_tuple = (1, 2, 3)
my_list = [4, 5, 6] 
merged_list = [*my_tuple, *my_list]
print(merged_list)
# [1, 2, 3, 4, 5, 6]

dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
merged_dict = {**dict_a, **dict_b}
print(merged_dict)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# unpacking arguments passed to function calls
# Ex 1: unpack collections into func arguments
def foo(a, b, *args, **kwargs):
    print(a, end = ' ')
    for arg in args:    #args is unpacked into an iterable object
        print(arg, end = ' ')
    for key in kwargs:
        print(key, kwargs[key], end = ' ')

foo(1, 2, 3, 4, 5, six=6, seven=7)
# 1 3 4 5 six 6 seven 7 
values = (1, 2, 3, 4, 5)
mydict = {'eight': 8, 'nine': 9}
foo(*values, **mydict)    #NB! * unpacking operator, otherwise passing a tuple + dict
#1 3 4 5 eight 8 nine 9   #NB! ** for dict, otherwise only get keys


# Ex 2: matching parameters with unpacked arguments
def myFun(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
     
# keys in dictionary must be the same as names of parameters
kwargs = {"a" : "One", "b" : "Two", "c" : "Three"}  #dictionary
myFun(**kwargs)     # passing a dictionary into myFun() by unpacking it and pass individual key:value pair
# a: One
# b: Two
# c: Three


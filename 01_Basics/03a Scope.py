# Global variable
# see https://www.programiz.com/python-programming/global-keyword 
    # for global variable across modules 
# When we create a variable inside a fxn, it is local by default.
# When we define a variable outside of a fxn, it is global by default. You don't have to use global keyword.
# We use global keyword to read and write a global variable inside a function.
# Use of global keyword outside a function has no effect.

#can access a global variable inside a fxn... but cannot modify it (see next)
c = 1 # global variable
def add():
    print(c)
add()           #1

# cannot modify a global variable from inside a fxn 
# b/c if identical name, a new local variable is just created inside the function local scope
c = 1 # global variable
def add():
    # c = 0     # adding this line would void exception, then output 2
                # as local c shadows global c, making it inaccessible in the scope of the fxn block
    c = c + 2 # increment c by 2
    print(c)
add()       #UnboundLocalError: local variable 'c' referenced before assignment

# declare global keyword, allows fxn to modify global variable
c = 0 # global variable
def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)
add()
print("In main:", c)
# Inside add(): 2
# In main: 2

# Global in nested function 
# Declared a global variable inside the nested function bar(). 
# Inside foo() function, x has no effect of the global keyword.
# Before and after calling bar(), the variable x takes the value of local variable i.e x = 20
# Outside of the foo() fxn, the variable x will take value defined in the bar() fxn i.e x = 25
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)

# Before calling bar:  20
# Calling bar now
# After calling bar:  20
# x in main:  25

# declare global variable in local scope
artist = "Michael Jackson"

def printer(artist): 
    global internal_var                     #declare global variable within fxn
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

# Michael Jackson is an artist
# Whitney Houston is an artist


def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)

# a = 30
# a = 20
# a = 10

def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)

# a = 30
# a = 30
# a = 30 

# ---------------------------------------------------------------------------

# create a global variable
x = "global"

def foo():
    print("x inside:", x)

foo()
print("x outside:", x)
# x inside: global
# x outside: global


# cannot modify global variable in local scope 
# without first declare that variable with keyword global in local scope
x = "global"

def foo():
    x = x * 2
    print(x)

foo()
# UnboundLocalError: local variable 'x' referenced before assignment


# cannot access local variable outside the scope
def foo():
    y = "local"

foo()
print(y)
# NameError: name 'y' is not defined


# ----------------------------------------------------------------------------

# nonlocal
# The nonlocal keyword is used to work with variables inside nested functions, 
# where the variable should not belong to the inner function but rather
# the entire scope of that function
# it does not however have the global scope
# Use the keyword nonlocal to declare that the variable is not local.

# example with nonlocal keyword
def foo():
  x = "local"
  def foo2():
    nonlocal x
    x = "nonlocal"
  foo2()
  return x

print(foo())

#nonlocal

# example without nonlocal keyword
def foo():
  x = "local"
  def foo2():
    x = "nonlocal"
  foo2()
  return x

print(foo())

#local

# combined example + triple nested fxn
x = "global"

def outer():
    x = "local"

    def inner():
        def innerest():
            nonlocal x
            x = "nonlocal"
            print("innerest:", x)
        innerest()
    
    inner()
    print("outer:", x)

outer()
print("global:", x)

# innerest: nonlocal
# outer: nonlocal
# global: global


# -----------------------------------------------------------------------------

# Scope in control statements
# if control statement is in global scope, then any var defined in control statement have global scope
# if control statement is in function's block, then any var defined in control statement have local scope

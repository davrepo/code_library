#conditional
print("B">"A")      #True  #ASCII, each letter has an int value    
print("BA">"AB")    #True   #in multiple letters, first letter takes precedence

age = 19
if age > 18:        #True bool satisfies condition
    print("age>18")
elif age == 18:
    print ("age==18")
else:
    print("age<18")

if not age<=18:     #False bool satisfies condition, equivalent to if age > 18
    print("age>18")
    
# True: any non-zero value    False: 0
true_val = 5
false_val = 0

if true_val:
    print("passed")
    
# Ternary operator in Python
# condition_true if condition else condition_false
a, b = 10, 20
# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)
# 10


# Refactor if elif chaining with dictionary get()
# Also see Match pattern - a Python 3.10 feature
def foo1(x):
    print('1 is done')

def foo2(x):
    print('2 is done')

def foo3(x):
    print('3 is done')

def foo_default(x):
    print('default')

actions = {1: foo1, 2: foo2, 3: foo3}
# x = None
# while True:
#     x = int(input('Insert which foo to perform (1-3): '))
#     action = actions.get(x, foo_default)
#     action(x)

# get(key, default) - check for key in dict, 
# if key doesn't exist, return default param
x = 2
action = actions.get(x, foo_default)
action(x)
# 2 is done

x = 5
actions.get(x, foo_default)(x)
# default

# -------------------- Switch statement ----------------------------

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None

# Python does not have switch statement, but has first-class functions, which
# you can return. Here we use a dictionary function dict.get()
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

dispatch_if('mul', 2, 8)    #16
dispatch_dict('mul', 2, 8)  #16
dispatch_if('unknown', 2, 8)    #None
dispatch_dict('unknown', 2, 8)  #None
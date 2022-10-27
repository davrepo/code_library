# 'Intro to Python', chapter 9, p322


# ------------------ Writing a file ----------------------------------------
# https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

# f.write(string) writes the contents of string to file
    # returns the num of chars written

# Creating a file
# with keyword handles resource deallocation automatically, 
# i.e. do not need finally clause to close the file
with open('accounts.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')

# 100 Jones 24.98
# 200 Doe 345.67


# ------------------ Reading a file ----------------------------------------


#Reading a file
# https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

# read(size: int) reads size byte of text into a single string. 
    # if size omitted, reads the entire file. Size can be more than your memory. 
# readline() reads a single line incldue a newline char into a string
# readlines() - returns a list of every line also include newlines
    # same as list(f)


with open('accounts.txt', mode='r') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    # Looping through file object, reads one line at a time, returns it as a string
    # is the most efficient method of all
    for record in accounts:    
    #split() delimiter is ' ' by default, and automatically discard newline character
        account, name, balance = record.split()     
        print(f'{account:<10}{name:<10}{balance:>10}')
# Account   Name         Balance
# 100       Jones          24.98
# 200       Doe           345.67

#accounts.readlines() can also read entire text file, returns each line as a string
# in a list of strings. But inefficient compared to for loop, 
# bc must complete before you can begin using the list of strings
with open('accounts.txt', mode='r') as accounts:
    for record in accounts.readlines():
        account, name, balance = record.split()     
        print(f'{account:<10}{name:<10}{balance:>10}')
# 100       Jones          24.98
# 200       Doe           345.67

#file-position pointer, seek()
f = open("accounts.txt", "r")
f.seek(6)
print(f.readline()) 
#nes 24.98


# ---------------- File String parsing --------------------------------------
name = input("Enter file:")
if len(name) < 1:
    name = "a_random_file.txt"

with open(name, mode='r') as fh:
    for line in fh:
        line = line.rstrip()
        if not line.startswith('From '): continue
        words = line.split()
        print(words[2])

# ------------------ Read file a chunck at a time ---------------------------------------------

def chunckRead():
    with open('accounts.txt', mode='r') as f:
        size_to_read = 10
        f_contents = f.read(size_to_read)
        while len(f_contents) > 0:
            print(f_contents, end='*')
            f_contents = f.read(size_to_read)

def chunkReader():
    with open('accounts.txt', mode='rb') as f:
        while (chunk := f.read(10)) != b'':   # := is walrus operator, assigns value to chunk and can use it
            print(f'chunk: {chunk}')

# ----------------- Exception ----------------------------------------------

while True:
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1 / number2
    # can't convert non-numeric value + division by zero
    except (ValueError, ZeroDivisionError):     # must enclose exceptions in a tuple, i.e. ()    
        print('Error')
    else:                   # executes only if no exceptions occur
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
        break               # terminate the loop
    finally:
        print('finally always executes regardless, used for release resources')


try:
    print('try suite that raises an exception')
    int('hello')
    print('this will not execute')
except ValueError:
    print('a ValueError occurred')
else:
    print('else will not execute because an exception occurred')
finally:  
    print('finally always executes')
# try suite that raises an exception
# a ValueError occurred
# finally always executes

# Combining with Statements and try…except Statements 
try:
    with open('gradez.txt', 'r') as accounts:
        pass
except FileNotFoundError:
    print('The file name you specified does not exist')
# The file name you specified does not exist


#raise exception
def positiveNumber(num):
    if num < 0:
        raise ValueError('number must be >= 0')
    else:
        print(f'Number is {num}')

positiveNumber(5)       #Number is 5
positiveNumber(-6)      #ValueError: number must be >= 0


#make your own exception
class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    else:
        pass

test_value(200)
# ValueTooHighError: value is too high

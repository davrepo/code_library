print("double quotes")
print('single quotes')

#escape characters
#   \n new line; \t tab; \\ is \; \" is "; \' is '

#line break     \ in string
print('''this is a long string, so we \
split it over two lines''')

#input
# myName = input("What's your name? ")
# print(myName)

#input always returns string, use type casting to convert
value1 = int(input("Enter first number: "))
value2 = int(input("Enter first number: "))
print(value1 + value2)

#instead of newline after each int, end=" ", means space after each int. 
#end= is a keyword argument in print constructor. end="\n" by default
for i in range(5):      
    print(i, end="  ")         #0  1  2  3  4 

#keyword argument sep= , separator
print(10, 20, 30, sep=', ')     #10, 20, 30

#when separator is not specified, it uses space as default
print('welcome', 'to', 'Python')    #welcome to Python

# ------------------- string format, f-string ----------------------------

# {} is placeholder
num1 = 5
num2 = 3                
print(f'{num1} times {num2} is {num1 / num2:.2f}')  #2f means print to 2 decimal precision
#5 times 3 is 1.67

#explicit call format() method
number1 = 'One'
number2 = 'Two'
number3 = 'Three'

# default(implicit) order
default_order = "{}, {} and {}".format(number1,number2,number3)
print('\n--- Default Order ---')
print(default_order)
# One, Two and Three

# order using positional argument
positional_order = "{1}, {0} and {2}".format(number1,number2,number3)
print(positional_order)
# Two, One and Three

# order using keyword argument
keyword_order = "{i}, {j} and {k}".format(j=number1,k=number2,i=number3)
print(keyword_order)
# Three, One and Two

# -----------------------------------------------------------------------------

#alignment  ("intro to Python", p105)
principle = 1000
rate = 0.05
for year in range(1, 6):
    amount = principle * (1 + rate) ** year
    print(f'{year:>2}{amount:>10.2f}')  
# (>) means right aligned
# year:>2   means right aligned, field width 2
# amount:>10.2f     means right aligned, field width 10, 2 decimal points

 # 1   1050.00
 # 2   1102.50
 # 3   1157.63
 # 4   1215.51
 # 5   1276.28
    
# Regular expression

# https://docs.python.org/3/howto/regex.html
# https://regexone.com/
# ^           Matches the beginning of a line
# $           Matches the end of the line
# .           Matches any character
# \s          Matches whitespace
# \S          Matches any non-whitespace characters
# *           Repeats a character zero or more times
# *?          Repeats a character zero or more times (non-greedy)
# +           Repeats a character one or more times
# +?          Repeats a character one or more times(non-greedy)
# [aeiou]     Matches a single character in the listed set
# [^XYZ]      Matches a single character not in the listed set
# [a-z0-9]    The set of characters can include a range
# (           Indicates where string extraction is to start
# )           Indicates where string extraction is to end

string.find('sub')    # returns the index of first occurance
string.startswith('sub')    # returns True/False
re.search('^sub', string)   # returns True/False
findall()     #extracts substrings in a list 

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x) 
print(y)
['2', '19', '42']


# Greedy matching - * and + push outward in both directions (greedy)
# to match the largest possible string

import re
x ='From: stephen@gmail.com Sat Jan 5 09:14:16 2022'
y = re.findall('^F.+:', x)      # greedy match
print(y)
# ['From: stephen@gmail.com Sat Jan 5 09:14:']
z = re.findall('^F.+?:', x)     # non-greedy match
print(z)
# ['From:']

# find the substring, but extract only what's in ()
a = re.findall('^From: (\S+?@\S+)', x)   
print(a)
# ['stephen@gmail.com']

# Dual Split pattern - cut both ways
b = re.findall('From.*@([^ ]*)', x)       # [^ ] == match non-blank char
print(b)
# ['gmail.com']

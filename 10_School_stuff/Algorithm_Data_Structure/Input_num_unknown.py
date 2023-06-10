# for each line, there are 2 inputs, s and t, separated by a space
# there is unknown number of lines
# s and t are non-negative integers, between 0 and 10^15
# output absolute value of their difference

import sys

# sys.stdin is a file object, it reads one line at a time by default 
# when used in a loop or with the readline() method.

for i in sys.stdin:
    s, t = i.split()
    print(abs(int(s) - int(t)))
    
# alternative implementation
# while True:
#     line = sys.stdin.readline()
#     if line:
#         s, t = line.split()
#         print(abs(int(s) - int(t)))
#     else:
#         break


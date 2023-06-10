from itu.algs4.fundamentals.stack import Stack

class BalanceStack():
    
    def __init__(self, string_list):
        self._string_list = string_list
        self._stack = Stack()
        self._left = ['(', '[', '{']
        self._right = [')', ']', '}']
        self._left_to_right = {')': '(', ']': '[', '}': '{'}
    
    def isBalanced(self):
        for char in self._string_list:
            if char in self._left:
                self._stack.push(char)
            elif char in self._right:
                if self._stack.is_empty():
                    return False
                if self._stack.pop() != self._left_to_right[char]:
                    return False
        return self._stack.is_empty()
        

string = input()
string_list = list(string)
test = BalanceStack(string_list)
if test.isBalanced():
    print("1")
else:
    print("0")

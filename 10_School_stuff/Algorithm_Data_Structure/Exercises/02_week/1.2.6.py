# Concatenate string s with itself and store the result in a new string, say s_double.
# Check if t is a substring of s_double.
# If t is a substring of s_double, then s and t are circular shifts of one another.
# O(n), where n is length of string s, as we only need to concatenate and search the string once

def is_circular_shift(s, t):
    s_double = s + s
    return t in s_double

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        
    def insertAfter(self, node1, node2, current=None):
        if node1 is None or node2 is None:
            return
        
        if current is None:
            current = self.first
            
        if current is node1:
            node2.next = node1.next
            node1.next = node2
        else:
            self.insertAfter(node1, node2, current.next)


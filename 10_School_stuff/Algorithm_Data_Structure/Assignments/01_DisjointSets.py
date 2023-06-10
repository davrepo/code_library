from itu.algs4.fundamentals.uf import UF

# from typing import List

class AugmentedUF(UF):
    
    def _children(self, s: int):
        """
        Returns a list of direct children (1 layer deep) of element s.
        :param s: the integer representing one element
        :return: a list of direct children of element s
        """
        self._validate(s)
        children = []
        for i, parent in enumerate(self._parent):
            if i == s:
                continue
            if parent == s:
                children.append(i)
        return children
    
    def move(self, s: int, t: int):
        """
        Edges cases:
        (1) s does not have children, i.e. s is a leaf node
        (2) s is a root node
        (3) s has children and is not root node
        """
        self._validate(s)
        self._validate(t)
        
        root_t = self.find(t)
        root_s = self.find(s)
        s_children = self._children(s)
        
        if self.connected(s, t):
            return
        
        # if s has no children, make s point to root of t
        if len(s_children) == 0:
            self._parent[s] = root_t
        else:
            # if s is root:
            if s == self._parent[s]:
                root_s = s_children[0]
            for child in s_children:
                self._parent[child] = root_s
            self._parent[s] = root_t
        

def initialize_tree(n):
    return AugmentedUF(n)
    

def operation_0(s, t, tree):
    if tree.connected(s, t):
        print("1")
    else:
        print("0")     


def operation_1(s, t, tree):
    if tree.connected(s, t):
        return
    else:
        tree.union(s, t)


def operations_2(s, t, tree):
    tree.move(s, t)


input_value = input().split()
n = int(input_value[0])
m = int(input_value[1])
tree = initialize_tree(n)


for i in range(m):
    inputs = input().split()
    operation = inputs[0]
    if operation == "0":
        operation_0(int(inputs[1]), int(inputs[2]), tree)
    elif operation == "1":
        operation_1(int(inputs[1]), int(inputs[2]), tree)
    elif operation == "2":
        operations_2(int(inputs[1]), int(inputs[2]), tree)
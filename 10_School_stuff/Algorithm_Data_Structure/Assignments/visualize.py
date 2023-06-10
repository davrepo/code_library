from itu.algs4.fundamentals.uf import UF

from typing import List

class AugmentedUF(UF):
    
    def _children(self, s: int) -> List[int]:
        """
        Returns a list of direct children (1 layer deep) of element s.
        :param s: the integer representing one element
        :return: a list of direct children of element s
        """
        self._validate(s)
        children = []
        for i, parent in enumerate(self._parent):
            if parent == s:
                children.append(i)
        return children
    
    def move(self, s: int, t: int) -> None:
        """
        find(s) has the side effect of making children of s point to their grandparent, 
        thus making s a leaf node
        """
        # make s a leaf node
        for child in self._children(s):
            self.find(child)
        # make s point to root of t
        t_root = self.find(t)
        self._parent[s] = t_root


def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": { "graph": True },
        "nodes": [
            # { "id": "1", "label": "1" },
            # { "id": "2", "label": "2" }
            { "id": str(i), "label": str(i) } for i, value in enumerate(arr._parent)
        ],
        "edges": [
            # { "from": "1", "to": "2" },
            # { "from": "1", "to": "3" }
            { "from": str(i), "to": str(value) } for i, value in enumerate(arr._parent)
        ]
    }
    return formatted

# initialize tree
tree = AugmentedUF(10)
serialized = serialize(tree)

sequence = [(9,0), (3,4), (5,8), (7,2), (2,1), (5,7), (0,3), (4,2)]

for i in sequence:
    tree.union(i[0], i[1])
    serialized = serialize(tree)

# move 5 to 6
tree.move(5, 6)
serialized = serialize(tree)

class UF:
    """
    This is an implementation of the union-find data structure - see module documentation for
    more info.
    This implementation uses weighted quick union by rank with path compression by
    halving. Initializing a data structure with n sites takes linear time. Afterwards,
    the union, find, and connected operations take logarithmic time (in the worst case)
    and the count operation takes constant time. Moreover, the amortized time per union,
    find, and connected operation has inverse Ackermann complexity.
    For additional documentation, see Section 1.5 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """

    def __init__(self, n: int) -> None:
        """Initializes an empty union-find data structure with n sites, 0
        through n-1. Each site is initially in its own component.
        :param n: the number of sites
        """
        self._count = n
        self._parent = list(range(n))
        self._rank = [0] * n
        self._array_accesses = 0

    def _validate(self, p: int) -> None:
        # validate that p is a valid index
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError("index {} is not between 0 and {}".format(p, n - 1))

    def union(self, p: int, q: int) -> None:
        """Merges the component containing site p with the component containing
        site q.
        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # make root of smaller rank point to root of larger rank
        if self._rank[root_p] < self._rank[root_q]:
            # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            self._array_accesses += 2
            self._parent[root_p] = root_q
            # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            self._array_accesses += 1
        elif self._rank[root_p] > self._rank[root_q]:
            # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            self._array_accesses += 2
            self._parent[root_q] = root_p
            # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            self._array_accesses += 1
        else:
            self._parent[root_q] = root_p
            self._rank[root_p] += 1
            # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            self._array_accesses += 2

        self._count -= 1

    def find(self, p: int) -> int:
        """Returns the component identifier for the component containing site
        p.
        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self._array_accesses += 1
        while p != self._parent[p]:
            self._parent[p] = self._parent[
                self._parent[p]
            ]  # path compression by halving
            p = self._parent[p]
            # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            self._array_accesses += 5
        return p

    def connected(self, p: int, q: int) -> bool:
        """Returns true if the two sites are in the same component.
        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        return self.find(p) == self.find(q)

    def count(self) -> int:
        return self._count
    
# graph visualizer
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

# grid visualizer
# def serialize(arr):
#     """Serialize an array into a format the visualizer can understand."""
#     formatted = {
#         "kind": {"grid": True},
#         "rows": [
#             {
#                 "columns": [
#                     {"content": str(value), "tag": str(i)} for i, value in enumerate(arr._parent)
#                 ],
#             }
#         ],
#     }
#     return formatted

# initialize tree
tree = UF(10)
serialized = serialize(tree)

sequence = [(9,0), (3,4), (5,8), (7,2), (2,1), (5,7), (0,3), (4,2)]

for i in sequence:
    tree.union(i[0], i[1])
    serialized = serialize(tree)
    print(f'union: {i[0]}-{i[1]}')
    print(f'array accesses so far: {tree._array_accesses}')

tree.find(7)
tree.find(1)
serialized = serialize(tree)
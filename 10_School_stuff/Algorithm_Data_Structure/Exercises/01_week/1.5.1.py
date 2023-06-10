# show contents of id[] array and number of times array is accessed for each input pair
# when use quick-find for sequence 9-0 3-4 5-8 7-2 2-1 5-7 0-3

# from itu.algs4.fundamentals.uf import QuickFindUF

class QuickFindUF:
    """
    This is an implementation of the union-find data structure - see module documentation for
    more info.
    This implementation uses quick find. Initializing a data structure with n sites takes linear time.
    Afterwards, the find, connected, and count operations take constant time but the union operation
    takes linear time.
    For additional documentation, see Section 1.5 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """

    def __init__(self, n: int) -> None:
        """Initializes an empty union-find data structure with n sites, 0
        through n-1. Each site is initially in its own component.
        :param n: the number of sites
        """
        self._count = n
        self._id = list(range(n))
        # variable to keep track of number of array accesses
        self._array_accesses = 0

    def _validate(self, p: int) -> None:
        # validate that p is a valid index
        n = len(self._id)
        if p < 0 or p >= n:
            raise ValueError("index {} is not between 0 and {}".format(p, n - 1))

    def union(self, p: int, q: int) -> None:
        """Merges the component containing site p with the component containing
        site q.
        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        self._validate(p)
        self._validate(q)

        p_id = self._id[p]  # needed for correctness
        # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self._array_accesses += 1
        q_id = self._id[q]  # to reduce the number of array accesses
        # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self._array_accesses += 1

        # p and q are already in the same component
        if p_id == q_id:
            return

        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id
                # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                self._array_accesses += 1
        self._count -= 1
        # *******************************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self._array_accesses += len(self._id)

    def find(self, p: int) -> int:
        """Returns the component identifier for the component containing site
        p.
        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        return self._id[p]

    def connected(self, p: int, q: int) -> bool:
        """Returns true if the two sites are in the same component.
        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        self._validate(p)
        self._validate(q)
        return self._id[p] == self._id[q]

    def count(self):
        return self._count


# graph visualizer
# def serialize(arr):
#     """Serialize an array into a format the visualizer can understand."""
#     formatted = {
#         "kind": { "graph": True },
#         "nodes": [
#             # { "id": "1", "label": "1" },
#             # { "id": "2", "label": "2" }
#             { "id": str(i), "label": str(i) } for i, value in enumerate(arr._id)
#         ],
#         "edges": [
#             # { "from": "1", "to": "2" },
#             # { "from": "1", "to": "3" }
#             { "from": str(i), "to": str(value) } for i, value in enumerate(arr._id)
#         ]
#     }
#     return formatted

# grid visualizer
def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(i)} for i, value in enumerate(arr._id)
                ],
            }
        ],
    }
    return formatted

# initialize tree
tree = QuickFindUF(10)
serialized = serialize(tree)

sequence = [(9,0), (3,4), (5,8), (7,2), (2,1), (5,7), (0,3), (4,2)]

for i in sequence:
    tree.union(i[0], i[1])
    serialized = serialize(tree)
    print(f'union: {i[0]}-{i[1]}')
    # print(tree._id)
    print(f'array accesses so far: {tree._array_accesses}')


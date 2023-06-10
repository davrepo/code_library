from typing import Generic, List, Optional, TypeVar

from itu.algs4.errors.errors import NoSuchElementException
from itu.algs4.stdlib import stdio

Key = TypeVar("Key")


class MinPQ(Generic[Key]):
    def __init__(self, _max: int = 1) -> None:
        self._pq: List[Optional[Key]] = [None] * (_max + 1)
        self._n = 0

    def insert(self, x: Key) -> None:
        if self._n == len(self._pq) - 1:
            self._resize(2 * len(self._pq))
        self._n += 1
        self._pq[self._n] = x
        self._swim(self._n)

    def min(self) -> Key:
        return self._pq[1]

    def del_min(self) -> Key:
        _min = self._pq[1]
        self._exch(1, self._n)
        self._n -= 1
        self._sink(1)
        self._pq[self._n + 1] = None
        if self._n > 0 and self._n == (len(self._pq) - 1) // 4:
            self._resize(len(self._pq) // 2)
        return _min

    def _sink(self, k) -> None:
        while 2 * k <= self._n:
            j = 2 * k
            if j < self._n and self._greater(j, j + 1):
                j += 1
            if not self._greater(k, j):
                break
            self._exch(k, j)
            k = j

    def _swim(self, k) -> None:
        while k > 1 and self._greater(k // 2, k):
            self._exch(k, k // 2)
            k = k // 2

    def _greater(self, i: int, j: int):
        return self._pq[i] > self._pq[j]
    
    def _exch(self, i: int, j: int):
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]

    def _resize(self, capacity: int):
        temp: List[Optional[Key]] = [None] * capacity
        for i in range(1, self._n + 1):
            temp[i] = self._pq[i]
        self._pq = temp

    def is_empty(self) -> bool:
        return self._n == 0

    def size(self) -> int:
        return self._n

    def __len__(self) -> int:
        return self.size()

    def __iter__(self):
        """Iterates over all the items in this priority queue in ascending
        order."""
        copy = MinPQ(self.size())
        for i in range(1, self._n + 1):
            copy.insert(self._pq[i])
        for i in range(1, copy._n + 1):
            yield copy.del_min()


from typing import Generic, Iterator, List, Optional, TypeVar

T = TypeVar("T")

class Node(Generic[T]):     # helper linked list
    def __init__(self):
        self.item: T = None     # type: ignore
        self.next: Optional[Node] = None


class Stack(Generic[T]):    # linked list implementation
    def __init__(self) -> None:
        """Initializes an empty stack."""
        self._first: Optional[Node[T]] = None
        self._n: int = 0

    def is_empty(self) -> bool:
        return self._n == 0

    def size(self) -> int:
        """Returns the number of items in this stack."""
        return self._n

    def __len__(self) -> int:
        return self.size()

    def push(self, item: T) -> None:
        oldfirst = self._first
        self._first = Node()
        self._first.item = item
        self._first.next = oldfirst
        self._n += 1

    def pop(self) -> T:
        if self.is_empty():
            raise ValueError("Stack underflow")
        assert self._first is not None
        item = self._first.item
        assert item is not None
        self._first = self._first.next
        self._n -= 1
        return item

    def peek(self) -> T:
        if self.is_empty():
            raise ValueError("Stack underflow")
        assert self._first is not None
        item = self._first.item
        assert item is not None
        return item

    def __iter__(self) -> Iterator[T]:
        """Returns an iterator in LIFO order."""
        current = self._first
        while current is not None:
            item = current.item
            assert item is not None
            yield item
            current = current.next


class ResizingArrayStack(Generic[T]):   # resizing array implementation
    def __init__(self) -> None:
        self.a: List[Optional[T]] = [None]
        self.n: int = 0

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n

    def __len__(self) -> int:
        return self.size()

    def resize(self, capacity: int) -> None:
        temp: List[Optional[T]] = [None] * capacity
        for i in range(self.n):
            temp[i] = self.a[i]
        self.a = temp

    def push(self, item: T) -> None:
        if self.n == len(self.a):
            self.resize(2 * len(self.a))
        self.a[self.n] = item
        self.n += 1

    def pop(self) -> T:
        self.n -= 1
        item = self.a[self.n]
        self.a[self.n] = None
        if self.n > 0 and self.n <= len(self.a) // 4:
            self.resize(len(self.a) // 2)
        assert item is not None
        return item

    def __iter__(self) -> Iterator[T]:
        i = self.n - 1
        while i >= 0:
            item = self.a[i]
            assert item is not None
            yield item
            i -= 1
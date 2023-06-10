from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")

class Node(Generic[T]):    # helper class to define nodes
    def __init__(self, item: T, next: Optional["Node[T]"]) -> None:
        self.item: T = item     # object content of the node
        self.next: Optional[Node[T]] = next  # the next node pointed to


class Queue(Generic[T]):    # linked list implementation
    def __init__(self) -> None:
        """Initializes an empty queue."""
        self._first: Optional[Node[T]] = None
        self._last: Optional[Node[T]] = None
        self._n: int = 0

    def enqueue(self, item: T) -> None:
        old_last: Optional[Node[T]] = self._last
        self._last = Node(item, None)
        if self.is_empty():
            self._first = self._last
        else:
            assert old_last is not None
            old_last.next = self._last
        self._n += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise Exception("Queue underflow")

        assert self._first is not None
        item = self._first.item
        self._first = self._first.next
        self._n -= 1
        if self.is_empty():
            self._last = None
        return item

    def is_empty(self) -> bool:
        return self._first is None

    def size(self) -> int:
        return self._n

    def peek(self) -> T:
        if self.is_empty():
            raise Exception("Queue underflow")

        assert self._first is not None
        return self._first.item
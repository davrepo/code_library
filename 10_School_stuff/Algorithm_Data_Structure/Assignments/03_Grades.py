import sys
from typing import List, TypeVar

T = TypeVar("T")


def sort(a: List[T]):
    """Rearranges the array in ascending order, using the natural order.
    :param a: the array to be sorted.
    """
    # Sort a[] into increasing order.
    N = len(a)
    for i in range(0, N):
        # Insert a[i] among a[i-1], a[i-2], a[i-3]...
        for j in range(i, 0, -1):
            if not _less(a[j], a[j - 1]):
                break
            _exch(a, j, j - 1)


def _less(v: T, w: T):
    return v < w


def _exch(a: List[T], i: int, j: int):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def _show(a: List[T]):
    # Prints the array on a single line
    for item in a:
        print(item, end=" ")
    print()


def is_sorted(a: List[T]):
    """Returns true if a is sorted.
    :param a: the array to be checked.
    :returns: True if a is sorted.
    """
    for i in range(1, len(a)):
        if _less(a[i], a[i - 1]):
            return False
    return True

number_of_rows = input()

# make a list of tuples, with grade as first element, name as second
tuple_list = []

for i in range(int(number_of_rows)):
    name, grade = input().split()
    tuple_list.append((grade, name))

sort(tuple_list)

for i in range(len(tuple_list)):
    # print only name element
    print(tuple_list[i][1])


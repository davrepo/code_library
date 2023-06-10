import random

def binary_search_standard(x, a):
    lo = 0
    hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2

        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid
        else:
            return mid

    return -1


def binary_search_lowest_index(x, a):
    lo = 0
    hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2

        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid
        elif mid > 0 and a[mid-1] == x:
            hi = mid
        else:
            return mid

    return -1

a = [1, 2, 5, 5, 5, 6, 7, 8, 9, 10]

print(binary_search_standard(5, a)) # 2

b = [1, 1, 1, 2, 3, 4, 5, 6]
print(binary_search_lowest_index(1, b)) # 0
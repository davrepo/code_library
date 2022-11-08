from math import comb
from collections import Counter
def search_pascal_multiples_fast(row_limit):
    myList = [comb(n, k) for n in range(10, row_limit) for k in range(2, int(n/2+1))]
    new_list = [i for i, count in Counter(myList).items() if count > 1]
    return sorted(new_list)

search_pascal_multiples_fast(250)

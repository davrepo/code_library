from collections import Counter
from functools import lru_cache
import concurrent.futures

@lru_cache(maxsize=None)
def comb_recurs(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return comb_recurs(n-1, k-1) + comb_recurs(n-1, k)

@lru_cache(maxsize=None)
def search_pascal_multiples_fast(row_limit):
    myList = []
    for n in range(10, row_limit):
        for k in range(2, n//2+1):
            myList.append(comb_recurs(n,k))
    
    dupes = [i for i, count in Counter(myList).items() if count > 1]
    sorted_dupes = sorted(dupes)
    return sorted_dupes

# @lru_cache(maxsize=None)
# def search_pascal_multiples_fast(row_limit):
#     seen = set()
#     return sorted(set(x for x in (comb_recurs(n, k) for n in range(10, row_limit) for k in range(2, n//2+1)) if x in seen or seen.add(x)))

def threaded(row_limit):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(search_pascal_multiples_fast, row_limit)
        print(f1.result())
        

from timeit import default_timer as timer

def main():
	row_limit = 250

	start = timer()
	print(search_pascal_multiples_fast(row_limit))
	end = timer()
	runtime_slow = end-start

	start = timer()
	print(threaded(row_limit))
	end = timer()
	runtime_fast = end-start

	print(round(runtime_slow / runtime_fast, 2))

if __name__ == "__main__":
	main()
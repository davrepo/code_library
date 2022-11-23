from collections import Counter
from functools import lru_cache
import concurrent.futures
from itertools import chain


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



@lru_cache(maxsize=None)
def subthread(n):
    for k in range(2, n//2+1):
        yield comb_recurs(n,k)

@lru_cache(maxsize=None)
def threaded(row_limit):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(subthread, range(10, row_limit))
        chained_result = chain.from_iterable(results)
        dupes = [i for i, count in Counter(chained_result).items() if count > 1]
        sorted_dupes = sorted(dupes)
        return sorted_dupes



# @lru_cache(maxsize=None)
# def subthread(n):
#     return [comb_recurs(n,k) for k in range(2, n//2+1)]

# @lru_cache(maxsize=None)
# def threaded(row_limit):
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = executor.map(subthread, range(10, row_limit))
#         chained_result = chain.from_iterable(results)
#         dupes = [i for i, count in Counter(chained_result).items() if count > 1]
#         sorted_dupes = sorted(dupes)
#         return sorted_dupes



from timeit import default_timer as timer

def main():
	row_limit = 250

	start = timer()
	print(search_pascal_multiples_fast(row_limit))
	end = timer()
	runtime_slow = end-start
    
	start1 = timer()
	print(threaded(row_limit))
	end1 = timer()
	runtime_fast = end1-start1

	print(f'Nonthread / thread >1 is better: {runtime_slow / runtime_fast}')

if __name__ == "__main__":
	main()
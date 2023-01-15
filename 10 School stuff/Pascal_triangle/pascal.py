
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

# ------------------------------ Standard version ------------------------------
@lru_cache(maxsize=None)
def search_pascal_multiples_fast(row_limit):
    return sorted(i for i, count in Counter(comb_recurs(n, k) for n in range(10, row_limit) for k in range(2, n//2+1)).items() if count > 1)


# ------------------------------ no Counter() overhead ------------------------------
# @lru_cache(maxsize=None)
# def search_pascal_multiples_fast(row_limit):
#     seen = set()
#     return sorted(set(x for x in (comb_recurs(n, k) for n in range(10, row_limit) for k in range(2, n//2+1)) if x in seen or seen.add(x)))


# ------------------------------ Multithreading, faster if row > 300 ------------------------------
# @lru_cache(maxsize=None)
# def subthread(n):
#     for k in range(2, n//2+1):
#         yield comb_recurs(n,k)

# @lru_cache(maxsize=None)
# def search_pascal_multiples_fast(row_limit):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         results = executor.map(subthread, range(10, row_limit))
#         chained_result = chain.from_iterable(results)
#         dupes = [i for i, count in Counter(chained_result).items() if count > 1]
#         sorted_dupes = sorted(dupes)
#         return sorted_dupes

# ------------------------------ Multiprocessing, actually much slower ------------------------------
# @lru_cache(maxsize=None)
# def subthread(n):
#     return [comb_recurs(n,k) for k in range(2, n//2+1)]

# @lru_cache(maxsize=None)
# def search_pascal_multiples_fast(row_limit):
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = executor.map(subthread, range(10, row_limit))
#         chained_result = chain.from_iterable(results)
#         dupes = [i for i, count in Counter(chained_result).items() if count > 1]
#         sorted_dupes = sorted(dupes)
#         return sorted_dupes


#----------- DO NOT CHANGE ANYTHING BELOW THIS LINE


def search_pascal_multiples_slow(row_limit):

    # Building up Pascal's triangle with a dict of lists
    ptriangle = {}
    ptriangle[0] = [1]
    ptriangle[1] = [1,1]
    ptriangle[2] = [1,2,1]
    for r in range(3, row_limit):
        ptriangle[r] = []
        for i in range(len(ptriangle[r-1])+1):
            if i == 0: # on left border, so we just add 1
                ptriangle[r].append(1)
            elif i == len(ptriangle[r-1]): # on right border, so we just add 1
                ptriangle[r].append(1)
            else: # not on border, so we sum up the two numbers above
                ptriangle[r].append(ptriangle[r-1][i-1] + ptriangle[r-1][i])

    # Putting all numbers into one list, except the outermost 2 numbers in each row
    number_list = []
    for r in range(row_limit):
        row = ptriangle[r]
        for i, number in enumerate(row):
            if i > 1 and i < len(row)-1: # exclude the outermost 2 numbers in each row
                number_list.append(number)

    # Counting the numbers
    number_set = set(number_list) 
    pascal_multiples = []
    for unique_number in number_set:
        count = 0
        for number in number_list:
            if number == unique_number:
                count = count + 1
        if count > 3:
            pascal_multiples.append(unique_number)
    
    return sorted(pascal_multiples)


from timeit import default_timer as timer

def main():
	row_limit = 250

	start = timer()
	print(search_pascal_multiples_slow(row_limit))
	end = timer()
	runtime_slow = end-start

	start = timer()
	print(search_pascal_multiples_fast(row_limit))
	end = timer()
	runtime_fast = end-start

	print(round(runtime_slow / runtime_fast, 2))

if __name__ == "__main__":
	main()
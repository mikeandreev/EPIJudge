import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# DONE : no recursion
# DONE : with recursion

def search_entry_equal_to_its_index(A):
    lo, hi = 0, len(A)-1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] == mid: return mid
        else:
            if lo == hi: return -1
            elif A[mid] < mid: lo = mid+1
            else: hi = mid-1
    return -1

def search_entry_equal_to_its_index_rec(A):
    def hlp(lo, hi):
        if lo > hi: return -1
        elif lo == hi:
            if A[lo] == lo: return lo
            else: return -1
        elif A[lo] <= lo and A[hi] >= hi:
            mid = lo + (hi - lo) // 2
            lo_res = hlp(lo, mid)
            if lo_res != -1: return lo_res
            return hlp(mid+1, hi)
        else: return -1
    return hlp(0, len(A)-1)


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(
        functools.partial(search_entry_equal_to_its_index, A))
    if result != -1:
        if A[result] != result:
            raise TestFailure("Entry does not equal to its index")
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure("There are entries which equal to its index")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_entry_equal_to_index.py",
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))

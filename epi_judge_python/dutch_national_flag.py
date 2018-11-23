import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

#
# [DONE]
# variant to try : sorting when key in 4 valued enum
#

def dutch_flag_partition(pivot_index, A):
    if len(A) <= 1:
        return
    pivot = A[pivot_index]
    after_ltp = 0 # first index after less_then_pivot part
    last_unp = len(A)-1  # last index of unprcessed part
    cur = after_ltp
    
    while cur <= last_unp:
    	if A[cur] < pivot:
    		if after_ltp < cur:
    			A[after_ltp], A[cur] = A[cur], A[after_ltp]
    		after_ltp += 1
    		cur += 1
    	elif A[cur] > pivot:
    		A[last_unp], A[cur] = A[cur], A[last_unp]
    		last_unp -= 1
    	else: # A[cur] == pivot
    	    cur += 1
    
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))

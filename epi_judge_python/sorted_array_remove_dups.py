import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Done

def delete_duplicates(A):
    if not A: return 0
    n = 1
    for i in range(1, len(A)):
        if A[n-1] != A[i] : 
            A[n] = A[i]
            n += 1
    return n

def delete_duplicates2(A):
    if not A: return 0
    n = 1
    for i in range(1, len(A)):
        if n < i : A[n] = A[i]
        if A[n-1] != A[n] : n += 1
    return n

# Returns the number of valid entries after deletion.
def delete_duplicates1(A):
    end = 0
    for i in range( 1, len(A)):
        if A[i-1] != A[i]:
            if end +1 < i : A[end+1] = A[i]
            end += 1
        elif (end + 1 == i) & (A[end] != A[end+1]):
            end +=1
        
    return end+1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))

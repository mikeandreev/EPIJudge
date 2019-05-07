from test_framework import generic_test

import bisect

# DONE: with lib
# DONE: from scratch

def search_first_of_k(A, k):
    L, U, res = 0, len(A)-1, -1
    while L <= U:
        M = L + (U - L) // 2
        if A[M] < k:
            L = M + 1
        elif k < A[M]:
            U = M - 1
        else: # A[M] == k
            res = M
            U = M - 1
    return res

def search_first_of_k_with_lib(A, k):
    i = bisect.bisect_left(A, k)
    if 0 <= i < len(A) and A[i] == k:
        return i
    else:
        return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))

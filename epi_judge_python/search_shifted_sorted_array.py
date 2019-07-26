from test_framework import generic_test

# DONE

def search_smallest(A):
    if not A:
        raise ValueError("list is empty")
    if len(A) == 1:
        return 0
    lo, hi = 0, len(A)-1
    if A[lo] < A[hi]:
        return lo 
    while hi-lo > 1:
        med = lo + (hi-lo)//2
        if A[med] < A[hi]:
            hi = med
        else:
            lo = med
    return hi


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))

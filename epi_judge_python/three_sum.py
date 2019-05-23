from test_framework import generic_test

import bisect

# DONE

def has_three_sum(A, t):
    A.sort()
    def has_two_sum(lo, c):
        hi = len(A)-1
        while lo <= hi:
            x = A[lo] + A[hi]
            if x == c: return True
            elif x < c: lo += 1
            else: hi -= 1
        return False
        
    #for i, a in enumerate(A):
    #    if has_two_sum(i, t-a): return True
    #return False
    return any(has_two_sum(i, t-a) for i, a in enumerate(A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))

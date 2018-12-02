from test_framework import generic_test

# Done

def apply_permutation(perm, A):
    n = len(A)    
    for i in range( n ):
        # find and apply cycle
        # we are using A[i] as temporary storage
        k = i
        while perm[k] >= 0:
            A[perm[k]], A[i] = A[i], A[perm[k]]
            perm[k], tmp = perm[k]-n, perm[k]
            k = tmp
    return

def apply_permutation1(perm, A):
    B = list(A)
    for i, p in enumerate( perm ):
        B[p] = A[i]
    for i in range(len(A)):
        A[i] = B[i]
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))

import unittest

class TestStringMethods(unittest.TestCase):
        
    def test1(self):
        self.assertEqual( apply_permutation_wrapper([2, 0, 1, 3], ['a', 'b', 'c', 'd']), ['b', 'c', 'a', 'd'] )

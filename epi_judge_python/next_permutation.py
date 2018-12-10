from test_framework import generic_test

# DONE

def next_permutation(perm):
    i = len(perm)-1
    # there are some wierd test cases with perm[i] = perm[j] for i != j
    while (i>0) & (perm[i-1] >= perm[i]):
        i -= 1
    if i == 0: return []
    # j :  perm[j] = min(  p in perm[i:] s.a. p > perm[i]   )
    _, min_indx = min( [ (p, -j) for j, p in enumerate(perm[i:], start=i) if p > perm[i-1] ] ) # the '-j' because of the wierd test cases
    min_indx = -min_indx
    #
    #print(perm)
    #print("{} perm[{}] = {}".format(i, min_indx, perm[min_indx]))
    #
    perm[i-1], perm[min_indx] = perm[min_indx], perm[i-1]
    # sort perm[i:]
    perm[i:] = reversed( perm[i:])
    return perm

def next_permutation1(perm):
    i = len(perm)-1
    # there are some wierd test cases with perm[i] = perm[j] for i != j
    while (i>0) & (perm[i-1] >= perm[i]):
        i -= 1
    if i == 0: return []
    # j :  perm[j] = min(  p in perm[i:] s.a. p > perm[i]   )
    #_, min_indx = min( [ (p, j) for j, p in enumerate(perm[i:], start=i) if p > perm[i-1] ] ) # doesn't work because of the wierd test cases
    min_val = float('inf')
    min_indx = i-1
    for k in range(i, len(perm)):
        if perm[k] > perm[i-1]:
            if perm[k] <= min_val:
                min_indx, min_val = k, perm[k]
    #
    #print(perm)
    #print("{} perm[{}] = {}".format(i, min_indx, perm[min_indx]))
    #
    perm[i-1], perm[min_indx] = perm[min_indx], perm[i-1]
    # sort perm[i:]
    perm[i:] = reversed( perm[i:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))


import unittest

class TestStringMethods(unittest.TestCase):
        
    def test1(self):
        self.assertEqual( next_permutation([6, 2, 3, 5, 4, 1, 0]), [6, 2, 4, 0, 1, 3, 5] )
from test_framework import generic_test

# DONE

def matrix_in_spiral_order(square_matrix):
    inc_q, inc_i = [ (0,1),(1,0), (0,-1), (-1,0)], 0
    n = len(square_matrix)
    arr = [0]*(n*n)
    
    indx = (0, 0)
    for i in range(n*n):
        arr[i] = square_matrix[ indx[0] ][ indx[1] ]
        square_matrix[ indx[0] ][ indx[1] ] = 0
        
        next = (indx[0]+inc_q[inc_i][0], indx[1]+inc_q[inc_i][1])
        if  (next[0] < 0) or (next[0] >= n) or (next[1] < 0) or (next[1] >= n) or square_matrix[ next[0] ][ next[1] ] == 0:
            inc_i = (inc_i+1) %len(inc_q)
            next = (indx[0]+inc_q[inc_i][0], indx[1]+inc_q[inc_i][1])
        indx = next
    return arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))


import unittest

class TestSolution(unittest.TestCase):
        
    def test1(self):
        self.assertEqual( matrix_in_spiral_order( [ [4,3], [2,1]] ), [4,3,2,1] )
from test_framework import generic_test

# DONE

def rotate_matrix(A):
    n = len(A)
    for k in range(n // 2):
        for i in range(n-1-k*2):
            #A[k][k+i], A[k+i][n-1-k], A[n-1-k][n-1-i-k], A[n-1-i-k][k] = A[n-1-i-k][k], A[k][k+i], A[k+i][n-1-k], A[n-1-k][n-1-i-k]
            A[k][k+i], A[k+i][~k], A[~k][~(i+k)], A[~(i+k)][k] = A[~(i+k)][k], A[k][k+i], A[k+i][~k], A[~k][~(i+k)]
        #
    return A


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))

import unittest

class TestSolution(unittest.TestCase):
        
    def test1(self):
        self.assertEqual( rotate_matrix( [ [ 1,  2,  3,  4],
                                           [ 5,  6,  7,  8],
                                           [ 9, 10, 11, 12],
                                           [13, 14, 15, 16] ] ),
                                         #
                                         [ [13,  9, 5, 1],
                                           [14, 10, 6, 2],
                                           [15, 11, 7, 3],
                                           [16, 12, 8, 4] ] )
    def test2(self):
        self.assertEqual( rotate_matrix( [[1, 2, 3, 4, 5, 6],
                                          [7, 8, 9, 10, 11, 12],
                                          [13, 14, 15, 16, 17, 18],
                                          [19, 20, 21, 22, 23, 24],
                                          [25, 26, 27, 28, 29, 30],
                                          [31, 32, 33, 34, 35, 36]]),
                                         #
                                         [[31, 25, 19, 13, 7, 1],
                                          [32, 26, 20, 14, 8, 2],
                                          [33, 27, 21, 15, 9, 3],
                                          [34, 28, 22, 16, 10, 4],
                                          [35, 29, 23, 17, 11, 5],
                                          [36, 30, 24, 18, 12, 6]] )

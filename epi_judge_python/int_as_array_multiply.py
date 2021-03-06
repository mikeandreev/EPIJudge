from test_framework import generic_test
import copy

# DONE

def multiply(num1, num2):
    return multiply2(num1, num2)
    
def multiply2(A, B):
    neg = (A[0] < 0) ^ (B[0] < 0)
    A[0], B[0] = abs(A[0]), abs(B[0])
    res = [0]*(len(A)+len(B))
    for i in reversed( range( len(A)) ):
        for j in reversed( range( len(B)) ):
            k = i + j + 1
            res[k] += A[i] *B[j]
            res[k-1] += res[k] // 10
            res[k] %= 10
    # python trick:
    res = res[ next( ( i for i, x in enumerate(res) if x != 0 ), len(res)  ) : ] or [0]
    
    if neg:
        res[0] *= -1
    return res

#####
# >>>
def plus( A, B):
    carry = 0
    res = [0] * max(len(A), len(B))
    a_shift = len(res) - len(A)
    b_shift = len(res) - len(B)
    for i in reversed( range( len(res) ) ):
        if i-a_shift >= 0: res[i] += A[i-a_shift]
        if i-b_shift >= 0: res[i] += B[i-b_shift]
        res[i] += carry
        carry = res[i] // 10
        res[i] = res[i] % 10
    if carry > 0:
        return [carry] + res
    return res

def mult( A, m ):
    curry = 0
    for i in reversed( range( len(A) ) ):
        A[i] = A[i]*m + curry
        curry = A[i] // 10
        A[i] = A[i] % 10
    if curry > 0:
        return [curry] + A
    return A

def multiply1(num1, num2):
    if num1 == [0] or num2 == [0]:
        return [0]
    res = []
    neg = (num1[0] < 0) ^ (num2[0] < 0)
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    for i in range( len(num2) ):
        tmp = mult( copy.deepcopy(num1), num2[i] ) + [0]*(len(num2)-1-i)
        res = plus( res, tmp)
    if neg:
        res[0] = -res[0]
    return res
#<<<<
####

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))

import unittest

class TestStringMethods(unittest.TestCase):
    
    def hlp_multiply(self, f):
        self.assertEqual( f([1, 9, 3, 7, 0, 7, 7, 2, 1], [1]),       [1, 9, 3, 7, 0, 7, 7, 2, 1] )
        self.assertEqual( f([1, 9, 3, 7, 0, 7, 7, 2, 1], [1, 0]), [1, 9, 3, 7, 0, 7, 7, 2, 1, 0] )
        self.assertEqual( f([1, 9, 3, 7, 0, 7, 7, 2, 1], [2, 0]), [3, 8, 7, 4, 1, 5, 4, 4, 2, 0] )
        self.assertEqual( f([1, 9, 3, 7, 0, 7, 7, 2, 1], [1, 1]), [2, 1, 3, 0, 7, 8, 4, 9, 3, 1] )
        self.assertEqual( f([1, 9, 3, 7, 0, 7, 7, 2, 1], [2, 1]), [4, 0, 6, 7, 8, 6, 2, 1, 4, 1] )
        self.assertEqual( f([1, 9, 3, 7, 0, 7, 7, 2, 1], [-2, 1]), [-4, 0, 6, 7, 8, 6, 2, 1, 4, 1] )
        self.assertEqual( f([-1, 9, 3, 7, 0, 7, 7, 2, 1], [-2, 1]), [4, 0, 6, 7, 8, 6, 2, 1, 4, 1] )
        self.assertEqual( f([-1, 9, 3, 7, 0, 7, 7, 2, 1], [2, 1]), [-4, 0, 6, 7, 8, 6, 2, 1, 4, 1] )
        self.assertEqual( f([2, 6, 7], [0]), [0])
    
    def test_multiply1(self):
        self.hlp_multiply( multiply1 )
        

    def test_multiply2(self):
        self.hlp_multiply( multiply2 )
        
        
    def test_mult0(self):
        self.assertEqual(mult([1, 1, 1], 5), [5, 5, 5])
        self.assertEqual(mult([1, 2, 9], 5), [6, 4, 5])
        self.assertEqual(mult([2, 2, 2], 5), [1, 1, 1, 0])

    def test_plus0(self):
        self.assertEqual(plus([], [2, 5]), [2, 5])
        self.assertEqual(plus([1, 2, 9], [2, 8]), [1, 5, 7])
        self.assertEqual(plus([2, 3], [8, 9]), [1, 1, 2])
        self.assertEqual(plus([1, 9, 3, 7, 0, 7, 7, 2, 1, 0], [1, 9, 3, 7, 0, 7, 7, 2, 1]), [2, 1, 3, 0, 7, 8, 4, 9, 3, 1])
        self.assertEqual(plus([3, 8, 7, 4, 1, 5, 4, 4, 2, 0], [1, 9, 3, 7, 0, 7, 7, 2, 1]), [4, 0, 6, 7, 8, 6, 2, 1, 4, 1])


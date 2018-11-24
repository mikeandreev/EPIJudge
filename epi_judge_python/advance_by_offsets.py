from test_framework import generic_test

# DONE

def can_reach_end(A):
    max_reachable = 0
    for i in range(len(A)):
        if i > max_reachable: return False
        if i+A[i] >= len(A): return True
        if i+A[i] > max_reachable: max_reachable = i+A[i]

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
            
            
import unittest

class TestStringMethods(unittest.TestCase):
        
    def test1(self):
        self.assertEqual( can_reach_end([3, 3, 1, 0, 3, 1, 0, 2, 0, 1]), True)

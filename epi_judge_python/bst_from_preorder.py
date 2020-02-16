from test_framework import generic_test
import math

# DONE

class Node: 
    def __init__(self , data=None, left=None, right=None): 
        self.data, self.left, self.right = data, left, right

def rebuild_bst_from_preorder(preorder_sequence):
    i, A = 0, preorder_sequence
    def tree(is_left, limit):
        nonlocal i, A
        if i >=  len(A) or A[i] > limit or (is_left and A[i] > A[i-1]):
            return None
        val = A[i]
        i += 1
        return Node(val, tree(True, val), tree(False, limit))
        
    t = tree(False, math.inf)
    return t


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))

import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# problem 14.8
#
# DONE
#

class BSTNode: 
    def __init__(self , data=None, left=None, right=None): 
        self.data, self.left, self.right = data, left, right

def build_min_height_bst_from_sorted_array(A):
    def hlp(start, end):
        if start >= end:
            return None
        i = (end+start) // 2
        return BSTNode(A[i], hlp(start, i), hlp(i+1, end))
    return hlp(0, len(A))
            


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py", 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))

import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# DONE

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

def find_kth_node_binary_tree_norec(tree, k):
    if not tree or k <= 0: return None
    left_size = tree.left.size if tree.left else 0

    while left_size != k-1:
        if left_size >= k:
            tree = tree.left
        else:
            tree, k = tree.right, k - left_size - 1
        left_size = tree.left.size if tree.left else 0
    return tree

def find_kth_node_binary_tree_rec(tree, k):
    if not tree or k <= 0: return None
    left_size = tree.left.size if tree.left else 0

    if left_size >= k:
        return find_kth_node_binary_tree_rec(tree.left, k)
    elif left_size == k - 1:
        return tree
    return find_kth_node_binary_tree_rec(tree.right, k - left_size - 1)

find_kth_node_binary_tree = find_kth_node_binary_tree_norec

@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(
        functools.partial(find_kth_node_binary_tree, tree, k))

    if not result:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_node_in_tree.py",
                                       "kth_node_in_tree.tsv",
                                       find_kth_node_binary_tree_wrapper))

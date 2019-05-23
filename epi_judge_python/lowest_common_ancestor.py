import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple

# DONE

def lca(tree, node0, node1):
    def find1(node):
        if not node: return False
        if node is node0 or node is node1: return True
        return find1(node.left) or find1(node.right)
        
    def find0(node):
        if not node: return False, None
        if node is node0 or node is node1:
            if node0 is node1 or find1(node.left) or find1(node.right):
                return True, node
            return True, None
            
        lres = find0(node.left)
        if lres[1] is not None: return lres
        rres = find0(node.right)
        if rres[1] is not None: return rres
        if lres[0] and rres[0]: return True, node
        return lres[0] or rres[0], None
        
    return find0(tree)[1]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))

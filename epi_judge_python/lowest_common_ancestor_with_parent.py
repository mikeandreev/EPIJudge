import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# DONE : with additional memory
# DONE : no additional memory

def lca(node0, node1):
    def get_depth(node):
        depth = 0
        while node.parent:
            node, depth = node.parent, depth+1
        return depth
        
    depth0, depth1 = get_depth(node0), get_depth(node1)
    if depth0 > depth1:
        node0, node1 = node1, node0
        depth0, depth1 = depth1, depth0
        
    depth_diff = depth1-depth0
    while depth_diff:
        node1 = node1.parent
        depth_diff -= 1
        
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
        
    return node0

def lca1(node0, node1):
    cache = {id(node0), id(node1)}
    while True:
        if node0 is node1:
            return node1
        if (node0.parent is None) and (node1.parent is None): return None
        if node0.parent:
            node0 = node0.parent
            if id(node0) in cache: return node0
            cache.add(id(node0))
        if node1.parent:
            node1 = node1.parent
            if id(node1) in cache: return node1
            cache.add(id(node1))
    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))

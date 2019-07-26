import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# DONE

def lca(node0, node1):
    cache = set()
    node = [node0, node1]
    while node[0] or node[1]:
        for i in [0, 1]:
            if node[i]:
                if id(node[i]) in cache: 
                    return node[i]
                cache.add( id(node[i]) )
                node[i] = node[i].parent
    raise ValueError("Nodes have no common ancestor")


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
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))

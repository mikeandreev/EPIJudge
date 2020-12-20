import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook

# DONE
# rec +
# norec +
#
###
def find_successor_norec(node):
    if node is not None:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        else:
            while node.parent and node.parent.left is not node:
                node = node.parent
            if node.parent is None:
                return None
            node = node.parent
    return node

###
def find_left_turn_at_top(node):
    if node.parent is None: return None
    if node.parent.left is node: return node.parent
    return find_left_turn_at_top(node.parent)

def find_leftest_at_bottom(node):
    if node.left is None: return node
    return find_leftest_at_bottom(node.left)

def find_successor_rec(node):
    if node is None: return None
    if node.right:
        return find_leftest_at_bottom(node.right)
    else:
        return find_left_turn_at_top(node)
    return None
###

def find_successor(node):
    return find_successor_norec(node)

@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("successor_in_tree.py",
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))

from test_framework import generic_test

# DONE

def preorder_traversal(tree):
    res, stack = [], []
    while tree or stack:
        if tree:
            res.append(tree.data)
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            tree = tree.right
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))

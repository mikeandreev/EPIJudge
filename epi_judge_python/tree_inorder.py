from test_framework import generic_test

# DONE

def inorder_traversal(tree):
    res = []
    stack = []
    while tree or stack:
        if not tree:
            tree = stack.pop()
            res.append(tree.data)
            tree = tree.right
        else:
            stack.append(tree)
            tree = tree.left
    return res
    
def inorder_traversal_rec(tree):
    res = []
    def hlp(tree):
        if not tree: return
        hlp(tree.left)
        res.append(tree.data)
        hlp(tree.right)
    hlp(tree)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))

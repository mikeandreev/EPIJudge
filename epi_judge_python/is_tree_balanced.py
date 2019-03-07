from test_framework import generic_test

# DONE

def is_balanced_binary_tree(tree):
    if not tree: return True
    def tree_depth_chk(root):
        if not root: return True, 0
        lchk, ldepth = tree_depth_chk(root.left)
        rchk, rdepth = tree_depth_chk(root.right)
        return (lchk & rchk & (abs(ldepth-rdepth)<=1)), 1+max(ldepth, rdepth)
        
    chk, _ = tree_depth_chk(tree)
    return chk


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

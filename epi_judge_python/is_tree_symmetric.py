from test_framework import generic_test

# DONE

def is_symmetric(tree):
    
    def is_mirrors(r1, r2):
        if not r1 and not r2: return True
        if not r1 or not r2: return False
        return (r1.data == r2.data
                     and is_mirrors(r1.left, r2.right)
                     and is_mirrors(r1.right, r2.left))
        
    return not tree or is_mirrors(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))

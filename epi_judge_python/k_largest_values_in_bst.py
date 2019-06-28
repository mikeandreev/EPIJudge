from test_framework import generic_test, test_utils

# DONE

def find_k_largest_in_bst_rec(tree, k):
    if not tree or k == 0: return []
    found = find_k_largest_in_bst(tree.right, k)
    if len(found) == k: return found
    found.append( tree.data )
    return found + find_k_largest_in_bst(tree.left, k - len(found))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))

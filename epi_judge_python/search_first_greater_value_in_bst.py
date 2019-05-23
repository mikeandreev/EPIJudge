from test_framework import generic_test

# DONE

def find_first_greater_than_k(tree, k):
    if tree is None: return None
    left_res = find_first_greater_than_k(tree.left, k)
    if left_res is not None: return left_res
    if tree.data > k: return tree
    return find_first_greater_than_k(tree.right, k)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))

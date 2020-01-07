from test_framework import generic_test

# DONE

def matrix_search(A, x):
    n, m = len(A), len(A[0]) # n x m matrix
    j, i = 0, m-1
    while j < n and i >= 0:
        if A[j][i] == x:
            return True
        elif A[j][i] < x:
            j += 1
        else:
            i -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))

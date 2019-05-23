from test_framework import generic_test

# DONE

def merge_two_sorted_arrays(A, m, B, n):
    i, a, b = n + m - 1, m-1, n-1
    while b >= 0:
        if a >= 0 and A[a] >= B[b]:
            if i != a: A[i] = A[a]
            a -= 1
        else: A[i] = B[b]; b -= 1
        i -= 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))

from test_framework import generic_test

# DONE

def intersect_two_sorted_arrays(A, B):
    res = []
    a, b = 0, 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            a += 1
        elif A[a] > B[b]:
            b += 1
        else:
            if not res or res[-1] != A[a]:
                res.append(A[a])
            a += 1; b+=1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))

from test_framework import generic_test, test_utils

# DONE

def permutations(A):
    res = []
    n = len(A)
    def hlp(L, l):
        if l == 0:
            res.append(L.copy())
            return
        for i in reversed(range(l)):
            if l == n:
                L = L.copy()
            L[i], L[l-1] = L[l-1], L[i]
            hlp(L, l-1)
            #L[i], L[l-1] = L[l-1], L[i]

    hlp(A, n)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))

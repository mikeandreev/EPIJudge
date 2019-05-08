from test_framework import generic_test

# DONE

def number_of_ways(n, m):
    l, k = n + m - 2, n - 1 # need to calculate (l choose k)
    if k == 0 or l == k: return 1
    C = [[0]*(k+1) for _ in range(l+1)] # DP cache, we are using indexes [ from 1 to l ][ 1 to k ]
    for i in range(1, l+1):
        for j in range(max(1, i-l+k), min(k+1, i+1) ):
            if j == i: C[i][j] = 1
            elif j == 1: C[i][j] = i
            else: C[i][j] = C[i-1][j] + C[i-1][j-1]
    return C[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))

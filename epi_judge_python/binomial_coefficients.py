from test_framework import generic_test

# DONE : rec with cache
# DONE : bottom-up

def compute_binomial_coefficient(n, k):
    C = [ [0]*min(k+1, i+1) for i in range(n+1)] 
    def hlp(n, k):
        if C[n][k] == 0:
            if k == 0 or n == k: C[n][k] = 1
            elif k == 1: C[n][k] = n
            else: C[n][k] = hlp(n-1, k) + hlp(n-1, k-1)
        return C[n][k]
    return hlp(n, k)

def compute_binomial_coefficient_1(n, k):
    C = [ [0]*min(k+1, i+1) for i in range(n+1)] 
    for i in range(n+1):
        for j in range(min(k+1, i+1)):
            if j == 0 or j == i: C[i][j] = 1; continue
            if j == 1: C[i][j] = i; continue
            C[i][j] = C[i-1][j] + C[i-1][j-1]
    return C[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))

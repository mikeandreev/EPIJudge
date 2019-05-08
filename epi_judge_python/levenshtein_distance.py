from test_framework import generic_test

# DONE

def levenshtein_distance(A, B):
    a, b = len(A)+1, len(B)+1
    C = [[0]*a for _ in range(b)] # DP cache
    for i in range(b):
        for j in range(a):
            if i == 0: C[i][j] = j
            elif j == 0: C[i][j] = i
            else:
                if A[j-1] == B[i-1]: C[i][j] = C[i-1][j-1]
                else: C[i][j] = 1 + min(C[i-1][j-1], C[i-1][j], C[i][j-1] )
    return C[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))

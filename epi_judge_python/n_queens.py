from test_framework import generic_test

# DONE

def n_queens(n):
    res, state = [], [0] * n
    def check(row):
        if row == n:
            res.append(list(state))
            return
        for k in range(n):
            ok = all(
                j != k and i-j != row-k and i+j != row+k
                for i, j in enumerate(state[:row])
            )
            if ok:
                state[row] = k
                check(row+1)
    check(0)
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))

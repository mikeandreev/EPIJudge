from test_framework import generic_test
import math

# DONE

def square_root(x):
    if x < 0: return math.nan
    left, right = (1, x) if x >= 1 else (x, 1)
    while not math.isclose(left, right):
        mid = (left + right)*0.5
        if mid*mid > x:
            right = mid
        else:
            left = mid
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))

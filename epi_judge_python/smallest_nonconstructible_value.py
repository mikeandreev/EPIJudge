from test_framework import generic_test

# DONE

def smallest_nonconstructible_value(A):
    max_constructible = 0
    A.sort()
    for a in A:
        if a > max_constructible+1:
            break
        max_constructible += a
    return max_constructible + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
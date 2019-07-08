from test_framework import generic_test

#WIP

def smallest_nonconstructible_value(A):
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
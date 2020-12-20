import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

# problem: 11.7
#
# DONE
#

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    min_ = A[0]
    max_ = A[0]
    for a in A:
        if a > max_: max_ = a
        elif a < min_: min_ = a
    return MinMax(min_, max_)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))

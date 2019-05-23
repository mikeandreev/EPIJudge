import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

# DONE

def find_minimum_visits(intervals):
    intervals.sort(key=lambda interval: interval.right)
    res, curr = 0, float('-inf')
    for interval in intervals:
        if curr < interval.left:
            curr = interval.right
            res += 1
    return res


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))

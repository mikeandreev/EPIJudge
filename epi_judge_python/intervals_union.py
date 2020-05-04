import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# DONE

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    if not intervals:
        return []

    intervals.sort( key=lambda interval: (interval.left.val, not interval.left.is_closed) )
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        to_join = intervals[i]
        last = result[-1]
        if (last.right.val, last.right.is_closed) < (to_join.right.val, to_join.right.is_closed):
            if last.right.val < to_join.left.val or \
                 (last.right.val == to_join.left.val and not last.right.is_closed and not to_join.left.is_closed):
                result.append(to_join)
            else:
                result[-1] = Interval( last.left, to_join.right)

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))

import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

# DONE

def optimum_subject_to_capacity(items, capacity):
    #cache = [ {} for _ in items]
    cache = [ [-1] * (capacity + 1) for _ in items ]
    def solve(j, maxW):
        if maxW <= 0 or j < 0: return 0

        w, v = items[j].weight, items[j].value
        if cache[j][maxW] >= 0:
            return cache[j][maxW]
        res = solve(j-1, maxW)
        if w <= maxW:
            res = max(res, solve(j-1, maxW-w) + v)
        cache[j][maxW] = res
        return res
    return solve(len(items)-1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))

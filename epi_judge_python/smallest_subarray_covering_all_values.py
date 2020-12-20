import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

#  DONE
import math

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(paragraph, keywords):
    key_to_indx = { k: i for i, k in enumerate(keywords) }
    last_indx = [-1] * len(keywords)
    interim_res = [math.inf] * len(keywords)
    res = None
    for i, w in enumerate(paragraph):
        if w not in key_to_indx:
            continue
        indx = key_to_indx[w]
        if indx == 0:
            interim_res[indx] = 0
        else:
            if interim_res[indx-1] < math.inf:
                interim_res[indx] = interim_res[indx-1] + i - last_indx[indx-1]
        if indx == len(keywords) - 1 and interim_res[indx] < math.inf and\
           (res is None or res.end - res.start > interim_res[indx]):
            res = Subarray(i - interim_res[indx], i)
        last_indx[indx] = i
    if res is None: return Subarray(-1, -1)
    return res


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))

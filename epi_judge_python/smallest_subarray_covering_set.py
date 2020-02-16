import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections
import math
# WIP

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def subarr_len(subarr):
    if subarr.end < 0:
        return math.inf
    else:
        return subarr.end - subarr.start

def find_smallest_subarray_covering_set_v1(paragraph, keywords):
    subarr = Subarray(-1, -1)
    count = collections.Counter(keywords) # init value is 1
    empty_counter_val = 1
    remains_to_cover = len(count)
    i, j = 0, 0 # means [i, j)
    while j < len(paragraph):
        word, j = paragraph[j], j+1
        if word not in count:
            continue
        if count[word] == empty_counter_val:
            remains_to_cover -= 1
        count[word] += 1

        while i < j and remains_to_cover == 0:
            cur = Subarray(i, j-1)
            if subarr_len(subarr) > subarr_len(cur):
                subarr = cur

            word, i = paragraph[i], i+1
            if word not in count:
                continue
            count[word] -= 1
            if count[word] == empty_counter_val:
                remains_to_cover += 1
    return subarr
    
def find_smallest_subarray_covering_set_v2(paragraph, keywords):
    from sortedcontainers import SortedSet
    key_len, sorted_set = len(keywords), SortedSet()
    res = Subarray(0, len(paragraph))
    key_dict = {k: -1 for k in keywords }
    for i, w in enumerate(paragraph):
        if w not in key_dict: continue
        
        if key_dict[w] != -1: sorted_set.remove(key_dict[w])
        
        key_dict[w] = i
        sorted_set.add(i)
        if len(sorted_set) == key_len:
            min_indx, max_indx = sorted_set[0], i
            if res.end - res.start > max_indx - min_indx:
                res = Subarray(min_indx, max_indx)
                
    if len(sorted_set) < key_len: return Subarray(-1, -1)
    return res

def find_smallest_subarray_covering_set(paragraph, keywords):
    return find_smallest_subarray_covering_set_v1(paragraph, keywords)

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))

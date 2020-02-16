from test_framework import generic_test

# DONE

import collections
import math
from sortedcontainers import SortedList

Item = collections.namedtuple('Item', ('value', 'arr_i', 'indx'))

def find_closest_elements_in_sorted_arrays_tree(sorted_arrays):
    cache = SortedList([Item(sorted_arrays[arr_i][0], arr_i, 0) for arr_i in range(len(sorted_arrays))])
    res = math.inf
    while True:
        min_item = cache[0]
        res = min(res, cache[-1].value - min_item.value )
        if min_item.indx == len(sorted_arrays[min_item.arr_i]) - 1:
            break
        cache.remove(min_item)
        indx = min_item.indx+1
        cache.add(Item(sorted_arrays[min_item.arr_i][indx], min_item.arr_i, indx))
    return res


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    for arr in sorted_arrays:
        if len(arr) == 0: return -1
    return find_closest_elements_in_sorted_arrays_tree(sorted_arrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))

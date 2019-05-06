from test_framework import generic_test
import heapq

# DONE

def merge_sorted_arrays(sorted_arrays):
    h, res = [], []
    n = len(sorted_arrays)
    length = [len(sorted_arrays[i]) for i in range(n)]
    for i in range(n):
        indx = 0
        if indx < length[i]: heapq.heappush(h, (sorted_arrays[i][indx], i, indx+1))
    while h:
        val, i, next_indx = heapq.heappop(h)
        res.append(val)
        if next_indx < length[i]: heapq.heappush(h, (sorted_arrays[i][next_indx], i, next_indx+1))
        
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))

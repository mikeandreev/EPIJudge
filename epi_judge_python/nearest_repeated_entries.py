from test_framework import generic_test

import collections
# DONE

def find_nearest_repetition(paragraph):
    inf = float("inf")
    prev = collections.defaultdict(lambda: -inf)
    min_dist = inf
    for i, word in enumerate(paragraph):
        dist = i - prev[word]
        min_dist = min(min_dist, dist)
        prev[word] = i
    if min_dist == inf:
        return -1
    return min_dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))

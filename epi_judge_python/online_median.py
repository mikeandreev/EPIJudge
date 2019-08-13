from test_framework import generic_test

import heapq

# DONE

def online_median_2(sequence):
    low_heap = []
    high_heap = []
    res = []
    for x in sequence:
        heapq.heappush(high_heap, -heapq.heappushpop(low_heap, -x))

        # rebalance
        if len(high_heap) > len(low_heap) + 1:
            heapq.heappush(low_heap, -heapq.heappop(high_heap) )

        # median
        if len(low_heap) == len(high_heap):
            res.append( (-low_heap[0] + high_heap[0])/2 )
        else:
            res.append( high_heap[0] )
    return res

def online_median_1(sequence):
    low_heap = []
    high_heap = []
    res = []
    for x in sequence:
        if len(low_heap) == 0 or x <= -low_heap[0]:
            heapq.heappush(low_heap, -x)
        else:
            heapq.heappush(high_heap, x)
        # rebalance
        if len(low_heap) > len(high_heap) + 1:
            heapq.heappush(high_heap, -heapq.heappop(low_heap) )
        elif len(high_heap) > len(low_heap) + 1:
            heapq.heappush(low_heap, -heapq.heappop(high_heap) )
        # median
        if len(low_heap) == len(high_heap):
            res.append( (-low_heap[0] + high_heap[0])/2 )
        elif len(low_heap) > len(high_heap):
            res.append( -low_heap[0] )
        else:
            res.append( high_heap[0] )
    return res

online_median = online_median_2

def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))

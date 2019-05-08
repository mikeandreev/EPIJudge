from test_framework import generic_test
import heapq

# DONE

def sort_k_increasing_decreasing_array(A):
    INCR, DECR = range(2)
    order, begin = INCR, 0
    sub_arr = []
    for i in range(1, len(A)):
        if (order == INCR and A[i-1] > A[i]) or (order == DECR and A[i-1] < A[i]):
            sub_arr.append( iter(A[begin: i]) if order == INCR else reversed( A[begin: i] ) )
            begin = i
            order = 1 - order
    sub_arr.append( iter(A[begin: ]) if order == INCR else reversed( A[begin: ] ) )

    # ver 1:
    #return list( heapq.merge( *sub_arr ) )

    # ver 2:
    res, heap = [], []
    def add_next(i):
        n = next(sub_arr[i], None)
        if n is not None: heapq.heappush( heap, (n, i) )
    for i in range(len(sub_arr)):
        add_next(i)
    while heap:
        n, i = heapq.heappop( heap )
        res.append( n )
        add_next(i)
    return res




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))

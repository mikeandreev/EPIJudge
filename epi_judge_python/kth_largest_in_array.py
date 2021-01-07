from test_framework import generic_test

#
# problem 11.8
#
# heap ver: DONE
# qselect ver: DONE
#



# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    return find_kth_largest_qselect(k, A)

def find_kth_largest_qselect(k, A):
    from random import randint
    pos = k-1
    if pos >= len(A):
        return None

    def do_pivot(start, end):
        pivot_indx = randint(start, end)
        pivot = A[pivot_indx]
        A[pivot_indx], A[end] = A[end], A[pivot_indx]
        pivot_indx = start
        for i in range(start, end):
            if A[i] > pivot: # moving larger elememts to the left
                A[i], A[pivot_indx] = A[pivot_indx], A[i]
                pivot_indx += 1
        A[pivot_indx], A[end] = A[end], A[pivot_indx]
        return pivot_indx

    def partition(start, end):
        pivot_indx = do_pivot(start, end)
        if pivot_indx == pos:
            return
        elif pivot_indx > pos:
            partition(start, pivot_indx-1)
        else: # pivot_indx < pos
            partition(pivot_indx+1, end)

    partition(0, len(A)-1)
    return A[pos]

def find_kth_largest_heap(k, A):
    from heapq import heappush, heappop
    heap = []
    for el in A:
        heappush(heap, el)
        if len(heap) > k:
            rem = heappop(heap)
    return heappop(heap)
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))

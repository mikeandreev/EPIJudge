from test_framework import generic_test, test_utils
import collections
import heapq

# DONE

def k_largest_in_binary_heap_2(A, k):
    h, res = [], []
    if A: heapq.heappush(h, (-A[0], 0))
    for _ in range(k):
        if not h: break
        val, i = heapq.heappop(h)
        res.append(-val)
        def add(j):
            if j < len(A):
                heapq.heappush(h, (-A[j], j))
        add(i*2+1)
        add(i*2+2)
    return res

def k_largest_in_binary_heap_1(A, k):
    h = []
    q = collections.deque([0])
    while q:
        i = q.popleft()
        if i >= len(A):
            continue
        val = A[i]
        if len(h) < k:
            heapq.heappush(h, val)
            q.extend([i*2+1, i*2+2])
        elif val > h[0]:
            heapq.heappushpop(h, val)
            q.extend([i*2+1, i*2+2])
    return h

k_largest_in_binary_heap = k_largest_in_binary_heap_1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))

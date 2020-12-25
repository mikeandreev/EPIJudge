from test_framework import generic_test

# problem 12.8
#
# DONE

def longest_subarray_with_distinct_entries(A):
    res = 0
    begin , end = 0, 0
    content = set()
    while True:
        while end < len(A) and A[end] not in content:
            content.add(A[end])
            end += 1
            res = max(res, end-begin)
        if end == len(A): break
        while A[end] in content:
           content.remove(A[begin])
           begin += 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))

from test_framework import generic_test, test_utils

# problem: 15.5
#
# DONE

def combinations(n, k):
    if k == 0: return [[]]
    #if n < k: return []
    res = combinations(n-1, k-1)
    for c in res:
        c.append(n)
    if n-1 >= k:
        res += combinations(n-1, k)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))

from test_framework import generic_test

from sortedcontainers import SortedDict
import math
import collections

# DONE

ABSqrt2 = collections.namedtuple('ABSqrt2', ('value', 'a', 'b'))

def absqrt2(a, b):
    return ABSqrt2(a+b*math.sqrt(2), a, b)

## ver 2

def generate_first_k_a_b_sqrt2_v2(k):    
    if k < 1: return []
    sqrt2 = math.sqrt(2)
    res = [0.0]
    # need abcache because test compares floating point numbers and
    # 3*sqrt2 is not equal to sqrt2 + sqrt2 + sqrt2
    abcache = [absqrt2(0, 0)] 
    # invariant:
    #    res[i] + 1 > res[-1]
    #    res[j] + sqrt2 > res[-1] 
    i, j = 0, 0
    while len(res) < k:
        ab1 = absqrt2(abcache[i].a+1, abcache[i].b)
        ab2 = absqrt2(abcache[j].a, abcache[j].b+1)
        ab = min(ab1, ab2)
        res.append(ab.value); abcache.append(ab)
        if ab1.value <= res[-1]:
            i += 1
        if ab2.value <= res[-1]:
            j += 1
    return res

## ver 1


def generate_first_k_a_b_sqrt2_v1(k):
    cache = SortedDict({absqrt2(0, 0): None})
    
    res = []
    for i in range(k):
        item = cache.popitem(0)[0]
        res.append(item.value)
        cache[ absqrt2(item.a, item.b+1) ] = None
        cache[ absqrt2(item.a+1, item.b) ] = None
    
    return res

def generate_first_k_a_b_sqrt2(k):
    return generate_first_k_a_b_sqrt2_v2(k)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))

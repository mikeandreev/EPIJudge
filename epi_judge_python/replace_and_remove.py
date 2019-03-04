import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# DONE

def replace_and_remove(size, s):
    '''
    a -> d, d
    b : remove
    '''
    res_size, j = 0, 0
    for i in range(size):
        el = s[i]
        if el == 'b': continue
        s[j] = el
        j += 1;  res_size += 1
        if el == 'a': res_size += 1
    #
    j -= 1
    if res_size > size: s[size:res_size] = [0]*res_size # is it correct?
    i = res_size - 1
    while j >= 0:
        el = s[j]
        if el == 'a':
            s[i],s[i-1] = 'd', 'd'
            i -= 2
        else:
            s[i] = el
            i -= 1
        j -= 1
    
    return res_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
                                       
import unittest

class TestSolution(unittest.TestCase):
    def test1(self):
        s = ['s','f','b', 'u', 'y']
        size = len(s)
        self.assertEqual(  replace_and_remove(size, s), size-1)
        self.assertEqual( s[:size-1], ['s', 'f', 'u', 'y'])
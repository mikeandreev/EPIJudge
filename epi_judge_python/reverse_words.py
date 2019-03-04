import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# DONE

# Assume s is a string encoded as bytearray.
def reverse_words(s):
    s.reverse()
    i = -1
    while i < len(s):
        start = i+1
        i = s.find(b' ',start)
        if i < 0: i = len(s)
        s[start:i] = reversed(s[start:i])
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))

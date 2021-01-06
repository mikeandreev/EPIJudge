import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

#
# problem 16.7
#
# DONE
#

def decompose_into_dictionary_words3(domain, dictionary):
    INIT_VAL = -1
    NO_RES = -2
    cache = [INIT_VAL] * len(domain)
    def help(i):
        if i == len(domain): return 0
        if cache[i] != INIT_VAL: return cache[i]
        substr = domain[i:]
        for s in dictionary:
            if substr.startswith(s):
                res = help(i+len(s))
                if res > 0 or len(s) == len(substr):
                    cache[i] = len(s)
                    return len(s)
        cache[i] = NO_RES
        return NO_RES
    help(0)
    res = []
    if cache[0] > 0:
        i = 0
        while i < len(domain):
            res.append(domain[i:i+cache[i]])
            i += cache[i]
    return res


def decompose_into_dictionary_words2(domain, dictionary):
    cache = {'': []}
    def help(substr):
        if substr in cache:
            return cache[substr]
        for s in dictionary:
            if substr.endswith(s):
                res = help(substr[0:-len(s):])
                if res or len(s) == len(substr):
                    res.append(s)
                    cache[substr] = res
                    return res
        cache[substr] = []
        return []
    return help(domain)

def decompose_into_dictionary_words1(domain, dictionary):
    cache = {'': []}
    def help(substr):
        if substr in cache:
            return cache[substr]
        for s in dictionary:
            if substr.startswith(s):
                res = help(substr[len(s):])
                if res or len(s) == len(substr):
                    res.append(s)
                    cache[substr] = res
                    return res
        cache[substr] = []
        return []
    return help(domain)[::-1] # reverse

def decompose_into_dictionary_words(domain, dictionary):
    return decompose_into_dictionary_words3(domain, dictionary)

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))

import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# WIP

def decompose_into_dictionary_words(domain, dictionary):
    cache = {'': []}
    def help(substr):
        print(f"*** {substr}")
        if substr in cache:
            return cache[substr]
        for s in dictionary:
            if substr.startswith(s):
                res = help(substr[len(s):])
                if res or not s:
                    res.append(s)
                    cache[substr] = res
                    return res
        cache[substr] = []
        return []
    return help(domain)


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

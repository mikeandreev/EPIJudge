from test_framework import generic_test
from test_framework.test_failure import TestFailure

# DONE

def decoding(s):
    res = []
    n = 0
    for c in s:
        if c.isdigit():
            n = n*10 + int(c)
        else:
            res.append( c * n )
            n = 0
            
    return ''.join(res)


def encoding(s):
    res = ''
    n, prev = 1, s[0]
    for c in s[1:]:
        if c != prev:
            res += str(n)+prev
            n, prev = 1, c
        else:
            n += 1
    res += str(n)+prev
    return res


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))

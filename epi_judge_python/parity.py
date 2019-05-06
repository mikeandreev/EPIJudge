from test_framework import generic_test

# DONE [.]

def parity(x):
    res = 0
    while x:
        res ^= 1
        x &= (x-1) # drop lowest bit
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))

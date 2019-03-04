from test_framework import generic_test, test_utils

# DONE

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonic_rec(phone, prefixies, i):
    if(i == len(phone)):
        return prefixies
    mapping = MAPPING[ int(phone[i]) ]
    res = []
    for m in mapping:
        p = [prefix +m for prefix in prefixies]
        res += phone_mnemonic_rec(phone, p, i+1)
    return res

def phone_mnemonic(phone_number):
    return phone_mnemonic_rec(phone_number, [''], 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))


import unittest

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(  phone_mnemonic('012'), ['01A', '01B', '01C'])
        
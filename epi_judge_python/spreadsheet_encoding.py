from test_framework import generic_test

# DONE
import functools

def ss_decode_col_id(col):
    num = 0
    ordA = ord('A')
    base = 26 # ord('Z') - ordA + 1
    #
    #for c in col:
    #    num = num*base + (ord(c) - ordA + 1)
    #return num
    #
    return functools.reduce(
            lambda num, char: num*base + (ord(char) - ordA + 1),
            col, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
import unittest

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual( ss_decode_col_id("A"), 1)
    def test2(self):
        self.assertEqual( ss_decode_col_id("Z"), 26)
    def test3(self):
        self.assertEqual( ss_decode_col_id("AA"), 27)
    def test4(self):
        self.assertEqual( ss_decode_col_id("ZZ"), 702)


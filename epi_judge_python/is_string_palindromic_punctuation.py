from test_framework import generic_test

# DONE

def is_palindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if not s[i].isalnum(): i+= 1; continue
        if not s[j].isalnum(): j -= 1; continue
        if s[i].lower() != s[j].lower(): return False;
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))

import unittest

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(  is_palindrome('A man, a plan, a canal, Panama.'), True)
        
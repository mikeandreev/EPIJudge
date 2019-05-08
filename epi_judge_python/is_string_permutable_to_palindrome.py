from test_framework import generic_test

from collections import Counter

# DONE

def can_form_palindrome(s):
    return len([True for v in Counter(s).values() if v%2]) <= 1

def can_form_palindrome_1(s):
    c = Counter(s)
    has_odd = False
    for _ in (v for v in c.values() if v%2):
        if has_odd: return False
        else: has_odd = True
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))

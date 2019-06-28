from test_framework import generic_test

from collections import Counter
# DONE: with Counter
# DONE: using dict

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    stat = {}
    for c in letter_text:
        if c not in stat: stat[c] = 1
        else:             stat[c] += 1
    for c in magazine_text:
        if c in stat:
            val = stat[c]
            if val == 1:
                del stat[c]
                if not stat: return True
            else: stat[c] -= 1
    return (not stat)

def is_letter_constructible_from_magazine_wCounter(letter_text, magazine_text):
    check = Counter(letter_text) - Counter(magazine_text)
    return (not check) # True if chek is empty 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))

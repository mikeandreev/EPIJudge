from test_framework import generic_test

# DONE

def is_well_formed(s):
    stack = []
    opening_pair = { ')': '(', ']': '[', '}': '{' }
    for sym in s:
        if sym in opening_pair:
            if not stack or opening_pair[ sym ] != stack.pop():
                return False
        else:
            stack.append(sym)
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))

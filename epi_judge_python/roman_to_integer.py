from test_framework import generic_test

# DONE

ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# I can immediately precede V and X.
# X can immediately precede L and C.
# C can immediately precede D and M.
INCR = { 'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M'] }

def roman_to_integer(s):
    res = ROMAN[s[-1]] if len(s) else 0
    for c, c_next in zip(s, s[1:]):
        num = ROMAN[c]
        if c_next in INCR.get(c, []): res -= num
        else: res += num
    return res

INCR_CASES = { 1: [5, 10], 10: [50, 100], 100: [500, 1000] }
def roman_to_integer_2(s):
    res = 0
    for i in range(len(s)):
        num = ROMAN[s[i]]
        if i < len(s)-1 and ROMAN[s[i+1]] in INCR_CASES.get( num, [] ):
            res -= num
        else:
            res += num
    return res

def roman_to_integer_1(s):
    res = 0
    prev_num = 0
    for i in range(len(s)):
        num = ROMAN[s[i]]
        if prev_num:
            res += num - prev_num
            prev_num = 0
        else:
            if i < len(s)-1 and ROMAN[s[i+1]] in INCR_CASES.get( num, [] ):
                prev_num = num
            else:
                res += num
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))

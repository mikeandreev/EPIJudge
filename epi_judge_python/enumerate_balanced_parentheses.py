from test_framework import generic_test, test_utils

# problem 16.8
#
# (2) DONE (-+)
# (1) weak DONE
#

from math import ceil

def generate_balanced_parentheses2(num):
    result = []
    def hlp(left_parans_to_add, right_parans_to_add, prefix):
        if left_parans_to_add == 0 and right_parans_to_add == 0:
            result.append(prefix)
            return

        if left_parans_to_add > 0:
            hlp(left_parans_to_add-1, right_parans_to_add, prefix+'(' )
        if left_parans_to_add < right_parans_to_add:
            hlp(left_parans_to_add, right_parans_to_add-1, prefix+')' )
    hlp(num, num, "")
    return result

def generate_balanced_parentheses1(num):
    if num == 0:
        return [""]
    if num == 1:
        return ["()"]
    res = set()
    for i in range(0, num):
        j = num - i
        if j < 0:
            break
        arr2 = generate_balanced_parentheses(j)
        if i == j:
            for k in range(len(arr2)):
                for l in range(k, len(arr2)):
                    res.add(s1+s2)
        else:
            for s1 in generate_balanced_parentheses(i):
                for s2 in arr2:
                    res.add('('+s1+s2+')')
                    res.add('()'+s1+s2)
                    res.add(s1+s2+'()')
    return list(res)

def generate_balanced_parentheses(num):
    return generate_balanced_parentheses2(num)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))

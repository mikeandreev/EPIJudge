from test_framework import generic_test, test_utils

# DONE

def generate_power_set(S):
    res = [[]]
    pref = []
    def hlp(prev_indx):
        for i in range(prev_indx + 1, len(S)):
            pref.append(S[i])
            res.append(pref.copy())
            if i < len(S)-1:
                hlp(i)
            pref.pop()
    hlp(-1)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))

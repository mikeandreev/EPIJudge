from test_framework import generic_test

# problem 15.7
#
# v2 : DONE
# v1 : DONE
# (-+)
#

def palindrome_decompositions_v2(input):
    res = []
    def hlp(partial_decomposition, offset_indx):
        # offset_indx : is offset index _to_check_, end when it's out off bounds
        if offset_indx == len(input):
            res.append(partial_decomposition)
            return

        for i in range(offset_indx+1, len(input)+1):
            string = input[offset_indx:i]
            if string == string[::-1]:
                hlp(partial_decomposition + [string], i)

    hlp([], 0)
    return res

def palindrome_decompositions_v1(input):
    res = []
    cache = set()
    def hlp(arr):
        tup = tuple(arr)
        if tup in cache:
            return
        cache.add(tup)
        res.append(arr)
        n = len(arr)
        for i in range(1, n):
            if arr[i-1] == arr[i][::-1]:
                hlp( arr[:i-1] + ["".join(arr[i-1:i+1])] + arr[i+1:] )
            if i < n-1:
                if arr[i-1] == arr[i+1][::-1]:
                    hlp( arr[:i-1] + ["".join(arr[i-1:i+2])] + arr[i+2:] )
    single_char_decomp = list([str(c) for c in input])
    hlp(single_char_decomp)
    return res

def palindrome_decompositions(input):
    return palindrome_decompositions_v2(input)

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))

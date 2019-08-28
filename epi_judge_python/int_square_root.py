from test_framework import generic_test

# DONE

def square_root(k):
    low, n, high = 0, k//2, k
    while True:
        if n**2 <= k:
            if (n+1)**2 > k:
                break
            else:
                low = n
                n = (n+1+high)//2
        else:
            high = n
            n = (low+n)//2
    return n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))

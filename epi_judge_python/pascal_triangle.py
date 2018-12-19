from test_framework import generic_test

# DONE

def generate_pascal_triangle(n):
    arr = [ [0]*i for i in range(1, n+1) ]
    for r in range(n):
        arr[r][0] = arr[r][-1] = 1
        for i in range(1, r):
            arr[r][i] = arr[r-1][i-1] + arr[r-1][i]
    return arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))

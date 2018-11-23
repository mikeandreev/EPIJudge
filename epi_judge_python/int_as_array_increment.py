from test_framework import generic_test

# DONE

def plus_one(A):
    curry = True
    for i in reversed( range( len(A) ) ):
        A[i] += 1
        if A[i] <= 9:
            curry = False
            break
        else:
            A[i] = 0
    if curry:
        A[i] = 1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))

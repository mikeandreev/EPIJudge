from test_framework import generic_test

# DONE

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(A):
    for i in range(9):
        for j in range(9):
            if not A[i][j]: continue
            if any( [ A[x+3*(i//3 )][y+3*(j//3)] == A[i][j] for x in range(3) for y in range(3) if x != i%3 or y != j%3 ]):
                return False
            if any( [A[x][j] == A[i][j] for x in range(9) if x != i] ):
                return False
            if any( [A[i][x] == A[i][j] for x in range(9) if x != j] ):
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))

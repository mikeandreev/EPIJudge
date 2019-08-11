from test_framework import generic_test

# DONE

def is_pattern_contained_in_grid_graph_search(grid, S):
    if len(S) == 0:
        return True
    s = 0
    condidates = set()
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if S[s] == grid[j][i]:
                if len(S) == 1: return True
                condidates.add( (j, i) )
    for s in range(1, len(S)):
        next_condidates = set()
        for (j, i) in condidates:
            steps = [ (x1,i) for x1 in [j-1, j+1] if x1 >=0 and x1 <len(grid)]
            steps.extend( [ (j,x2) for x2 in [i-1, i+1] if x2 >= 0 and x2 <len(grid[j])] )
            for (k,l) in steps:
                if S[s] == grid[k][l]:
                    if s == len(S)-1: return True
                    next_condidates.add( (k, l) )
        condidates = next_condidates
    return len(condidates) > 0

# reproducing idea from the book
def is_pattern_contained_in_grid_book(grid, S):
    dead_ends = set()
    def hlp(j, i, s):
        if s == len(S):
            return True

        if (0 <= j < len(grid) and 0 <= i < len(grid[j])
            and S[s] == grid[j][i] and (j, i, s) not in dead_ends):
            for k, l in [(j, i-1), (j, i+1), (j-1, i), (j+1, i)]:
                if hlp(k, l, s+1):
                    return True
        dead_ends.add( (j, i, s) )
        return False
    return any( hlp(j, i, 0) for j in range(len(grid)) for i in range(len(grid[j])) )

is_pattern_contained_in_grid = is_pattern_contained_in_grid_graph_search

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))

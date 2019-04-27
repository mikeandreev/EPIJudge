from test_framework import generic_test
import collections

# DONE

def fill_surrounded_regions(board):
    Pos = collections.namedtuple('Pos', ('x', 'y'))
    visited = set()
    def dfs(i, j):
        pos = Pos(i, j)
        if board[i][j] == 'B' or pos in visited: return
        q = collections.deque()
        visited.add(pos); q.append(pos)
        while q:
            p = q.popleft()
            for x, y in (p.x-1, p.y), (p.x+1, p.y), (p.x, p.y-1), (p.x, p.y+1):
                next_pos = Pos(x, y)
                if 0 <= x < len(board) and 0 <= y < len(board[x]) and board[x][y] == 'W' and (next_pos not in visited):
                    visited.add(next_pos); q.append(next_pos)
    for i in range( len(board) ):
        dfs(i, 0);
        dfs(i, len(board[i])-1)
    for j in range( len(board[0]) ):
        dfs(0, j)
        dfs(len(board)-1, j)
    for i in range(1, len(board)-1 ):
        for j in range(1, len(board[i])-1 ):
            pos = Pos(i, j)
            if board[i][j] == 'W' and (pos not in visited):
                board[i][j] = 'B'
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))

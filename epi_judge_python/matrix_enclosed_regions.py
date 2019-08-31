from test_framework import generic_test
import collections

# bfs 1 : DONE
# bfs 2 : DONE


def fill_surrounded_regions_bfs2(board):
    n, m = len(board), len(board[0])
    q = collections.deque()
    border = [ (x , y) for x, y in ( 
        [(i, 0) for i in range( n ) ] +
        [(i, m-1) for i in range( n )] +
        [(0, j) for j in range( m )] +
        [(n-1, j) for j in range( m )] ) ]
    for x, y in border:
        if board[x][y] == 'W':
            board[x][y] = 'x'
            q.append((x, y))
    
    while q:
         x, y = q.popleft()
         for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
             if 0 <= i < n and 0 <= j < m and board[i][j] == 'W':
                 board[i][j] = 'x'
                 q.append((i, j))
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'x': board[i][j] = 'W'
            elif board[i][j] == 'W': board[i][j] = 'B'

def fill_surrounded_regions_bfs1(board):
    Pos = collections.namedtuple('Pos', ('x', 'y'))
    visited = set()
    def bfs(i, j):
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
        bfs(i, 0)
        bfs(i, len(board[i])-1)
    for j in range( len(board[0]) ):
        bfs(0, j)
        bfs(len(board)-1, j)
    for i in range(1, len(board)-1 ):
        for j in range(1, len(board[i])-1 ):
            pos = Pos(i, j)
            if board[i][j] == 'W' and (pos not in visited):
                board[i][j] = 'B'
    return


fill_surrounded_regions = fill_surrounded_regions_bfs2


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))

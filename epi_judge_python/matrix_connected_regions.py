from test_framework import generic_test
import collections

# DONE bfs
# DONE dfs

def flip_color(x, y, A):
    color = A[x][y]
    def hlp( n_x, n_y ):
        if n_x < 0 or n_x >= len(A) or n_y < 0 or n_y >= len(A[n_x]) or A[n_x][n_y] != color:
            return
        A[n_x][n_y] = 1 - A[n_x][n_y]
        for x1, y1 in (n_x-1, n_y), (n_x+1, n_y), (n_x, n_y-1), (n_x, n_y+1):
            hlp(x1, y1)
    hlp(x, y)        
    return

def flip_color_bfs(x, y, A):
    Pos = collections.namedtuple('Pos', ('x', 'y'))
    color = A[x][y]
    queue = collections.deque([Pos(x,y)])
    A[x][y] = not A[x][y]
    while queue:
        pos = queue.popleft()

        for n_x, n_y in (pos.x-1, pos.y), (pos.x+1, pos.y), (pos.x, pos.y-1), (pos.x, pos.y+1):
            if n_x < 0 or n_x >= len(A) or n_y < 0 or n_y >= len(A[n_x]) or A[n_x][n_y] != color:
                continue
            A[n_x][n_y] = not A[n_x][n_y]
            queue.append(Pos(n_x, n_y))
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))

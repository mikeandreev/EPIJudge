import collections
import copy
import functools

# DONE

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    visited = set()
    path = []
    def hlp(pos):
        if pos.x < 0 or pos.x >= len(maze) or \
        pos.y < 0 or pos.y >= len(maze[pos.x]) or \
        maze[pos.x][pos.y] == BLACK or pos in visited:
           return False

        visited.add(pos)
        path.append(pos)
        if pos == e: return True
        #for d in [(-1,0), (0,-1),(1,0), (0,1)]:
        #    found = hlp( Coordinate(pos.x + d[0], pos.y + d[1]) )
        #    if found: return found
        if any( map(lambda d: hlp(Coordinate(pos.x+d[0], pos.y+d[1])),  [(-1,0), (0,-1),(1,0), (0,1)] )):
            return True
        del path[-1]
        return False
        
    if hlp(s): return path
    else: return []

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))

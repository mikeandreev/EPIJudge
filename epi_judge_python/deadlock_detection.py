import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# dfs simple: DONE
# dfs full: DONE

WHITE, GREY, BLACK = range(3)

class GraphVertex:
    def __init__(self):
        self.edges = []

def is_deadlocked(graph):
    cache = {}
    def hlp(v):
        color = cache.get(id(v), WHITE)
        if color == GREY: return True
        elif color == BLACK: return False
        else: # WHITE
            cache[id(v)] = GREY
            if any( hlp(w) for w in v.edges): return True
            cache[id(v)] = BLACK
            return False
    
    return any( hlp(v) for v in graph)

def is_deadlocked_simple(graph):
    def hlp(v, seen):
        if id(v) in seen: return True
        seen.add(id(v))
        return any( hlp(w, seen) for w in v.edges )
    return any( hlp(v, set()) for v in graph)

@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))

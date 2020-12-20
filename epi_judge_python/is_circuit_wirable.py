import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import deque

# problem 18.6
#
# DONE
#

class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []


def is_any_placement_feasible(graph):
    if not graph: return False
    for node in graph:
      if node.d != -1:
        continue
      node.d = 0
      queue = deque([node])
      while queue:
        v = queue.popleft()
        next_d = 1 - v.d
        for u in v.edges:
        	if u.d == -1:
        		u.d = next_d
        		queue.append(u)
        	elif u.d == v.d:
        		return False
    return True


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))

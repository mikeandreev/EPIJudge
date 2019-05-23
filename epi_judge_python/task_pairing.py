import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

# DONE

def optimum_task_assignment(task_durations):
    task_durations.sort()
    n = len(task_durations)
    return [ PairedTasks(task_durations[i], task_durations[n-1-i]) for i in range(n//2)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))

import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

TimePoint = collections.namedtuple('TimePoint', ('time', 'is_finish'))

# DONE

def find_max_simultaneous_events(A):
    E = sorted([TimePoint(x.start, False) for x in A ] + [TimePoint(x.finish, True) for x in A])
    max_sim_events, sim_events = 0, 0
    for point in E:
        if not point.is_finish:
            sim_events += 1
            max_sim_events = max(max_sim_events, sim_events)
        else:
            sim_events -= 1
    return max_sim_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))

import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# problem 13.8
#
# v1 DONE +
# v2 WIP
#

Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age_v1(people):
    min_age, max_age = 1e5, 0
    for s in people:
    	min_age, max_age = min(min_age, s.age), max(max_age, s.age)
    cache = [ [] for _ in range(max_age-min_age+1)]
    for s in people:
    	cache[s.age - min_age].append(s)
    i = 0
    for c in cache:
    	for el in c:
    		people[i] = el
    		i += 1
    return

def group_by_age_v2(people):
    min_age, max_age = 1e5, 0
    for s in people:
    	min_age, max_age = min(min_age, s.age), max(max_age, s.age)
    cache = [ [] for _ in range(max_age-min_age+1)]
    for s in people:
    	cache[s.age - min_age].append(s)
    i = 0
    for c in cache:
    	for el in c:
    		people[i] = el
    		i += 1
    return


def group_by_age(people):
	return group_by_age_v2(people)

@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0]

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("group_equal_entries.py",
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))

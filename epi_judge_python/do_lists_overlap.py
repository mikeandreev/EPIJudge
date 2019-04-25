import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# DONE

def has_cycle(head):
    if not head: return None
    slow, fast = head, head.next
    while fast and fast.next:
        if slow is fast: # cycle is found
            # what is cycle length?
            it, cycle_len = slow.next, 1
            while it is not slow: it = it.next; cycle_len += 1
            #
            it1 = head
            for _ in range(cycle_len): it1 = it.next
            #
            it = head
            while it is not it1: it, it1 = it.next, it1.next
            return it
        slow = slow.next
        fast = fast.next.next
    return None

#
def overlapping_lists(l0, l1):
    #print('++++++')
    if not l0 or not l1: return None

    cycle0 = has_cycle(l0)
    cycle1 = has_cycle(l1)
    #print(':::::::')
    
    if not cycle0 and not cycle1:
        tail0, tail1, n0, n1 = l0, l1, 0, 0
        while tail0.next: tail0=tail0.next; n0+=1
        while tail1.next: tail1=tail1.next; n1+=1
        if tail0 is not tail1: return None
        
        if n0 > n1: l0, l1, n0, n1 = l1, l0, n1, n0
        for _ in range(n1-n0): l1 = l1.next
        while l0 is not l1: l0, l1 = l0.next, l1.next

        return l0
    
    if cycle0 and cycle1:
        if cycle0 is not cycle1:
            #print('====')
            it = cycle0.next
            while it is not cycle0:
                if it is cycle1: return cycle0
                it = it.next
            return None
        # cycle0 is cycle1
        n0, n1 = 0, 0
        it = l0
        while it is not cycle0: it=it.next; n0+=1
        it = l1
        while it is not cycle1: it=it.next; n1+=1
        
        if n0 > n1: l0, l1, n0, n1 = l1, l0, n1, n0
        for _ in range(n1-n0): l1 = l1.next
        #print(';;;;2')
        while l0 is not l1 and l0 is not cycle0: l0, l1 = l0.next, l1.next
        
        return l0
        
        
    return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))

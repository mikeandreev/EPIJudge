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
            #print( slow.data )
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


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", 'is_list_cyclic.tsv', has_cycle_wrapper))
            
import unittest

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
        
class TestSolution(unittest.TestCase):
    def test1(self):
        tail = ListNode(2)
        head = ListNode( 0, ListNode(1, tail))
        tail.next = head
        self.assertEqual( has_cycle(head).data, 0)
        
    def test2(self):
        tail = ListNode(4)
        head = ListNode( 0, ListNode(1, ListNode(2, ListNode(3, tail))))
        tail.next = head.next
        self.assertEqual( has_cycle(head).data, 1)

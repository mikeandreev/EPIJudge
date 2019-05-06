from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections

# DONE

Pair = collections.namedtuple('Pair', ('element', 'cached_max'))

class Stack:
    
    def __init__(self):
        self.s = []
        
    def empty(self):
        return len(self.s) == 0

    def max(self):
        if self.empty():
            raise IndexError('max:  stack is empty')
        return self.s[-1].cached_max

    def pop(self):
        if self.empty():
            raise IndexError('pop:  stack is empty')
        return self.s.pop().element

    def push(self, x):
        max_el = x
        if not self.empty():
            max_el = max(max_el, self.s[-1].cached_max)
        self.s.append(Pair(x, max_el))
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))

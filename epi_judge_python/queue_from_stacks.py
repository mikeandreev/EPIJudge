from test_framework import generic_test

# DONE

class Queue:
    def __init__(self):
        self._head_down = []
        self._tail_up = []
        return
        
    def enqueue(self, x):
        self._head_down.append(x)
        return

    def dequeue(self):
        if not self._tail_up:
            while self._head_down:
                self._tail_up.append(self._head_down.pop())
        return self._tail_up.pop()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))

from test_framework import generic_test
from test_framework.test_failure import TestFailure

# DONE

class Queue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.begin = 0
        self.end = 0
        return

    def enqueue(self, x):
        l = len(self.arr)
        if self.size() == l-1:
            #if self.end < self.begin:
            self.arr = self.arr[self.begin:] + self.arr[:self.begin] + [None]*l
            self.begin, self.end = 0, l-1
            #else:
            #    self.arr = self.arr + [None]*l
            l = len(self.arr)
        self.arr[self.end] = x
        self.end += 1
        if self.end == l:
            self.end = 0
        return

    def dequeue(self):
        #print("dequeue")
        if self.begin == self.end:
            raise RuntimeError( "queue is empty" )
        x= self.arr[self.begin]
        l = len(self.arr)
        if self.begin == l -1:
            self.begin = 0
        else:
            self.begin += 1
        return x

    def size(self):
        s = self.end - self.begin
        if s < 0:
            s = len(self.arr) + s
        return s


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))

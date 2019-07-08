from test_framework import generic_test
from test_framework.test_failure import TestFailure

# DONE

class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.isbn_dict = {}
        self.lst_head = Node(None)
        self.lst_tail = Node(None)
        self.lst_head.next, self.lst_tail.prev = self.lst_tail, self.lst_head
        return
        
    def rm_node(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
            
    def ins_node(self, node):
        node.next, self.lst_head.next.prev = self.lst_head.next, node
        node.prev, self.lst_head.next = self.lst_head, node
            
    def lookup(self, isbn):
        if isbn not in self.isbn_dict:
            return -1
        price, node = self.isbn_dict[isbn]
        self.rm_node(node)
        self.ins_node(node)
        return price

    def insert(self, isbn, price):
        if isbn in self.isbn_dict:
            _, node = self.isbn_dict[isbn]
            self.rm_node(node)
            self.ins_node(node)
            #self.isbn_dict[isbn] = (price, node) # not logical, but according to spec
            return
        if len(self.isbn_dict) == self.capacity:
            node = self.lst_tail.prev
            self.rm_node(node)
            del self.isbn_dict[node.id]
        node = Node(isbn)
        self.ins_node(node)
        self.isbn_dict[isbn] = (price, node)
                    
    def erase(self, isbn):
        if isbn not in self.isbn_dict:
            return False
        _, node = self.isbn_dict[isbn]
        self.rm_node(node)
        del self.isbn_dict[isbn]
        return True


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))

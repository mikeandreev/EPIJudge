from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def reverse_sublist_rec(L, start, finish):
    if not L or finish <= start: return L
    dummy_head = cur = ListNode(0, L)
    start +=1; finish += 1
    
    def hlp(L, start, finish):
        if finish <= 1: return L, L.next
        next = L.next
        new_head, end = hlp(next, start-1, finish-1)
        next.next, L.next = L, end        
        return new_head, end
    
    while start > 2:  
        cur = cur.next; start -= 1; finish -= 1
    cur.next, _ = hlp(cur.next, start-1, finish-1)
    return dummy_head.next


        
def reverse_sublist(L, start, finish):
    if not L or finish <= start: return L
    dummy_head = head = ListNode(0, L)
    
    for _ in range(1, start):  
        head = head.next
        
    cur = head.next
    for _ in range(finish - start):
        next = cur.next
        cur.next = next.next
        next.next = head.next
        head.next = next
        
    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))

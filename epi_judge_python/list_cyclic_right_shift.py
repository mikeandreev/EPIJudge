from test_framework import generic_test

# DONE

def cyclically_right_shift_list(L, k):
    if not L or not L.next:
        return L
        
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next
    k = k % n
    
    if k == 0:
        return L
    
    before_newhead = L
    i = 1
    while i < n-k:
        i += 1
        before_newhead = before_newhead.next
    newhead = before_newhead.next
    tail.next = L
    before_newhead.next = None
    
    return newhead


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))

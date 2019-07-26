from test_framework import generic_test

# DONE

def even_odd_merge(L):
    if not L: return L

    head, odd_head = L, L.next
    even_it, odd_it = head, odd_head
    while odd_it and odd_it.next:
        # changing links
        even_it.next, odd_it.next = odd_it.next, odd_it.next.next
        # moving iterators
        even_it, odd_it = even_it.next, odd_it.next

    even_it.next = odd_head

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))

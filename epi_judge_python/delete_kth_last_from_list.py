from test_framework import generic_test

# DONE

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    #if not L: return
    prev, it, i = L, L, 0
    while i < k:
        if not it: return
        it = it.next
        i += 1
    if not it:
        return L.next
    while it.next:
        prev, it = prev.next, it.next
    prev.next = prev.next.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))

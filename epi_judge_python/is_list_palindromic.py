from test_framework import generic_test

# DONE

def cmp(L1, L2):
    while L1 and L2:
        if L1.data != L2.data: return False
        L1, L2 = L1.next, L2.next
    return True

def rev_list(begin, end = None):
    tail = end
    while begin is not end:
        next_ = begin.next
        begin.next = tail
        tail = begin
        begin = next_
    return tail

def is_linked_list_a_palindrome(L):
    if not L: return True
    L1, L2, fast = L, L, L
    while fast and fast.next:
        L2, fast = L2.next, fast.next.next

    L2 = rev_list(L2)
    res = cmp(L1, L2)
    rev_list(L2)
    return res

def is_linked_list_a_palindrome_v1(L):
    if not L: return True
    l, n = L, 0
    while l:
        l, n = l.next, n+1
    k = n // 2
    L1, L2 = L, L
    for _ in range(k):
        L2 = L2.next
    if k > 1: L1 = rev_list(L1, L2)
    res = cmp(L1, L2 if n % 2 == 0 else L2.next)
    if k > 1: L1 = rev_list(L1, L2)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))

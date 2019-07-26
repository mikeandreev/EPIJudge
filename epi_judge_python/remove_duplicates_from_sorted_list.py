from test_framework import generic_test

# DONE

def remove_duplicates(L):
    node = L
    while node:
        while node.next and node.data == node.next.data:
            node.next = node.next.next
        node = node.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))

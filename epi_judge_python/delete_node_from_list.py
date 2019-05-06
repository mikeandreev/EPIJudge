import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# DONE

# Assumes node_to_delete is not tail.
def deletion_from_list(node):
    next = node.next
    node.data = next.data
    node.next = next.next
    return


@enable_executor_hook
def deletion_from_list_wrapper(executor, head, node_to_delete_idx):
    node_to_delete = head
    if node_to_delete is None:
        raise RuntimeError('List is empty')
    for _ in range(node_to_delete_idx):
        if node_to_delete.next is None:
            raise RuntimeError("Can't delete last node")
        node_to_delete = node_to_delete.next

    executor.run(functools.partial(deletion_from_list, node_to_delete))

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_node_from_list.py",
                                       'delete_node_from_list.tsv',
                                       deletion_from_list_wrapper))

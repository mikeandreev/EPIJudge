from test_framework import generic_test

#
# problem 9.12
#
# DONE
#

from binary_tree_node import BinaryTreeNode

def binary_tree_from_preorder_inorder(preorder, inorder):
    data2inorder = {data: i for i, data in enumerate(inorder)}

    def hlp(in_start, in_end, pre_indx):
        if in_start >= in_end:
            return None
        data = preorder[pre_indx]
        node = BinaryTreeNode(data)
        if in_end > in_start + 1:
            i = data2inorder[data]
            node.left = hlp(in_start, i, pre_indx+1)
            node.right = hlp(i+1, in_end, pre_indx+i-in_start+1)
        return node

    return hlp(0, len(inorder), 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))

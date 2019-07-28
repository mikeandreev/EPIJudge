from test_framework import generic_test

# DONE

def binary_tree_depth_order_norec_pythonic(tree):
    res = []
    if not tree:
        return res
    level = [tree]
    while level:
        res.append( [n.data for n in level] )
        level = [
            node
            for cur in level for node in (cur.left, cur.right)
            if node
        ]
    return res

def binary_tree_depth_order_norec(tree):
    res = []
    if not tree:
        return res
    level = [tree]
    while level:
        level_data, next_level = [], []
        for node in level:
            level_data.append(node.data)
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        res.append(level_data)
        level = next_level
    return res

def binary_tree_depth_order_rec(tree):
    res = []
    def hlp(node, depth):
        if not node:
            return
        if len(res) == depth:
            res.append([])
        res[depth].append(node.data)
        hlp(node.left, depth+1)
        hlp(node.right, depth+1)
    hlp(tree, 0)
    return res

binary_tree_depth_order = binary_tree_depth_order_norec

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))

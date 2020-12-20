from test_framework import generic_test

# problem 9.11
#
# DONE
# -+
#

def inorder_traversal(tree):
    res = []
    prev_node, node = None, tree
    while node:
    	if prev_node is node.parent:
    	  if node.left:
    	     next_node = node.left
    	  else:
    	    res.append(node.data)
    	    next_node = node.right or node.parent
    	elif prev_node is node.left:
    	  res.append(node.data)
    	  next_node = node.right or node.parent
    	else:
    	  next_node = node.parent
    	  
    	prev_node, node = node, next_node
          
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:24:39 2020

@author: Beejal
"""
from tree_graph_common import TreeNode, priint_tree
# =============================================================================
# For a given node, the next node is within the right sub-tree.
# We look for the left most node in the right sub-tree of current node.
# Like mentioned in the example below, to locate the next of node 5..
# we select the right sub-tree of 5 which is node 8. On this sub-tree, 
# the left most node is 6. Thus 6 is the next node to 5.
#                                        5
#                        ------------------------------------
#                        |                                   |
#                        2                                   8
#            -------------------------               -------------------------
#            |                       |               |                       |
#            1                       3               6                       9
#                                    |               |                       |
#                                    -----           ----                    ----
#                                        |               |                       |
#                                        4               7                       10
#
# Now what should we do if a given node doesn't have right sub-tree. Like node 1.
# For the nodes that don't have right sub-tree, we have to select the first parent which is right 
# to the node. So for node 2 is the first parent which is right to node 1. Thus node 2 will 
# become the next node to 1. Another example, for node 7 the parent is node 6. But node 6
# is left to node 7. So we move on up the the hierarchy. Now the parent of node 6 is node 8.
# And node is the parent which is right to the node 6. Thus the next node to node 7 is node 8. 
# =============================================================================
def get_next_node(node):
    # There is no next node if the incoming node is None
    if node is None:
        return None
    
    if node.right != None:
        # When we have right sub-tree 
        left_most_node = find_left_most(node.right)
        return left_most_node
    else:
        # When there is no right sub-tree
        child = node
        parent = node.parent        
        
        while (parent != None and parent.left != child):
            child = parent
            parent = parent.parent
        
        return parent
    
def find_left_most(node):
    n = node
    while (n.left != None):
        n = n.left
    return n


if __name__ == '__main__':
    # Let's create the nodes
    tn5  = TreeNode(5)
    tn3  = TreeNode(3)
    tn8  = TreeNode(8)
    tn2  = TreeNode(2)
    tn4  = TreeNode(4)
    tn1  = TreeNode(1)
    tn7  = TreeNode(7)
    tn6  = TreeNode(6)
    tn9  = TreeNode(9)
    tn10 = TreeNode(10)
    
    # Set the relationship between TreeNode objects
    tn5.left  = tn2
    tn5.right = tn8
    
    tn2.parent = tn5
    tn2.left   = tn1
    tn2.right  = tn3
    
    tn1.parent = tn2
    
    tn3.parent = tn2    
    tn3.right  = tn4
    
    tn4.parent = tn3

    tn8.parent = tn5
    tn8.left   = tn6
    tn8.right  = tn9
    
    tn6.parent = tn8
    tn6.right  = tn7
    
    tn7.parent = tn6

    tn9.parent = tn8
    tn9.right  = tn10

    priint_tree(tn5)
    
    # Let's find the next node for tn5
    node = get_next_node(tn5)
    name = node.name if node is not None else 'None'
    print(f'\nNext node for {tn5.name} = {name}')

    # Let's find the next node for tn1
    node = get_next_node(tn1)
    name = node.name if node is not None else 'None'
    print(f'\nNext node for {tn1.name} = {name}')

    # Let's find the next node for tn1
    node = get_next_node(tn7)
    name = node.name if node is not None else 'None'
    print(f'\nNext node for {tn7.name} = {name}')
    
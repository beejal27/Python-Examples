# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 07:47:18 2020
Given a Binary Tree, this program checks if it is Binary Search Tree.
Definition of Binary Search Tree:
    "all descendents on left of node n <= n < all descendents on right of node n"

@author: Beejal
"""

import BSTMinimalCreate as bstBuilder
from tree_graph_common import priint_tree


###########
#APPROACH#1 : Use In-Order Traversal (Left, Node, Right) on the given Binary Tree to form a list of node values
#             If the list is sorted in ascending order, then given Binary Tree is a Binary Search Tree.
#             It has one limitation. Check the code below to understand.  
###########

def binary_tree_to_array(node, arr):
    # Stopping condition
    if node == None:
        return None
    
    # Left Node
    binary_tree_to_array(node.left, arr)

    # 
    arr.append(node.name)
    
    binary_tree_to_array(node.right, arr)

def checkSorted(arr):
    for index in range(len(arr)-1):
        if arr[index] <= arr[index+1]:
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    # Test-1
    print('Test-1 :: APPROACH#1')
    bst1 = bstBuilder.createMinimalBST(range(1, 11))
    priint_tree(bst1)
    # Now pass on this bst to our new function binary_tree_to_array to create an array out of it.
    arr = []
    binary_tree_to_array(bst1, arr)
    print(arr)
    # Now let's check if the arr comes out as sorted
    res = checkSorted(arr)
    result = 'is' if res else 'is not'
    print(f'Given Binary tree {result} Binary Search Tree.\n')
    
    # Test-2
    print('Test-2 :: APPROACH#1')
    bst2 = bstBuilder.createMinimalBST([19, 20, 21, 22, 24, 24, 25, 25])
    priint_tree(bst2)
    # Now pass on this bst to our new function binary_tree_to_array to create an array out of it.
    arr = []
    binary_tree_to_array(bst2, arr)
    print(arr)
    # Now let's check if the arr comes out as sorted
    res = checkSorted(arr)
    result = 'is' if res else 'is not'
    print(f'Given Binary tree {result} Binary Search Tree.')
    print('Clearly this approach fails. Observe that last 25 is right to its \
          parent (which again is 25). The value on right to the node \
          must be greater than node. Hence this algorithm fails.\n Let us solve \
          this limitation with APPROACH#2')


###########
#APPROACH#2 Works on the basic definition of Binary Search Tree
#          "all descendents on left of node n <= n < all descendents on right of node n"
#          In this approach, for the node being assessed, it would be either left or right to its parent node.
#          If it's left then it should be <= parent node. parent node value is supplied by min_val argument.
#          And if it's right then it should be > parent node. parent node value is supplied by max_val argument.
###########
    
def checkBST(node, min_val, max_val):
    # Stopping Condition - Evaluate if it's correct????????
    if node == None:
        return True
    
    passed_min_val_condition = False
    passed_max_val_condition = False
    
    # If min_val is provided, given node is left to its parent.  
    # min_val is the value of parent. Hence given node's value should be less than min_val.
    if min_val == None:
        passed_min_val_condition = True
    else:
        if node.name <= min_val:
            passed_min_val_condition = True

    # If max_val is provided, given node is right to its parent.  
    # max_val is the value of parent. Hence given node's value should be greater than max_val.        
    if max_val == None:
        passed_max_val_condition = True
    else:
        if node.name > max_val:
            passed_max_val_condition = True
    
    if passed_min_val_condition and passed_max_val_condition:
        return checkBST(node.left, node.name, None) and checkBST(node.right, None, node.name)
    else:
        return False


if __name__ == "__main__":
    print('Test-1 :: APPROACH#2')
    priint_tree(bst1)
    res = checkBST(bst1, None, None)
    result = 'is' if res else 'is not'
    print(f'Given Binary tree {result} Binary Search Tree.\n')
    
    print('Test-2 :: APPROACH#2')
    priint_tree(bst2)
    res = checkBST(bst2, None, None)
    result = 'is' if res else 'is not'
    print(f'Given Binary tree {result} Binary Search Tree.\n')

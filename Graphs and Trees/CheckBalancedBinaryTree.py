# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:14:55 2020

Program to check if the given Binary Tree is Balanced. For the purpose of this
question, a balanced tree is defined to be a tree such that the heights of the 
two subtrees of any node never differ by more than 1.

@author: Beejal
"""
from tree_graph_common import TreeNode, priint_tree

DEBUG = True

if __name__ == "__main__":
    # Instantiate some TreeNode objects
    tn5 = TreeNode(5)
    tn3 = TreeNode(3)
    tn8 = TreeNode(8)
    tn2 = TreeNode(2)
    tn4 = TreeNode(4)
    tn1 = TreeNode(1)
    tn7 = TreeNode(7)
    tn6 = TreeNode(6)
    tn9 = TreeNode(9)
    
    # Set the relationship between TreeNode objects
    tn5.left  = tn3
    tn5.right = tn8
    
    tn3.left  = tn2
    tn3.right = tn4
    
    tn2.left = tn1
    
# =============================================================================
# So we have laid the tree as follows
#  5 C
#   3 L
#    2 L
#     1 L
#    4 R
#   8 R    
#     
# =============================================================================

# In Current form the tree is Unbalanced, Uncomment following line(s) (1st or 1st and 2nd or all 3) to make the Tree Balanced
#    tn8.left  = tn7
#    tn8.right = tn9
#    tn7.left  = tn6

# =============================================================================
# Uncommenting all 3 lines gives following Balanced Tree
#  5 C
#   3 L
#    2 L
#     1 L
#    4 R
#   8 R
#    7 L
#     6 L
#    9 R    
#     
# =============================================================================

# Starting from tn5 (which is root), print the Tree
    print('Printing Binary Tree...')
    priint_tree(tn5, 'C')
    print()


# Algorithm to check if Tree is Balanced

############
# APPROACH#1
############
def getHeight(tn):
    if tn == None:
        return 0
    
    # The maximum height from left branch and right branch plus one (for its own level)
    # is considered a TreeNodes height
    return max(getHeight(tn.left), getHeight(tn.right)) + 1

if __name__ == "__main__":
    if DEBUG:
        print('Height of Tree = ', getHeight(tn5))

#Now let's check if the tree is balanced
#Each node has two conditions to satisfy:
#    1. The height of current node's left subtree should not be greater than right subtree by more than 1
#    2. Both left and right subtree of current node should be balanced
def isBalanced(tn):
    if tn is None:
        return True
    
    left_height  = getHeight(tn.left)
    right_height = getHeight(tn.right)
    
    height_diff = left_height - right_height
    if DEBUG:
        print(f'\tHeight difference at Node {tn.name} = {height_diff}; LN = {left_height}, RN = {right_height}')
        
    if height_diff > 1:
        return False
    else:
      return isBalanced(tn.left) and isBalanced(tn.right)

if __name__ == "__main__":
    print('APPROCH#1')
    result = isBalanced(tn5)
    bal = 'balanced' if result else 'imbalanced'
    print(f'\tGiven Tree is {bal}') 
    
############
# APPROACH#2
############
# As can be seen above getHeight() method is called repeatedly on the same nodes.
# It can be avoided if we check the height difference in getHeight() method itself.
# Belong checkHeight() method is the revision of getHeight() method.
# If 

def checkHeight(tn):
    if tn == None:
        return 0
    
    left_height  = checkHeight(tn.left)
    if left_height == -1:
        return -1
    right_height = checkHeight(tn.right)
    if right_height == -1:
        return -1
    
    height_diff = left_height - right_height
    if DEBUG:
        print(f'\tHeight difference at Node {tn.name} = {height_diff}; LN = {left_height}, RN = {right_height}')

    if height_diff > 1:
        return -1
    else:
        node_height = max(left_height, right_height) + 1
        #print(f'\tHeight at Node {tn.name} = {node_height}')
        return node_height

def checkBalanced(tn):
    val = checkHeight(tn)
    result = False if val < 0 else True
    return result

if __name__ == "__main__":
    print('APPROCH#2')
    result = checkBalanced(tn5)
    bal = 'balanced' if result else 'imbalanced'
    print(f'\tGiven Tree is {bal}') 
    
    
    
    
    
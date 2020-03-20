# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:56:14 2020

Given an array of sorted numbers (ascending order), this program create a Binary Search Tree.
Binary Search Tree is a type of Binary Tree that meets following criteria.
all decendents on left of node n < n < all decendents on right of node n.
Binary Tree is a type of tree where each node has upto two children.

Learnings:
    1. 
    Python does not support method overloading; Initially I had two 
    createMinimalBST(..) method with different set of arguments. 
    But Python would only recognize the last method. Invoking the first method 
    would give error (createMinimalBST() missing 2 required positional 
    arguments: 'start' and 'end'). Hence I appended a little underscore to the
    second method name.

    
@author: Beejal
"""

DEBUG = True

class TreeNode:
    def __init__(self, name, left = None, right = None):
        self.name = name
        self.left = left
        self.right = right
        

def createMinimalBST(arr):
    tree = createMinimalBST_(arr, 0, len(arr), 'left')
    return tree


def createMinimalBST_(arr, start, end, side):
        
    if end <= start:
        print(f'start {start}, end {end}, side {side}')
        return None
    
    # Find the mid-point
    mid = (start + end)//2
    if DEBUG:
        print(f'start {start}, end {end}, side {side}, mid {mid}, value = {arr[mid]}')

    node = TreeNode(arr[mid])
    
    # Invoke BST Creation for Left Sub Tree
    node.left  = createMinimalBST_(arr, start, mid, 'left')
    
    # Invoke BST Creation for Right Sub Tree
    node.right = createMinimalBST_(arr, mid+1, end, 'right')
    return node


def priint(node, side, level=1):
    if node != None:
        spaces = ' ' * level
        print(f'{spaces}{node.name} {side}')
        level += 1
        priint(node.left, 'L', level)
        priint(node.right, 'R', level)

    
# Test
array = range(1,11)
bst = createMinimalBST(array)
print("\nPrinting Binary Search Tree...\n")
priint(bst, 'C')
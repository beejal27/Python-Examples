# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:56:14 2020

Given an array of sorted numbers (ascending order), this program creates a Binary Search Tree.
Binary Search Tree is a type of Binary Tree that meets following criteria.

    "all descendants on left of node n <= n < all descendants on right of node n"

Binary Tree is a type of tree where each node has upto two children.
Set DEBUG to True to see the verbose log statements. Helps better understand the inner working of algorithm.

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
from tree_graph_common import TreeNode, priint_tree

DEBUG = False

def createMinimalBST(arr):
    tree = createMinimalBST_(arr, 0, len(arr)-1, 'center')
    return tree


def createMinimalBST_(arr, start, end, side):
        
    if end < start:
        if DEBUG:
            print(f'start {start}, end {end}, side {side}')
        return None
    
    # Find the mid-point
    mid = (start + end)//2
    if DEBUG:
        print(f'start {start}, end {end}, side {side}, mid {mid}, value = {arr[mid]}')

    mid_node = TreeNode(arr[mid])
    
    # Invoke BST Creation for Left Sub Tree
    mid_node.left  = createMinimalBST_(arr, start, mid-1, 'left')
    
    # Invoke BST Creation for Right Sub Tree
    mid_node.right = createMinimalBST_(arr, mid+1, end, 'right')
    return mid_node



if __name__== "__main__" :
    #Test - Uncomment when needed to test
    array = range(1,10)
    bst = createMinimalBST(array)
    print("\nPrinting Binary Search Tree...\n")
    priint_tree(bst, 'C')
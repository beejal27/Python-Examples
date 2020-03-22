# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:36:42 2020
Given a BST (Binary Search Tree), this program creates a LinkedList for all the 
nodes which are at same level in the hierarchy.

Learnings:
    1. We have imported BSTMinimalCreate here. Using BSTMinimalCreate, I am able
    to access the methods (createMinimalBST, priint) and variables (DEBUG) defined inside
    this module.
    
@author: Beejal
"""

import BSTMinimalCreate as bstCreator
from LinkedList import LinkedList
from tree_graph_common import priint_tree


def bstToLinkedList(node):
    lists = []
    level = 0
    bstToLinkedList_(node,  lists, level)
    return lists


def bstToLinkedList_(root, lists, level):
    if root == None:
        return None
    
    # If the length of lists is equal to level, then an empty LinkedList 
    # for this level hasn't been created yet
    if len(lists) == level:
        ll = LinkedList()
        lists.append(ll)
    else:
        # Else grab the LinkedList for this level
        ll = lists[level]
    
    # Now add the root node at this level to this linked list
    ll.add(root)
    
    # This root node is going to have a left and right node
    # Recursively call this method on left and right node
    # Since left and right nodes are decendents, increase the level by 1
    level += 1
    bstToLinkedList_(root.left, lists, level)
    bstToLinkedList_(root.right, lists, level)
    

# Test
# Let's create a BST first using BSTMinimalCreate that we created before
if __name__ == "__main__":
    array = range(1,20)
    bst = bstCreator.createMinimalBST(array)
    print("\nPrinting Binary Search Tree...")
    priint_tree(bst, 'C')
    
    # Let's convert BST to LinkedList
    print("\nPrinting Levels...")
    lls = bstToLinkedList(bst)
    
    # Let's print the LinkedLists
    for index in range(len(lls)):
        ll = lls[index]
        print(f'Level = {index}')
        node = ll.head
        while node != None:
            print(node.data.name)
            node = node.next
    



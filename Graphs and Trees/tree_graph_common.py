# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:38:13 2020

@author: Beejal
"""

class TreeNode:
    def __init__(self, name, left = None, right = None):
        self.name = name
        self.left = left
        self.right = right

    def priint(self):
        print(self.name)


def priint_tree(node, side, level=1):
    if node != None:
        spaces = ' ' * level
        print(f'{spaces}{node.name} {side}')
        level += 1
        priint_tree(node.left, 'L', level)
        priint_tree(node.right, 'R', level)
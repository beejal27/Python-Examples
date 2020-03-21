# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 09:08:40 2020

Learning:
    Python does not have LinkedList class like many other languages (like Java).
    So I have created a Singly Linked List here.
    
@author: Beejal
"""

import re

# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
        self.last = None
    
    def add(self, element):
        node = Node(element)
        if self.head == None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def priint(self):
        node = self.head
        while node != None:
            typ = str(type(node.data))
#            print(typ)
#            print(re.findall(r'str|int', typ))
            if len(re.findall(r'str|int', typ)) > 0:
                print(node.data)
            else:
                node.data.priint()
            node = node.next
            

# Test - Uncomment to run test
llist = LinkedList()
for index in range(11, 20, 2):
    llist.add(index)

llist.priint()
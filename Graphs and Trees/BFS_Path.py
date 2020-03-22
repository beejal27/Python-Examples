# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 08:31:27 2020
Implemented Breadth First Search for Graphs to search if a path exists between two given nodes.

@author: Beejal
"""

import enum
class State(enum.Enum):
    NOT_VISITED = 0
    VISITED = 1


class Node:
    def __init__(self, name, adjacent = [], state = State.NOT_VISITED):
        self.name = name
        self.adjacent = adjacent
        self.state = state
    
    def add_adjacent(self, adj):
        self.adjacent = self.adjacent + adj

    def priint(self):
        print(f'Node = {self.name}')
        for adj in self.adjacent:
            print(f'{self.name} :: {adj.name}')

      
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def priint(self):
        for node in self.nodes:
            node.priint()


# Create Nodes
node_0 = Node(0)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)


# Add the Edges
node_0.add_adjacent([node_1, node_4, node_5])
node_1.add_adjacent([node_3, node_4])
node_2.add_adjacent([node_1])
node_3.add_adjacent([node_2, node_4])

# Create Graph
graph = Graph([node_0, node_1, node_2, node_3, node_4, node_5])
graph.priint()


# Implement BFS - Breath First Search
# The key to remember is use of Queue. Everything follows from there.
from queue import Queue

def search(graph, start, end):
    if start == end:
        return True
    
    q = Queue()
    q.put(start)
    
    while q.empty() == False:
        node = q.get()
        if node.state == State.NOT_VISITED:
            print("Assessing node : ", node.name)
            for adj in node.adjacent:
                if adj == end:
                    print(f'Found Path from {start.name} to {end.name}')
                    node.priint()
                    return True
                else:
                    q.put(adj)
            node.state = State.VISITED

    return False

# Run some tests
if __name__ == "__main__":
    print('\n')
    start, end = node_0, node_3
    print(f'Checking path from {start.name} to {end.name}')
    result = search(graph, start, end)  
    print(f'Path from {start.name} to {end.name} = {result}')
    print('\n')
    
    
    start, end = node_2, node_0
    print(f'Checking path from {start.name} to {end.name}')
    result = search(graph, node_2, node_0)
    print(f'Path from {start.name} to {end.name} = {result}')



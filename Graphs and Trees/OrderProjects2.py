# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:55:05 2020

@author: Beejal
"""
import enum
from collections import deque

DEBUG = True
class State(enum.Enum):
    BLANK = 1
    VISITING = 2
    VISITED = 3


class Project:
    def __init__(self, name):
        self.name = name
        self.map_children = {}
        self.STATE = State.BLANK
        
    def addChild(self, child):
        if child != None:
            name = child.name
            try:
                self.map_children[name]
            except KeyError:
                self.map_children[name] = child
    
    def getChildren(self):
        return list(self.map_children.values())

class Graph:
    def __init__(self, name):
        self.name = name
        self.map_nodes = {}
    
    def getOrCreate(self, name):
        try:
            return self.map_nodes[name]
        except KeyError:
            node = Project(name)
            self.map_nodes[name] = node
            return node
    
    def addEdge(self, project1, project2):
        proj1 = self.getOrCreate(project1)
        proj2 = self.getOrCreate(project2)
        proj1.addChild(proj2)

    def getNodes(self):
        return list(self.map_nodes.values())        

def orderProjects(projects):
    stack = deque()
    for project in projects:
        if DEBUG:
            print(f'Project {project.name}, {project.STATE}')
        if project.STATE == State.BLANK:
            if doDFS(project, stack) == False:
                return None

    return stack


def doDFS(project, stack):
    if DEBUG:
        print(f'DFS : {project.name} {project.STATE}')
    if project.STATE == State.VISITING:
        if DEBUG:
            print('Found Cicrular Dependency')
        return False
    
    if project.STATE == State.BLANK:
        project.STATE = State.VISITING
        children = project.getChildren()
        for child in children:
            if doDFS(child, stack) == False:
                return False
        if DEBUG:
            print(f'Stacked {project.name}')
        stack.append(project)
        project.STATE = State.VISITED

    return True
    
#        c
#        ^
#        |
#        |
#        d<--------------b
#        ^               ^
#        |               |
#        |               |
#        a<--------------f

if __name__ == '__main__':
    name = 'AikWarium Product Graph'
    g = Graph(name) 

    edges= ['a,d', 'f,b', 'b,d', 'f,a', 'd,c']
    for edge in edges:
        names = edge.split(',')
        g.addEdge(names[0], names[1])
    
    stack = orderProjects(g.getNodes())
    
    print('Build Order')
    if stack != None:
        for ind in range(len(g.getNodes())):
            node = stack.pop()
            print(node.name)
    else:
        print('Circular Dependency detected')

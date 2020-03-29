# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 08:52:39 2020

We are given a set of project dependencies like (f, a). Here project 'a' depends on project 'f'.
For any project to be built, all the dependencies should be built first.
Given a set of dependencies, we need to find the order in which the projects 
need to be built.

Example: (a, d), (f, b), (b, d), (f, a), (d, c) 
        c
        ^
        |
        |
        d<--------------b
        ^               ^
        |               |
        |               |
        a<--------------f

Parent_Project             Child_Projects
a                          [d]
f                          [b, a]
b                          [d]
d                          [c]

Project                    Dependencies
a                          1
b                          1
c                          1
d                          2
f                          0

Take out the projects with 0 Dependencies. In above case it's 'f'. Once 'f' is 
built, then the Depencencies of the projects that depend on 'f' 
(i.e. Child Projects of 'f') can be reduced by 1. We have 'b' & 'a' as Child Projects 
of 'f'. So let's reduce the Dependencies of these two projects.

Project                    Dependencies
a                          0   *
b                          0   *
c                          1
d                          2   

Again take out the projects with 0 Dependencies. Now we get 'b'. We repeat the 
same process for 'b' as we did for 'f'.

Finally the order in which the projects should be built is : ['f', 'b', 'a', 'd', 'c']

@author: Beejal
"""

class Project:
    
    def __init__(self, name):
        self.name = name
        self.map_children = {}
        self.dependencies = 0
    
    def addChild(self, child):
        name = child.name
        try:
            self.map_children[name]
        except KeyError:
            self.map_children[name] = child
            # Since child is dependent on parent, increase the dependency counter
            # for the child node
            child.incrementDependencies()
    
    def incrementDependencies(self):
        self.dependencies = self.dependencies + 1
    
    def decrementDependencies(self):
        self.dependencies = self.dependencies - 1
    
    def getChildren(self):
        return list(self.map_children.values())
    
    def getNumberDependencies(self):
        return self.dependencies
    
class Graph:
    def __init__(self):
        self.map_projects = {}
    
    def getOrCreate(self, name):
        try:
            proj = self.map_projects[name]
        except KeyError:
            proj = Project(name)
            self.map_projects[name] = proj
        
        return proj
    
    # project_2 is child of project_1
    # addEdge basically adds project_2 as a child of project_1.
    # Since project_2 is child of project_1, it increments the dependency 
    # counter of project_2 (child) by 1, to indicate project_2 is dependent on one more project.
    def addEdge(self, project_1, project_2):
        proj_1 = self.getOrCreate(project_1)
        proj_2 = self.getOrCreate(project_2)
        proj_1.addChild(proj_2)
        
    def getProjects(self):
        return list(self.map_projects.values())
            

def orderProjects(graph):
    orderedProjects = []
    projects = graph.getProjects()
    total_projects = len(projects)
    toBeProcessed = 0
    
    # Return me projects with zero dependencies
    projectWithoutDependencies(projects, orderedProjects)
    while toBeProcessed < total_projects:
        try:
            prj = orderedProjects[toBeProcessed]
        except IndexError:
            print('Error: We have circular dependency since there are projects to be ordered but the next one to be ordered is missing.')
            return []

        for child in prj.getChildren():
            child.decrementDependencies()
        
        projectWithoutDependencies(prj.getChildren(), orderedProjects)
        toBeProcessed += 1
        
    return orderedProjects

def projectWithoutDependencies(projects, orderedProjects):
    for proj in projects:
        if proj.getNumberDependencies() == 0:
            orderedProjects.append(proj)

# Let's create a few projects
if __name__ == '__main__':
    g = Graph()
    
  
    # Add 'c,b' for circular dependency
    edges= ['a,d', 'f,b', 'b,d', 'f,a', 'd,c']
    
    for edge in edges:
        names = edge.split(',')
        g.addEdge(names[0], names[1])
    
   
    print([op.name for op in orderProjects(g)])
        
            
""" author: Beejal Vibhakar
Given two nodes in a Binary Tree, this program finds common ancestor between these two nodes.
In the example given below, the two nodes are given as 7 & 15. The common ancestor between these
two nodes is 10.
                           20
                            |
                ------------------------
                |                      |
                10                     30
                |
            -------------
            |           |
            5           15
            |           |
       -------------    -----
       |           |        |
       3           7        17

The way we find this is measure the depth of each given node. Like depth of 7 is 3 whereas the depth of 15 is 2. 
Now the difference of depth (delta) between these two nodes is 1. So for the deeper node, we move up by 1 (delta)
and arrive at node 5. Now node 5 and node 15 are at same depth. From this point, each node takes equal steps
upwards to arrive at a common parent (if there is one). So we take start traversing upwards, one step at a time.
For every upward step we see if we have reached common parent. Like in our case, it would just take one step for 
both the nodes (node 5 and node 15) to arrive at a common parent. So 10 is common ancestor for nodes 7 and 15.

 """

from tree_graph_common import TreeNode, priint_tree
DEBUG = True

def common_ancestor(node_p, node_q):
    if DEBUG:
        print(f'Finding common ancestor beween {node_p.name} & {node_q.name}')
    # Let's first take difference of depth between given nodes
    delta = depth(node_p) - depth(node_q)
    if DEBUG:
        print(f'\tDelta between {node_p.name} and {node_q.name} = {delta}')
    node_upper = node_q if delta > 0 else node_p
    node_lower = node_p if delta > 0 else node_q
    if DEBUG:
        print(f'\tUpper Node {node_upper.name}, Lower Node {node_lower.name}')

    # Now we move node_lower upward by delta steps to arrive at a parent which is at same depth as node_upper
    delta = abs(delta)
    node_lower = moveUpBy(node_lower, delta)
    if DEBUG:
        print(f'\tArrived at {node_lower.name} after moving {delta} steps upwards')

    # Now that both the nodes are at same depth, we shall take one step upwards for both and compare the parents
    # they arrive at. We stop this process on arrival of common parent or any of the two nodes not able to have a 
    # parent.
    while node_lower != node_upper and node_upper is not None and node_upper is not None:
        node_lower = node_lower.parent
        node_upper = node_upper.parent
    
    if node_upper is not None and node_upper is not None:
        print(f'Common Ancestor between {node_p.name} and {node_q.name} = {node_lower.name}\n')
    else:
        print('There is not a common ancestor between given nodes')


def moveUpBy(node_lower, delta):
    while delta != 0:
        node_lower = node_lower.parent
        delta -= 1
    return node_lower

def depth(tn):
    depth = 0
    if tn is not None:
        parent = tn.parent
        while parent is not None:
            depth += 1
            parent = parent.parent
    return depth

if __name__ == '__main__':
    tn20 = TreeNode(20)
    tn10 = TreeNode(10)
    tn05 = TreeNode(5)
    tn03 = TreeNode(3)
    tn07 = TreeNode(7)
    tn15 = TreeNode(15)
    tn30 = TreeNode(30)
    tn17 = TreeNode(17)

    tn20.left = tn10
    tn20.right = tn30

    tn10.parent = tn20
    tn10.left = tn05
    tn10.right = tn15

    tn30.parent = tn20

    tn05.parent = tn10
    tn05.left = tn03
    tn05.right = tn07

    tn15.parent = tn10
    tn15.right = tn17

    tn03.parent = tn05
    tn07.parent = tn05
    tn17.parent = tn15

    priint_tree(tn20)

    #print(depth(None))
    common_ancestor(tn05, tn07)
    common_ancestor(tn07, tn17)
    common_ancestor(tn07, tn20)
    common_ancestor(tn07, tn10)
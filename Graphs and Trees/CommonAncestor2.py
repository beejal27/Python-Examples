""" author: Beejal Vibhakar
Given two nodes in a Binary Tree and the root node of the tree, this program finds common ancestor between these two nodes.
In the example given below, the two nodes are given as 7 & 15 and root node is 20. The common ancestor between these
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

The way we find this:
    1. First we check if both nodes p & q are covered by root node (read it as both nodes are under the root node)
    2. If yes, check if q is covered by p; in that case p is the common ancestor
    3. If not, check if p is covered by q; in that case q is the common ancestor
    3. If 2 and 3 are not true, then:
        Find the sibling of p. Also find the parent of p.
        Check if q is covered by sibling. If yes, sibling is the common ancestor.
        If not,
            Find the sibling of parent. Also find the parent of current parent.
            Check if q is covered by sibling. If yes, sibling is the common ancestor.
            continue loop

 """

from tree_graph_common import TreeNode, priint_tree
DEBUG = False

def common_ancestor(node_root, node_p, node_q):
    print(f'Finding common ancestor beween {node_p.name} & {node_q.name}')

    if covers(node_root, node_p) == False or covers(node_root, node_q) == False:
        return None
    if covers(node_p, node_q):
        return node_p
    if covers(node_q, node_p):
        return node_q
    sibling = get_sibling(node_p)
    parent = node_p.parent
    while covers(sibling, node_q) == False:
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent

def get_sibling(node):
    if DEBUG:
        print(f'\tRequested sibling of {node.name if node is not None else None}')
    sibling = None
    if node is not None and node.parent is not None:
        parent = node.parent
        sibling = parent.left if node == parent.right else parent.right
    if DEBUG:
        print(f'\tSibling of {node.name if node is not None else None} = {sibling.name if sibling is not None else None}')
    return sibling

def covers(node_one, node_two):
    if DEBUG:
        print(f'\tChecking if {node_one.name if node_one is not None else None} contains {node_two.name if node_two is not None else None}')
    if node_one is None or node_two is None:
        return False

    if node_one == node_two:
        if DEBUG:
            print(f'\t\t{node_one.name} contains {node_two.name}')
        return node_one      # Or return node_two
    return covers(node_one.left, node_two) or covers(node_one.right, node_two)

def priint_ca(ca):
        if ca != None:
            print(f'common ancestor = {ca.name}')
        else:
            print('There does not exist a common ancestor between given nodes')

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
    priint_ca(common_ancestor(tn20, tn07, tn30))
    priint_ca(common_ancestor(tn20, tn07, tn17))
    priint_ca(common_ancestor(tn20, tn07, tn10))

    

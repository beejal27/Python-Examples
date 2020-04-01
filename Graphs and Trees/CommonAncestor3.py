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
    2. If yes, check which side of root node p is (left or right). Also check which side of root node q is (left or right).
    3. If both are not on same side of root, then it means root is the common ancestor
    4. If both are left side of root then perform then 
        Make root.left as root.
        Again perform steps 2, 3, 4

 """

from tree_graph_common import TreeNode, priint_tree
DEBUG = True
import enum

class Side(enum.Enum):
    LEFT  = 'left'
    RIGHT = 'right'

def common_ancestor(node_root, node_p, node_q):
    print(f'Finding common ancestor beween {node_p.name} & {node_q.name}')

    # Check if node_p and node_q are covered by root node
    if covers(node_root, node_p) == False or covers(node_root, node_q) == False:
        return None
    
    return ancestor_help(node_root, node_p, node_q)

def ancestor_help(node_root, node_p, node_q):
    if node_root is None or node_root == node_p or node_root == node_q:
        return node_root
    
    # Check if node_p is on left or right of root node
    pIsOnLeft = True if covers(node_root.left, node_p) else False
    # Check if node_q is on left or right of root node
    qIsOnLeft = True if covers(node_root.left, node_q) else False

    # If they both are not on the same side of root node, then it means root node is the common ancestor
    if pIsOnLeft != qIsOnLeft:
        if DEBUG:
            print(f'\t {node_p.name} & {node_q.name} are not on same side of {node_root.name}.')
            print(f'\t And that means common ancestor is {node_root.name}')
        return node_root
    
    if DEBUG:
        print(f'\t {node_p.name} & {node_q.name} are on {Side.LEFT.name if pIsOnLeft else Side.RIGHT.name} side of {node_root.name}.')

    # If both are on the same side of root node, then we need to extend our search to the side they both are
    node_root = node_root.left if pIsOnLeft else node_root.right
    return ancestor_help(node_root, node_p, node_q)

def covers(node_one, node_two):
    # if DEBUG:
    #     print(f'\tChecking if {node_one.name if node_one is not None else None} contains {node_two.name if node_two is not None else None}')
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
    priint_ca(common_ancestor(tn20, tn05, tn07))
    # priint_ca(common_ancestor(tn20, tn07, tn30))
    # priint_ca(common_ancestor(tn20, tn07, tn17))
    # priint_ca(common_ancestor(tn20, tn07, tn10))  

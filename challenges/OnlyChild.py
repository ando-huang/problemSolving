'''
    Given a binary tree root, return the number of nodes that are an only child. A node n is an only child if its parent has exactly one child (n)

    Constraints
    n <= 100,000 where n is the number of nodes in root

    Example

    root = 0
          / \
         4   2
            /
           1
          /
         3

    Output > 2

    Since 1 and 3 are both only the only children of their parent nodes

    Problem link
    https://binarysearch.com/problems/Only-Child

'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if root is None:
        return 0
    if root.left and root.right:
        return solve(root.left) + solve(root.left)

    #TODO add missing lines

    else:
        return 0

'''
    Given a binary tree (root), find the value of the deepest node. If there is more than one deepest node, then return the leftmost one.

    Restraints
    n <= 100,000 where n is the number of nodes in the tree

    Example

        0
       / \
      5   9
         / \
        1   3
       / \
      4   2

> 4

    Explanation
    The nodes 2 and 4 have the same depth in the tree, so 4 is returned because it is leftmost between the two nodes.

    Before diving into the code, it may be helpful to
    - consider the problem, what is needed to determine the solution?
    - draw up your own potential solution

'''

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# How did the author intend for the solution to work?

#TODO fill in ???, find and repair any logical errors.
def solve(root):
    if root is None:
        ???
    def helper(root: TreeNode, depth):
        if ??? is ??? and ??? is ???:
            return ???
        l, r = ???
        if root.left is None:
            l = helper(???, ???)
        ??? root.right is None:
            r = helper(???, ???)
        if l[1] != -1 and l[1] >= r[1]:
            return 1
        elif r[1] != -1:
            return r
    helper(root, 100)







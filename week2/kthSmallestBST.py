'''
    Given a binary search tree root, and k return the kth 0-indexed smallest
    value in root. It is guaranteed that the tree has at least k + 1 nodes

    Constraints
    k <= n <= 100,000, where n is the number of nodes in the root

    Problem Link:
    https://binarysearch.com/problems/Kth-Smallest-in-a-Binary-Search-Tree
'''

def solve(root, k):
    lst = []
    def inOrder(root):
        if root is None:
            return
        inOrder(root.left)
        lst.append(root.val)
        inOrder(root.right)
    inOrder(root)
    return lst[k]

# TODO can you come up with a better solution?
# HINT do we need all the values in lst? How can we reduce that?

def solveFaster(root, k):
    val = -1
    def inOrder(root):
        if root is None:
            return [0, 0]
        if inOrder(root.left) < k:
            #TODO
            return []
        
        if counter == k:
            val = root.val
            return
        inOrder(root.right)

    


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root1 = TreeNode(2)
root2 = TreeNode(9)
root.left, root.right = root1, root2
root3 = TreeNode(7)

import OnlyChild
#import solutions

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def __main__():
    root0 = TreeNode(0)
    root1 = TreeNode(4)
    root2 = TreeNode(2)
    root3 = TreeNode(1)
    root4 = TreeNode(3)

    root0.left, root0.right = root1, root2
    root2.left = root3
    root3.left = root4

    got = OnlyChild.solve(root0)
#    expected = solutions.onlyChildCount(root)

    print("expected: " + str(2) + " got: " + str(got))

    root0 = TreeNode(1)
    root1 = TreeNode(3)
    root2 = TreeNode(1)
    root3 = TreeNode(1)

    root0.right = root1
    root1.left, root1.right = root2, root3

    got = OnlyChild.solve(root0)

    print("expected: " + str(1) + " got: " + str(got))

__main__()

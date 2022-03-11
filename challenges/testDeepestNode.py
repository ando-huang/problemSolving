
import DeepestNode
import solutions

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def __main__():
    root = TreeNode(0)
    root1 = TreeNode(5)
    root2 = TreeNode(9)
    root3 = TreeNode(10)
    root4 = TreeNode(1)
    root5 = TreeNode(3)
    root6 = TreeNode(4)
    root7 = TreeNode(2)

    root.left, root.right = root1, root2
    root2.left, root2.right = root3, root4
    root3.left, root3.right = root5, root6
    root4.right = root7

    got = DeepestNode.solve(root)
    expected = solutions.getDeepestNode(root)
    print(f"Expected "+ str(expected) + ", got " + str(got))

__main__()

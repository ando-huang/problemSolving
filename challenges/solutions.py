def getDeepestNode(root):
    def helper(root, depth):
        if root.left is None and root.right is None:
            return [root.val, depth]
        l, r = [-1, -1], [-1, -1]
        if root.left:
            l = helper(root.left, depth+1)
        if root.right:
            r = helper(root.right, depth+1)
        if l[1] != -1 and l[1] >= r[1]:
            return l
        elif r[1] != -1:
            return r

    return helper(root, 0)[0]

def onlyChildCount(root):
    if root is None:
        return 0
    if root.left and root.right:
        return self.solve(root.left) + self.solve(root.right)
    elif root.left is None and root.right:
        return 1 + self.solve(root.right)
    elif root.left and root.right is None:
        return 1 + self.solve(root.left)
    else:
        return 0

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

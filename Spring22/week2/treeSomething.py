'''
    Given a binary search tree root, and k return ???. 
    It is guaranteed that the tree has at least k + 1 nodes

    Constraints
    k <= n <= 100,000, where n is the number of nodes in the root

    Problem Link:
    ??? can you determine which bsearch problem this is?
'''

class TreeNode:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

def s(r, k):
    l = []
    def h(r):
        if r is None:
            return
        h(r.l)
        l.append(r.v)
        h(r.r)
    h(r)
    return l[k]

# TODO is there a better solution?

def betterS(r, k):
    return 0

def test():
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n2.l, n2.r = n0, n3
    n0.r, n3.r = n1, n4
    print(s(n2, 1))
    res = s(n2, 1)
    print(f"Expected {1}, got {s(n2, 1)}",)

test()  

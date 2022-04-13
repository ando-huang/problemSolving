'''
    Code written during the class
'''

# generic implementation of max(x, y)
def min(x, y):
    if x < y:
        return x
    return y
x = 0
def auxMin(x, y):
    return None

def auxMin(x, y, z):
    return None

def mergeLists(l1, l2):
    i, j = 0
    l3 = []
    while i < len(l1) and j < len(l2):
        tup = min(l1[i], l2[j]) 
        l3[i + j] = tup[0]
        if tup[1]:
            i += 1
        else:
            j += 1
    return l3


'''
    3
   2 5
  1   8
     7 9
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leftMostLowest(root) -> int:
    def NodeDepth(root, depth):
        depth += 1
        if not root.left and not root.right:
            return [depth, root.val]
        elif root.left and not root.right:
            return NodeDepth(root.left, depth)
        elif root.right and not root.left:
            return NodeDepth(root.right, depth)
        l = NodeDepth(root.left, depth) # [2, 1]
        r = NodeDepth(root.right, depth) # [3, 7]
        if l[0] >= r[0]: 
            return l
        else:
            return r
    return NodeDepth(root, 0)[1]
    
     
    
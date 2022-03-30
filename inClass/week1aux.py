def mergeArrays(a1, a2):
    a3 = [0 for i in range(len(a1)+len(a2))]
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a3[i+j] = a1[i]
            i += 1
        else:
            a3[i+j] = a2[j]
            j += 1
    while i < len(a1):
        a3[len(a2)+i] = a1[i]
        i += 1
    while j < len(a2):
        a3[len(a1)+j] = a2[j]
        j += 1
    return a3

a1 = [1, 2, 5]
a2 = [3, 4, 6]
print(mergeArrays(a1, a2))


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeLinkedLists(root1, root2):
    if root1 is None:
        return root2
    elif root2 is None:
        return root1
    merged = Node(-1)
    curr = merged
    while root1 and root2:
        print(root1.val + root2.val)
        if root1.val < root2.val:
            curr.next = root1
            root1 = root1.next
            curr = root1
        else:
            curr.next = root2
            root2 = root2.next
            curr = root2
    if root1:
        curr.next = root1
    elif root2:
        curr.next = root2
    return merged.next

def printLinked(root):
    if root is None:
        print("Empty LL!")
    while root:
        print(root.val, end=" ")
        root = root.next
    return

root1 = Node(0)
root2 = Node(1)
root3 = Node(2)
root4 = Node(3)
root5 = Node(4)
root1.next, root2.next = root2, root4
root3.next = root5

printLinked(root1)
printLinked(root3)

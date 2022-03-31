# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
         
class Solution:
    def solve(self, node):
        lst = []
        while node is not None:
            lst.append(node.val)
            node = node.next
        i, j = 0, len(lst)-1
        while i <= j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1
        return True

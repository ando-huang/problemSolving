# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        curr = node
        fast = curr
        count = curr.val # 2
        while curr:
            while fast and count > 0:
                fast = fast.next
                count -= 1
            if fast is None:
                curr.next = fast
                return node
            curr.next = fast
            curr = fast
            count = curr.val

        return node

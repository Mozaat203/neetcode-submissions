# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        stack = []

        fast= slow= head

        while fast and fast.next:

            stack.append(slow)
            slow = slow.next
            fast = fast.next.next

        while stack:
            thePoint = stack.pop()
            maxSum = max(maxSum, thePoint.val + slow.val)
            slow = slow.next

        return maxSum

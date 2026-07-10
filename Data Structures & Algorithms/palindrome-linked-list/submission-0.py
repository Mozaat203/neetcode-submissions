# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #stack solution

        stack = []

        current =head
        
        while current:
            stack.append(current.val)
            current =current.next

        current = head

        while current and current.val == stack.pop():
            current = current.next

        return not current
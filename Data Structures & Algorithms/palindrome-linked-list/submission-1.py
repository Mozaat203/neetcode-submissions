# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        self.current =head

        def recursion(node):
            if node is not None:
                if not recursion(node.next):
                    return False
                
                if self.current.val != node.val:
                    return False
                
                # here we move the main current node to the next so we can compare it with the recurisved one
                self.current = self.current.next

            return True

        return recursion(head)
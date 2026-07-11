# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def solve(node):
            if not node:
                return 1

            carry = solve(node.next)

            if carry ==1:
                if node.val==9:
                    node.val = 0
                    return 1
                else:
                    node.val+=carry
                    return 0

            else:
                return 0

        last_carry= solve(head)

        if last_carry == 1:
            node = ListNode(1)
            node.next = head
            return node
        
        
        return head


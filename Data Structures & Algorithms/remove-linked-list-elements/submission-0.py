# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to anchor the new list
        newHead = ListNode()
        
        node = newHead      
        current = head     
        
        while current:
            # 1. Fixed: Compare the node's VALUE (current.val), not the node object
            if current.val != val:
                node.next = current  # Link the valid node to our new list
                node = node.next     # Advance our new list's tail pointer
            
            current = current.next   # Move to the next node in the original list
            
        
        node.next = None
        
        # Return the actual head of the filtered list (skipping the dummy node)
        return newHead.next
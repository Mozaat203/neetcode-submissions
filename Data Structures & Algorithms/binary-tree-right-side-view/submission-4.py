# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        que= collections.deque()
        
        que.append(root)

        while que:
            lenq = len(que)  
            level = []

            for i in range(lenq):
                node= que.popleft()
                
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            if level:
                res.append(level[-1])

        return res
                    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        record = float('-inf')
        def dfs(node, record):
            if not node:
                return 0

            res = 1 if node.val >= record else 0
            record= max(record, node.val)
            res+= dfs(node.left, record)
            res+= dfs(node.right, record)

            return res
        return dfs(root, record)

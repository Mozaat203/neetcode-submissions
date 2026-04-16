class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subset, index , total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or index >= len(nums):
                return
            
            subset.append(nums[index])
            

            dfs(subset, index, total + nums[index])
            
            subset.pop()
            
            dfs(subset, index +1 , total)

        dfs([], 0, 0)
        return res

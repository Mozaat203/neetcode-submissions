class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs( subset , index , total ):
            if total == target:
                res.append(subset.copy())

            for j in range(index , len(nums)):
                if total + nums[j] > target:
                    return
                subset.append(nums[j])
                dfs( subset, j, total+nums[j])
                subset.pop()

        dfs([], 0, 0)
        return res

        


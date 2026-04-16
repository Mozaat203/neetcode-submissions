class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(index, subset):
            res.append(subset[::])

            for j in range(index, len(nums)):
                if (nums[j] == nums[j-1] and j > index):
                    continue
                subset.append(nums[j])
                dfs(j + 1 ,subset)
                subset.pop()


        dfs(0,[])
        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n-1] = 1
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]

        for j in range(n-2, -1, -1):
            suffix[j] = nums[j+1] * suffix[j + 1]

        for z in range(n):
            result[z] = prefix[z] * suffix[z]

        return result
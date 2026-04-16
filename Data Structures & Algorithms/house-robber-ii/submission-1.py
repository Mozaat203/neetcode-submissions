class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) ->int:
        if not len(nums):
            return 0

        if len(nums) == 1:
            return nums[0]

        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            arr[i] = max(nums[i]+arr[i-2], arr[i-1])

        return arr[-1]
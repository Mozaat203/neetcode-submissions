class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        array = [0] * len(nums)

        array[0] = nums [0]
        array[1] = max(nums[1], nums[0])


        for i in range(2, len(nums)):
            array[i] = max(array[i-2] + nums[i], array[i-1])

        return array[-1]



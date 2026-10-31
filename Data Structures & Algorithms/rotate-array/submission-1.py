class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """ Do not return anything, modify nums in-place instead."""
        trueRotates = k % len(nums)

        left, right = 0, len(nums) - 1  

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
        
        left, right = 0, trueRotates - 1  
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

        left, right = trueRotates, len(nums) - 1  
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

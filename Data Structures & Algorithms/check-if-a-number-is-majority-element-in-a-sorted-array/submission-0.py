class Solution:
    def lower_bound(self, nums:List[int], target:int) -> int:
        l = 0
        r = len(nums) - 1
        index = len(nums)


        while l<=r:
            m = l+ (r-l) // 2
            if nums[m] >= target:
                r = m - 1
                index = m
            else:
                l = m+1
        return index

    def upper_bound(self, nums:List[int], target:int) -> int:
        l = 0
        r = len(nums) - 1
        index = len(nums)


        while l<=r:
            m = l+ (r-l) // 2
            if nums[m] > target:
                r = m - 1
                index = m
            else:
                l = m+1
        return index

        
    
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        first_element = self.lower_bound(nums , target)
        next_to_last_element = self.upper_bound(nums, target)

        return next_to_last_element - first_element > len(nums) // 2





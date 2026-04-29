from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        total_product = 1
        
        # Step 1: Scanner Phase (O(N))
        for x in nums:
            if x == 0:
                zero_count += 1
            else:
                total_product *= x
        
        # Step 2: Dispatcher Phase (O(N))
        # Case 1: More than one zero makes every "except self" product 0
        if zero_count > 1:
            return [0] * n
        
        res = [0] * n
        for i in range(n):
            if zero_count == 1:
                # Case 2: Exactly one zero
                # Only the zero's index gets the product of everything else
                if nums[i] == 0:
                    res[i] = total_product
                else:
                    res[i] = 0
            else:
                # Case 3: No zeros
                # Use integer division to maintain int type and avoid float conversion
                res[i] = total_product // nums[i]
                
        return res
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Step 1: Get the exact length of the input array
        n = len(nums) 
        
        # Step 2: Create the target array with a size of 2 * n
        ans = [0] * (2 * n)
        
        # Step 3: Populate ans by looping through its entire range
        for i in range(2 * n):
            ans[i] = nums[i % n]
            
        return ans
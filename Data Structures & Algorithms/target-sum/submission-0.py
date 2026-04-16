class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Base case: if the target is mathematically impossible to reach
        if abs(target) > total_sum:
            return 0
            
        # The offset represents our mathematical "0"
        offset = total_sum
        cols = 2 * total_sum + 1
        n = len(nums)
        
        # Initialize the 2D DP table with 0s
        dp = [[0] * cols for _ in range(n + 1)]
        
        # "Ground Zero" initialization: 1 way to have sum of 0 with 0 elements
        dp[0][offset] = 1
        
        # Forward flow: Fill the table
        for i in range(1, n + 1):
            val = nums[i - 1]
            for j in range(cols):
                # Only branch if the previous cell actually has a path reaching it
                if dp[i - 1][j] > 0:
                    
                    # Path (+): Add the value, ensuring we don't go out of bounds
                    if j + val < cols:
                        dp[i][j + val] += dp[i - 1][j]
                        
                    # Path (-): Subtract the value, ensuring we don't drop below 0 index
                    if j - val >= 0:
                        dp[i][j - val] += dp[i - 1][j]
                        
        # The final answer lives in the last row, at the shifted target index
        return dp[n][target + offset]
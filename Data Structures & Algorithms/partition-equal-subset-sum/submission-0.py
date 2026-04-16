class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2      
        N = len(nums)
        
        # Initialize DP table with False
        # Rows: items (0 to N), Cols: sums (0 to target)
        dp = [[False] * (target + 1) for _ in range(N + 1)]

        # Base case: A sum of 0 is always possible (empty set)
        for i in range(N + 1):
            dp[i][0] = True

        # Filling the matrix
        for i in range(1, N + 1):
            for j in range(1, target + 1):
                # Hard Part 1: The Exclude Logic (always look at the row above)
                dp[i][j] = dp[i-1][j]

                # Hard Part 2: The Include Logic
                # We use i-1 to access nums because our dp table has an extra "zero" row
                if nums[i-1] <= j:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]

        # The final result is in the bottom-right cell
        return dp[N][target]
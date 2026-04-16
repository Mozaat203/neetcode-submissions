class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        
        # Guard clause: length must match exactly
        if n + m != len(s3):
            return False

        # Create DP table: (n+1) rows for s1, (m+1) cols for s2
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Base case: 0 characters of s1 and s2 form 0 characters of s3
        
        dp[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                # 1. Try coming from the cell above (using s1)
                if i > 0:
                    if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                        dp[i][j] = True
                
                # 2. Try coming from the cell to the left (using s2)
                if j > 0:
                    # We use 'or dp[i][j]' to make sure we don't overwrite a True from above
                    if dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                        dp[i][j] = True

        return dp[n][m]
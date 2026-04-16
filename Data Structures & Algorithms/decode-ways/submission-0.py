class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
    
        def dfs(i):
   
            if i == len(s):
                return 1

            if i in memo:
                return memo[i]

            if s[i] == "0":
                return 0

            res = dfs(i + 1)

            if i + 1 < len(s):
                two_digit = int(s[i:i+2])
                if 10 <= two_digit <= 26:
                    res += dfs(i + 2)

            memo[i] = res
            return res

        # Start the journey from the beginning of the string
        return dfs(0)
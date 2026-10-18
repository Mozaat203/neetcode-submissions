class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentLength = 0
        L = 0
        window = set()
        maxLength = 0
        for R in range(len(s)):
            
            while s[R] in window:
                window.remove(s[L])
                L += 1
                currentLength -= 1

            window.add(s[R])
            currentLength += 1

            maxLength = max(currentLength, maxLength)

        return maxLength




class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        s = s.strip()
        n=len(s)

        for i in range(n-1,-1,-1):
            if(ord(s[i]) == 32):
                return length
            length+=1
        return length
            
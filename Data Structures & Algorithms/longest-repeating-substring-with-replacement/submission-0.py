class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        max_current=0
        max_len=0

        count={}

        for right in range(len(s)):
            char=s[right]
            count[char]=count.get(char,0)+1
            max_current=max(max_current,count[char])

            window=right-left+1
            replacements=window-max_current

            if (replacements>k):
                count[s[left]]-=1
                left+=1
                window=right-left+1

            max_len=max(max_len,window)
        return max_len
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0  # Pointer for s
        j = 0  # Pointer for t
        
        len_s = len(s)
        len_t = len(t)
        
        # Scan through s to match as many characters of t as possible
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                # Found a match, move to the next character in t
                j += 1
            # Always move forward in s to keep searching
            i += 1
            
        # The number of characters left unmatched in t is the answer
        return len_t - j
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. Create a frequency map for the target string 't'
        # This tells us exactly what we need (e.g., {'A':1, 'B':1, 'C':1})
        target_count = Counter(t)
        window_count = {}
        
        # 2. Setup tracking variables
        # 'have' = count of unique characters in current window that meet the target requirement
        # 'need' = total number of unique characters required
        have, need = 0, len(target_count)
        
        # 'res' stores the best substring found so far
        # 'res_len' stores the length of that substring (initially infinity)
        res, res_len = "", float("infinity")
        
        # Left pointer for the sliding window
        left = 0
        
        # 3. Dynamic Sliding Window: Expand 'right' pointer
        for right in range(len(s)):
            char = s[right]
            
            # Add the current character to our window dictionary
            window_count[char] = window_count.get(char, 0) + 1
            
            # If this character is one we need, and we have exactly enough of it
            if char in target_count and window_count[char] == target_count[char]:
                have += 1
            
            # 4. Shrink Phase: While the window is valid (has all needed characters)
            while have == need:
                # Check if this valid window is smaller than our previous best
                if (right - left + 1) < res_len:
                    res = s[left : right+1]
                    res_len = right - left + 1
                
                # Try to shrink from the left to see if we can make it smaller
                # Remove the character at the 'left' pointer
                left_char = s[left]
                window_count[left_char] -= 1
                
                # CRITICAL CHECK: Did removing this character break our validity?
                # We only lose 'have' credit if the count drops strictly BELOW the target
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    have -= 1
                
                # Move left pointer forward
                left += 1
                
        return res
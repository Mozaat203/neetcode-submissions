class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Create count1 for the target string s1
        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        # 2. Setup for the sliding window on s2
        count2 = {}
        left = 0
        
        for right in range(len(s2)):
            char = s2[right]
            
            # Add current character to our window count
            count2[char] = count2.get(char, 0) + 1
            
            # 3. CRITICAL STEP: If we have "too many" of this character, shrink from left
            # We check count1.get(char, 0) to handle characters that aren't in s1 at all
            while count2[char] > count1.get(char, 0):
                left_char = s2[left]
                count2[left_char] -= 1
                left += 1
            
            # 4. Check if the valid window length matches s1's length
            if right - left + 1 == len(s1):
                return True
                
        return False
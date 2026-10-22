class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        current = 0
        lastElement = 0
        for num in nums:
            current += num
            lastElement += num
            prefix.append(current)
        
        for i in range(len(prefix)):
            left_sum = prefix[i-1] if i > 0 else 0
            right_sum = lastElement - prefix[i]
            if left_sum == right_sum:
                return i

            
        return -1

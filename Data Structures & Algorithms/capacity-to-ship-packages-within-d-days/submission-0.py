class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = right
        
        while left <= right:
            ourDays = 1 
            total = 0
            mid = (left + right) // 2 

            for weight in weights:
                total += weight
                if total > mid:
                    ourDays += 1
                    total = weight 

            if ourDays <= days:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        result = right

        while left <= right:
            mid = left + (right - left) // 2
            total = 0
            ourK = 1

            for num in nums:
                total += num
                if total > mid:
                    total = num
                    ourK += 1
                
                    

            if ourK <= k:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
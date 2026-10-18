class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 0

        maxSum = nums[0]
        currSum = 0

        for right in range(len(nums)):
            if currSum < 0:
                currSum = 0
                left = right


            currSum += nums[right]

            if currSum > maxSum:
                maxSum = currSum
                maxLeft, maxRight = left, right

            
        return maxSum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        myTarget = 0
        minLength = float("inf")

        for  R in range(len(nums)):
            myTarget += nums[R]

            while myTarget >= target:
                
                minLength = min(minLength, R - L +1)
                myTarget -= nums[L]
                L +=1

        
        return 0 if minLength == float("inf") else minLength
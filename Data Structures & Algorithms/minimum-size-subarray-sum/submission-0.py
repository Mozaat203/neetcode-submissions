class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = float("inf")
        myTarget = 0

        for R in range(len(nums)):
            myTarget += nums[R]

            while myTarget >= target:
                length = min(length, R-L+1)
                myTarget -= nums[L]
                L+=1

        return 0 if length == float("inf") else length
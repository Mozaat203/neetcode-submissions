class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum =0

        diffHash = {0 : 1}

        for num in nums:
            currSum += num
            diff = currSum - k

            res += diffHash.get(diff, 0)

            diffHash[currSum] = 1 + diffHash.get(currSum, 0)


        return res
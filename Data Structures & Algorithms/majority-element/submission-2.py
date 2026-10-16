class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            majority[num] +=1
            if maxCount < majority[num]:
                res = num
                maxCount = majority[num]

        return res
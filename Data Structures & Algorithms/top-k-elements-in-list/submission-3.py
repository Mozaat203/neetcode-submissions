class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1+count.get(i, 0)
        
        array = []
        for num, counter in count.items():
            array.append([counter,num])
        
        array.sort()

        res = []

        while len(res) < k:
            res.append(array.pop()[1])

        return res
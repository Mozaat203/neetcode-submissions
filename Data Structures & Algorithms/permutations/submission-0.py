class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res= []
        self.backtrack(nums,0)
        return self.res

    
    def backtrack(self, nums:List[list], index: int):
        if index==len(nums):
            self.res.append(nums[:])
            return

        for i in range(index, len(nums)):
            nums[index], nums[i]= nums[i], nums[index]
            self.backtrack(nums, index+1)
            nums[index], nums[i]= nums[i], nums[index]
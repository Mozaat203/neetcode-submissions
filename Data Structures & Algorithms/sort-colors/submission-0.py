class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors= [0,0,0]

        for i in nums:
            colors[i]+=1

        index= 0
        for z in range( len(colors) ):
            for j in range(colors[z]):
                nums[index]=z
                index+=1
        return nums
    

            

        
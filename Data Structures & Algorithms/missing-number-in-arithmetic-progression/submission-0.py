class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        l, r = 0, len(arr) -1
        n =len(arr)
        difference = (arr[n-1] - arr[0]) // n


        while l< r:
            m = l +(r-l) // 2
            if (arr[m] == arr[0]+ m* difference):
                l = m +1
            
            else:
                r = m 

        return arr[0] + difference * l
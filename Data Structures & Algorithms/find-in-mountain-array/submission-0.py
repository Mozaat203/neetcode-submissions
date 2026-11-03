# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        
        # 1. Find the peak index
        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                # Ascending slope: peak is to the right
                left = mid + 1
            else:
                # Descending slope: mid could be peak, or peak is to the left
                right = mid
                
        peak = left
        
        # 2. Binary search on the ascending left half
        left, right = 0, peak
        while left <= right:
            mid = left + (right - left) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # 3. Binary search on the descending right half
        left, right = peak + 1, length - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                # Descending slope: smaller values are to the right
                right = mid - 1
            else:
                # Descending slope: larger values are to the left
                left = mid + 1
                
        # Target not found in either half
        return -1
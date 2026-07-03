class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        array2 = len(arr) * [0]
        n = len(arr) 

        right = arr[n-1]
        array2[n-1] = -1
        for i in range(n-2, -1, -1):
            current = arr[i]
             
            array2[i] = right

            if right<current:
                right = current

        return array2 
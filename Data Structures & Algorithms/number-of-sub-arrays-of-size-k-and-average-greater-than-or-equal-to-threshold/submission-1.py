class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        numberOfThresholds = 0
        SumOfElements = 0
        avg = 0
        
        for R in range(len(arr)):
            SumOfElements += arr[R]
            if (R - L + 1 == k):
                avg = SumOfElements / k
                if (avg >= threshold):
                    numberOfThresholds += 1
                
                SumOfElements -= arr[L]
                L += 1

        return numberOfThresholds
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        total = 0
        avg = 0
        numberOfThresholds = 0
        
        for R in range(len(arr)):
            total += arr[R]

            if (R-L +1 == k):
                avg = total / k

                if (avg >=  threshold):
                    numberOfThresholds += 1

                total -= arr[L]
                L += 1
        return numberOfThresholds



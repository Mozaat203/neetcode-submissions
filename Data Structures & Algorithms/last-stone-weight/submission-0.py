class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)

        while n>1:
            current = stones.pop() - stones.pop()
            n -=2

            if current > 0:
                left, right = 0, n
                while left < right:
                    mid = (left+right) // 2
                    if stones[mid] < current:
                        left = mid + 1
                    else:
                        right = mid

                position = left
                n+=1

                stones.append(0)
                for i in range(n - 1, position, -1):
                    stones[i] =stones[i-1]
                stones[position] = current

        return stones[0] if n > 0 else 0

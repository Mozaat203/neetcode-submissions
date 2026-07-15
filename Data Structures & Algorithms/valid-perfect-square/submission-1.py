class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid

            if square == num:
                return True
            elif square > num:
                r = mid - 1
            else:
                l = mid + 1

        return False
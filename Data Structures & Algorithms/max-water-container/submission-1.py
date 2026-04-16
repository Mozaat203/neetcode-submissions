class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = 0

        while left < right:
            distance = right - left
            current_area = distance * min(heights[left], heights[right])
            area = max(area, current_area)

            # Move the pointer pointing to the shorter line
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area

# 11. Container With Most Water
# Ref: https://leetcode.com/problems/container-with-most-water/description/
# Solution Ref: AM
# tags: array, two-pointers, medium, container-with-most-water, AM

class Solution:
    def maxArea(self, height: List[int]) -> int:
        longest = max(height)
        area = 0
        left = 0
        right = len(height) - 1

        while(area < (right - left) * longest):
            area = max(area, min(height[left], height[right]) * (right - left))

            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return area

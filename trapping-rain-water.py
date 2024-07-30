# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/
# Tags: bca, day-2
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_wall = [None] * length
        for i in range(length):
            if i == 0:
                left_wall[i] = 0
            else:
                left_wall[i] = max(height[i - 1], left_wall[i - 1])
        
        right_wall = [None] * length
        for i in range(length - 1, -1, -1):
            if i == length - 1:
                right_wall[i] = 0
            else:
                right_wall[i] = max(height[i + 1], right_wall[i + 1])

        total_storage = 0
        for i in range(length):
            actual_water = min(left_wall[i], right_wall[i]) - height[i]
            if actual_water > 0:
                total_storage += actual_water
        
        return total_storage

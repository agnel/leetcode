# 223. Rectangle Area
# Ref: https://leetcode.com/problems/rectangle-area/description/
# tags: bca, day-4, assignment

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # let's the areas of two rectangles
        area1 = abs(ay2 - ay1) * abs(ax2 - ax1)
        area2 = abs(by2 - by1) * abs(bx2 - bx1)

        # let's find intersection length and width
        length = max(0, min(ax2, bx2) - max(ax1, bx1))
        width = max(0, min(ay2, by2) - max(ay1, by1))

        return area1 + area2 - (length * width)

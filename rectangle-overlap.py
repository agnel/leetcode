# 836. Rectangle Overlap
# Ref: https://leetcode.com/problems/rectangle-overlap/description/
# tags: practice, math, rectangle-overlap
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1x1, r1y1, r1x2, r1y2 = rec1
        r2x1, r2y1, r2x2, r2y2 = rec2

        return not (r1x1 >= r2x2 or r1y1 >= r2y2 or r1x2 <= r2x1 or r1y2 <= r2y1)

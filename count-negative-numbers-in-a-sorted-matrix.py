# 1351. Count Negative Numbers in a Sorted Matrix
# Ref: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
# tags: bca, day-3, assignment
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # rows, cols
        top = 0
        right = n - 1
        count = 0

        while right >= 0 and top < m:
            if grid[top][right] < 0:
                count += m - top
                right -= 1
            else:
                top += 1

        return count

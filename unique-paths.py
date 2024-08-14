# 62. Unique Paths
# Ref: https://leetcode.com/problems/unique-paths/description/
# tags: bca, day-4, assignments, maths-1, maths-2
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))

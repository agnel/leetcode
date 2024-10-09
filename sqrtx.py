# 69. Sqrt(x)
# Ref: https://leetcode.com/problems/sqrtx/
# tags: bca, day-6, easy, math, binary-search, sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x + 1

        while l < r:
            m = l + (r - l) // 2
            if m * m <= x:
                l = m + 1
            else:
                r = m

        return l - 1

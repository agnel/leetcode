# 483. Smallest Good Base
# Ref: https://leetcode.com/problems/smallest-good-base/description/
# Solution: https://github.com/agnel/leetcode/blob/main/smallest-good-base.md
# tags: bca, day-6, math, binary-search, smallest-good-base
import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        # refer to solution to know why we need this
        max_m = int(math.log(n, 2))

        for m in range(max_m, 1, -1):
            # this is the range of base
            l, r = 2, n - 1
            while l <= r:
                k = l + (r - l) // 2
                # refer to solution to know why we use this formula
                guess = (k**(m + 1) - 1) // (k - 1)
                if guess == n:
                    return str(k)
                elif guess < n:
                    l = k + 1
                else:
                    r = k - 1

        return str(n - 1) 

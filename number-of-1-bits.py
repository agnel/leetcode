# 191. Number of 1 Bits
# Ref: https://leetcode.com/problems/number-of-1-bits/description/
# tags: bca, day-5, bit manipulation, easy
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        return count

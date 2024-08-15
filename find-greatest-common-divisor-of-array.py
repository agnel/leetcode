# 1979. Find Greatest Common Divisor of Array
# Ref: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
# tags: self-practice, math, gcd, array
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = mx = nums[0]
        for n in nums:
            mx = max(mx, n)
            mn = min(mn, n)

        for n in range(mn, 0, -1):
            if mn % n == 0 and mx % n == 0:
                return n

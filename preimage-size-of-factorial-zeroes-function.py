# 793. Preimage Size of Factorial Zeroes Function
# Ref: https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
# Solution Ref: (optimized) https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/solutions/2966459/python3-solution-binary-search
# tags: bca, day-6, math, binary-search, preimage-size-of-factorial-zeroes-function
class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        while n > 0:
            n //= 5
            c += n
        return c

    def preimageSizeFZF(self, k: int) -> int:
        l = 0
        r = 5 * (k + 1) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            tz = self.trailingZeroes(m)

            if tz < k: l = m + 1
            elif tz > k: r = m - 1
            else: return 5

        # Why we will take return 0 or return 5 in answer ?
        # Because we will get a range of 5 integers,
        # as in the formula above we are dividing by 5. Ex: 5! = 1 zero.
        # 6!, 7!, 8!, 9! will also give 1 zero each.
        # 10! will have 2 zeroes at the end.
        # hence the range has a size of 5 [5!,6!,7!,8!,9!]
        return 0

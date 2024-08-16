# 1281. Subtract the Product and Sum of Digits of an Integer
# Ref: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
# tags: bca, day-4, assignment
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        while n:
            # returns a tuple containing the quotient and remainder
            n, digit = divmod(n, 10)
            p, s = p * digit, s + digit
        return p - s

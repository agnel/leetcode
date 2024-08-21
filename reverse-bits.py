# 190. Reverse Bits
# Ref: https://leetcode.com/problems/reverse-bits/description/
# tags: bca, day-5, assignment
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        size = 32 # no of bits of a integer
        for i in range(1, size + 1):
            bit = (n >> (i - 1)) & 1
            new_position = (size - i) + 1
            mask = bit << (new_position - 1)
            ans = ans | mask
        return ans

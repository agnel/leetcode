# 136. Single Number
# Ref: https://leetcode.com/problems/single-number/description/
# tags: bca, day-5, assignment
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result

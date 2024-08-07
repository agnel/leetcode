# 1480. Running Sum of 1d Array
# Ref: https://leetcode.com/problems/richest-customer-wealth/description/
# tags: bca, day-3, assignment
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0] * len(nums)
        for i, n in enumerate(nums):
            runningSum[i] = runningSum[i - 1] + n
        
        return runningSum

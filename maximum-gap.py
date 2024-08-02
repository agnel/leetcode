# 164. Maximum Gap
# Ref: https://leetcode.com/problems/maximum-gap/
# tags: bca, day-2, assignment
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        maxDiff = nums[1] - nums[0]

        for i in range(2, len(nums)):
            maxDiff = max(maxDiff, nums[i] - nums[i - 1])

        return maxDiff

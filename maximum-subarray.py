# 53. Maximum Subarray
# Ref: https://leetcode.com/problems/maximum-subarray/
# Ref: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# tags: bca, day-2, assignment
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m1 = nums[0]
        m2 = nums[0]
        for i in range(1, len(nums)):
            m1 = max(m1 + nums[i], nums[i])
            m2 = max(m1, m2)
        return m2

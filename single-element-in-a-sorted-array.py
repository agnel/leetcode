# 540. Single Element in a Sorted Array
# Ref: https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# tags: bca, day-6, searching, array, binary-search, medium, single-element
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 2 # this is important, r is second to last

        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == nums[m ^ 1]:
                l = m + 1
            else:
                r = m - 1
        
        return nums[l]

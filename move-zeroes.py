# 283. Move Zeroes
# Ref: https://leetcode.com/problems/move-zeroes/description/
# Solution Ref: AM
# tags: move-zeroes, array, two-pointers, AM

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1:
        # using two pointers
        # fast to find the non-zero elements
        # slow to replace the zero with non-zero elements with
        # that the fast pointer found
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

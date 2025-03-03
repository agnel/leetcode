# 283. Move Zeroes
# Ref: https://leetcode.com/problems/move-zeroes/description/
# Solution Ref: AM
# tags: move-zeroes, array, two-pointers, AM

class Solution:
    # Approach 1:
    # using two pointers
    # fast to find the non-zero elements
    # slow to replace the zero with non-zero elements with
    # that the fast pointer found
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

    # Approach 2:
    # use a single pointer i.e. `i`
    # for iterating over the array
    # iterate over the nums of the array
    # for each number `n` in nums, if it is non-zero
    # we replace it with the number at i
    # and then once all the non-zero nums are copied
    # at the start of the array
    # set all the other remaining positions to zero
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        
        while i < len(nums):
            nums[i] = 0
            i += 1

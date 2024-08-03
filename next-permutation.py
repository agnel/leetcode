# 31. Next Permutation
# Ref: https://leetcode.com/problems/next-permutation/
# tags: bca, day-3, assignment
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        j = len(nums) - 1
        if i >= 0:
            while nums[j] <= nums[i]:
                print(i, j, nums[i], nums[j])
                j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        start, end = i + 1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

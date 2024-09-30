# 33. Search in Rotated Sorted Array
# Ref: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# tags: bca, day-6, searching, array, binary-search, medium, pivot
class Solution:
    # pivot means the index of the smallest element
    # in an unrotated array it will be 0 i.e. the first element
    def find_pivot(self, nums: List[int]) -> int:
        l = 0 # low
        r = len(nums) - 1 # high
        while l < r:
            # mid = low + (high - low) / 2
            m = l + ((r - l) // 2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return l

    def binary_search(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1
            

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot = self.find_pivot(nums)
        ans = -1

        if target >= nums[pivot] and target <= nums[r]:
            ans = self.binary_search(nums, target, pivot, r)
        else:
            ans = self.binary_search(nums, target, l, pivot)

        return ans

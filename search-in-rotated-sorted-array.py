# 33. Search in Rotated Sorted Array
# Ref: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# tags: bca, day-6, searching, array, binary-search, medium, pivot
class Solution:
    class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1

        # pivot means the index of the smallest element
        # in an unrotated array it will be 0 i.e. the first element
        while l < r:
            mid = l + ((r - l) // 2)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        # decide the range for searching out target
        if pivot == 0:
            l, r = 0, n - 1
        elif target >= nums[pivot] and target <= nums[n - 1]:
            l, r = pivot, n - 1
        else:
            l, r = 0, pivot - 1

        # use binary search for searching
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

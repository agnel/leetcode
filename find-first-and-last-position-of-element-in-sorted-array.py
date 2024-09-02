# 34. Find First and Last Position of Element in Sorted Array
# Ref: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Solution Ref: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/5378191/video-binary-search-solution
# Solution: https://www.youtube.com/watch?v=441pamgku74
# tags: bca, day-6, searching, array, binary-search, medium
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(nums, target, searching_left):
            lo = 0
            hi = len(nums) - 1
            idx = -1

            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    idx = mid
                    if searching_left:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return idx

        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)

        return [left, right]

# 90. Subsets II
# Ref: https://leetcode.com/problems/subsets-ii
# tags: bca, day-7, medium, array, backtracking, bit-manipulation, subsets-ii
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start_index, candidate):
            result.append(candidate[:])

            for i in range(start_index, len(nums)):
                if i != start_index and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, candidate + [nums[i]])

        backtrack(0, [])

        return result

# 494. Target Sum
# Ref: https://leetcode.com/problems/target-sum/
# Solution Ref: https://leetcode.com/problems/target-sum/solutions/4776428/107-1-approach-1-o-2-n-python-c-step-by-step-explanation
# tags: bca, day-7, medium, array, dynamic-programming, backtracking, target-sum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])

            return dp[(i, total)]

        
        return backtrack(0, 0)

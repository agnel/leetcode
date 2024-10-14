# 216. Combination Sum III
# Ref: https://leetcode.com/problems/combination-sum-iii/
# Solution Ref: https://leetcode.com/problems/combination-sum-iii/solutions/843394/python-simple-solution-explained-video-code-backtracking
# Video: https://youtu.be/J2hcPZRpbMk
# tags: bca, day-7, practice, array, backtracking, medium, combination-sum-iii, amazon, sde-1
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(num, combination, target):
            if len(combination) == k:
                if target == 0:
                    res.append(combination[:])
                return # return anyway even if the target is not 0, since the combination was not found.

            for x in range(num + 1, 10):
                if x <= target:
                    backtrack(x, combination + [x], target - x)
                else:
                    return

        backtrack(0, [], n)

        return res

# 39. Combination Sum
# Ref: https://leetcode.com/problems/combination-sum/
# Solution Ref: https://www.youtube.com/watch?v=GBKI9VSKdGg
# tags: bca, day-7, medium, array, backtracking, combination-sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        length = len(candidates)
        combination = []

        def backtrack(candidates, sum_total):
            if sum_total == target:
                result.append(combination[:])
                return
            if sum_total > target or not candidates:
                return

            combination.append(candidates[0])
            backtrack(candidates, sum_total + candidates[0])
            combination.pop()
            backtrack(candidates[1:], sum_total)
        
        backtrack(candidates, 0)

        return result

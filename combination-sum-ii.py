# 40. Combination Sum II
# Ref: https://leetcode.com/problems/combination-sum-ii
# Solution Ref: https://leetcode.com/problems/combination-sum-ii/editorial/
# tags: bca, day-7, medium, array, backtracking, combination-sum-ii
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() # in-place sorting
        length = len(candidates)
        
        def backtrack(start, combination, target):
            if target < 0:
                return # backtrack immediately, since no solution found
            if target == 0:
                result.append(combination[:])
                return # solution found
            
            for i in range(start, length):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # This condition will prune the tree faster.
                # It brought down the runtime from 63ms to 34 ms
                # when the solution was submitted with it.
                if candidates[i] > target:
                    break
                backtrack(i + 1, combination + [candidates[i]], target - candidates[i])
        
        backtrack(0, [], target)
        return result

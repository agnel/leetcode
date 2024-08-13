# 867. Transpose Matrix
# Ref: https://leetcode.com/problems/transpose-matrix/description/
# tags: bca, day-3, assignment
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]

        for j in range(n):
            for i in range(m):
                res[j][i] = matrix[i][j]

        return res

# 1582. Special Positions in a Binary Matrix
# Ref: https://leetcode.com/problems/special-positions-in-a-binary-matrix/
# tags: bca, day-3, assignment
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_counts = [0] * m
        col_counts = [0] * n
        indices_of_one = []
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
                    indices_of_one.append((i,j))

        for k, pair in enumerate(indices_of_one):
            if row_counts[pair[0]] == 1 and col_counts[pair[1]] == 1:
                res += 1

        return res

# 304. Range Sum Query 2D - Immutable
# Ref: https://leetcode.com/problems/range-sum-query-2d-immutable/description/
# tags: bca, day-3, assignment
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.p_sum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.p_sum[i][j] = matrix[i][j]

                if i > 0:
                    self.p_sum[i][j] += self.p_sum[i - 1][j]

                if j > 0:
                    self.p_sum[i][j] += self.p_sum[i][j - 1]

                if i > 0 and j > 0:
                    self.p_sum[i][j] -= self.p_sum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int): # -> int:
        sum = self.p_sum[row2][col2]
        if row1 > 0:
            sum -= self.p_sum[row1 -1][col2]
        if col1 > 0:
            sum -= self.p_sum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            sum += self.p_sum[row1 - 1][col1 - 1]

        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

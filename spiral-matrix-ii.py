# 59. Spiral Matrix II
# Ref: https://leetcode.com/problems/spiral-matrix-ii/description/
# tags: bca, day-2, assignment
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]  # result
        cnt = 1  # count
        for layer in range((n + 1) // 2):
            # direction 1
            # row is fixed i.e. layer
            # col moves from layer to n - layer - 1
            # in forward direction (increasing) i.e. left to right
            for pointer in range(layer, n - layer):
                res[layer][pointer] = cnt
                cnt += 1

            # direction 2
            # col is fixed i.e. n - layer - 1
            # row moves from layer + 1 to n - layer -1
            # in forward direction (increasing) i.e. top to bottom
            for pointer in range(layer + 1, n - layer):
                res[pointer][n - layer - 1] = cnt
                cnt += 1

            # direction 3
            # row is fixed i.e. n - layer - 1
            # col moves from n - layer - 2 to layer
            # in reverse direction (decreasing) i.e. right to left
            for pointer in range(n - layer - 2, layer - 1, -1):
                res[n - layer - 1][pointer] = cnt
                cnt += 1

            # direction 4
            # col is fixed i.e. layer
            # row moves from
            # in reverse direction (decreasing) i.e. bottom to top
            for pointer in range(n - layer - 2, layer, - 1):
                res[pointer][layer] = cnt
                cnt += 1

        return res
            

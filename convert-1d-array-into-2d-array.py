# 2022. Convert 1D Array Into 2D Array
# Ref: https://leetcode.com/problems/convert-1d-array-into-2d-array/
# tags: bca, day-3, assignment
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = len(original)
        if size != m * n:
            return []

        res = []

        for i in range(0, size, n):
            res.append(original[i:i + n])

        return res

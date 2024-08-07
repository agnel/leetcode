# 2022. Convert 1D Array Into 2D Array
# Ref: https://leetcode.com/problems/convert-1d-array-into-2d-array/
# tags: bca, day-3, assignment
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
    
        result = [[0] * n for _ in range(m)]
        
        for i in range(len(original)):
            # For  m=2,n=2
            # 
            # i      i/n         i%n        [ ][ ]
            # 
            # 0      0/2       0%2          [0][0]
            # 1      1/2       1%2          [0][1]
            # 2      2/2       2%2          [1][0]
            # 3      3/2       3%2          [1][1]
            result[i // n][i % n] = original[i]
        
        return result

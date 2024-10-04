# 74. Search a 2D Matrix
# Ref: https://leetcode.com/problems/search-a-2d-matrix/description/
# tags: bca, day-6, array, binary-search, matrix, search-a-2d-matrix-ii
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        l = 0
        r = rows * cols - 1
        
        while l <= r:
            mid = l + ((r - l) // 2)
            row = mid // cols
            col = mid % cols
            current = matrix[row][col]

            if current == target:
                return 1

            elif current < target:
                l =  mid + 1

            else:
                r = mid - 1
            
        return 0

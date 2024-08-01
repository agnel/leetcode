import sys

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max_X, min_Y = -sys.maxsize, sys.maxsize
        max_A, min_B = -sys.maxsize, sys.maxsize
        max_C, min_D = -sys.maxsize, sys.maxsize
        max_M, min_N = -sys.maxsize, sys.maxsize
        
        for i in range(len(arr1)):
            X = arr1[i] + arr2[i] + i
            A = arr1[i] - arr2[i] - i
            C = arr1[i] - arr2[i] + i
            M = arr1[i] + arr2[i] - i

            max_X = max(max_X, X)
            min_Y = min(min_Y, X)
            max_A = max(max_A, A)
            min_B = min(min_B, A)
            max_C = max(max_C, C)
            min_D = min(min_D, C)
            max_M = max(max_M, M)
            min_N = min(min_N, M)

        return max(max_X - min_Y, max_A - min_B, max_C - min_D, max_M - min_N)


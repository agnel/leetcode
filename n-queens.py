# 51. N-Queens
# Ref: https://leetcode.com/problems/n-queens/
# tags: bca, day-7, hard, array, backtracking, n-queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        def is_safe(board: List[List[str]], row: int, col: int):
            # check current column
            for r in range(row - 1, -1, -1):
                if board[r][col] == 'Q':
                    return False # i.e. False

            # check negative diagonal
            for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[r][c] == 'Q':
                    return False # i.e. False

            # check positive diagonal
            for r, c in zip(range(row, -1, -1), range(col, n)):
                if board[r][c] == 'Q':
                    return False # i.e. False

            # else return True
            return True

        def n_queens(board: List[List[str]], row: int) -> List[List[str]]:
            if row == n:
                solutions.append(["".join(i) for i in board])
                return

            for c in range(n):
                if is_safe(board, row, c):
                    board[row][c] = 'Q'
                    n_queens(board, row + 1)
                    board[row][c] = '.'

        board = [["."] * n for _ in range(n)]
        n_queens(board, 0)
        return solutions

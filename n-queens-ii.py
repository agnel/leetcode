# 52. N-Queens II
# Ref: https://leetcode.com/problems/n-queens-ii
# Solution Ref: https://leetcode.com/problems/n-queens/solutions/3520928/python3-easy-backtracking-with-1-hash
# tags: bca, day-7, similar-questions, hard, backtracking, n-queens, n-queens-ii
class Solution:
    def totalNQueens(self, n: int) -> int:

        positioned_queens = set()

        def backtrack_nqueen(row=0, count=0):
            for col in range(n):
                current_position = set([f'col_{col}', f'd1_{row + col}', f'd2_{row - col}'])
                # iterate through columns at the curent row.
                if not positioned_queens & current_position:
                    # explore this partial candidate solution, and mark the attacking zone
                    positioned_queens.update(current_position)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack_nqueen(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    positioned_queens.difference_update(current_position)
            return count

        return backtrack_nqueen(0, 0)

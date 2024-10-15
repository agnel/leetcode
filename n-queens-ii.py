# 52. N-Queens II
# Ref: https://leetcode.com/problems/n-queens-ii
# Solution Ref: https://leetcode.com/problems/n-queens/solutions/3520928/python3-easy-backtracking-with-1-hash
# tags: bca, day-7, similar-questions, hard, backtracking, n-queens, n-queens-ii
class Solution:
    def totalNQueens(self, n: int) -> int:

        positioned_queens = set()

        # similar to is_safe in nQueens
        def is_not_under_attack(r, c):
            # positive diagonal / hill has constant values
            # of `r + c` for any r and c on that diagonal
            # similar goes for negative diagonal / dale
            # that has constant values of `r - c` for
            # any r and c on that diagonal
            return not (positioned_queens & set([f'col_{c}', f'd1_{r + c}', f'd2_{r - c}']))

        def place_queen(r, c):
            positioned_queens.update(set([f'col_{c}', f'd1_{r + c}', f'd2_{r - c}']))

        def remove_queen(r, c):
            positioned_queens.difference_update(set([f'col_{c}', f'd1_{r + c}', f'd2_{r - c}']))

        def backtrack_nqueen(row=0, count=0):
            for col in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    place_queen(row, col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack_nqueen(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
            return count

        return backtrack_nqueen(0, 0)

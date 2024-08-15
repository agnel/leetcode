# 470. Implement Rand10() Using Rand7()
# Ref: https://leetcode.com/problems/implement-rand10-using-rand7/
# tags: bca, day-4, assignment

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()
        val = (a - 1) * 7 + b
        if val > 40: return self.rand10()
        return val % 10 + 1

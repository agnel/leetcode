# 172. Factorial Trailing Zeroes.
# Ref: https://leetcode.com/problems/factorial-trailing-zeroes/
# tags: bca, day-4, assignment

# Let's analyze the time and space complexity of the given Python code for the problem "172. Factorial Trailing Zeroes."

# ### Code Overview:
# The function calculates the number of trailing zeroes in the factorial of a given integer `n`. Trailing zeroes in a factorial are produced by the factors of 10, and each 10 is a product of 2 and 5. Since there are usually more factors of 2 than 5 in a factorial, the number of trailing zeroes is determined by the number of times 5 is a factor in the numbers from 1 to `n`.

# ### Time Complexity:
# - The code repeatedly divides `n` by 5 and accumulates the quotient in `c`.
# - The number of times the loop runs is determined by how many times `n` can be divided by 5 before it becomes 0.
# - For an integer `n`, the number of times it can be divided by 5 before it becomes 0 is \(O(\log_5 n)\).

# Thus, the **time complexity** is \(O(\log_5 n)\), which simplifies to \(O(\log n)\).

# ### Space Complexity:
# - The space used by the algorithm is constant, as it only uses a few integer variables (`c` and `n`).
# - No additional space that scales with the size of `n` is used.

# Thus, the **space complexity** is \(O(1)\).

# ### Summary:
# - **Time Complexity**: \(O(\log n)\)
# - **Space Complexity**: \(O(1)\)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        while n > 0:
            n //= 5
            c += n
        return c

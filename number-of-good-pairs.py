# 1512. Number of Good Pairs
# Ref: https://leetcode.com/problems/number-of-good-pairs/
# tags: bca, day-4, assignment

# Let's break down the formula for calculating the number of "good pairs" in an array, where a pair \((i, j)\) is considered "good" if \(nums[i] = nums[j]\) and \(i < j\).

# ### Understanding Good Pairs

# When you're counting "good pairs," you're essentially counting all possible pairs of indices \((i, j)\) where the element at index \(i\) is the same as the element at index \(j\), and \(i < j\).

# ### Example:
# Let's say you have the following array:

# \[ \text{nums} = [1, 2, 3, 1, 1, 3] \]

# Here, the "good pairs" are:
# - \((0, 3)\) because \(nums[0] = nums[3] = 1\)
# - \((0, 4)\) because \(nums[0] = nums[4] = 1\)
# - \((3, 4)\) because \(nums[3] = nums[4] = 1\)
# - \((2, 5)\) because \(nums[2] = nums[5] = 3\)

# So, there are 4 good pairs in this array.

# ### Deriving the Formula:
# If a number appears \(n\) times in the array, then we need to calculate how many pairs \((i, j)\) can be formed where \(i < j\) and \(nums[i] = nums[j]\).

# For any given number that appears \(n\) times:
# - The first occurrence can pair with \(n-1\) elements.
# - The second occurrence can pair with \(n-2\) elements.
# - The third occurrence can pair with \(n-3\) elements, and so on.

# The total number of pairs can be computed using the combination formula \(C(n, 2)\), which counts the number of ways to choose 2 items out of \(n\).

# \[ C(n, 2) = \frac{n \times (n-1)}{2} \]

# ### Why This Formula Works:
# - **\(n \times (n-1)\)**: This is the product of the number of possible pairs. Each of the \(n\) items can pair with \(n-1\) other items.
# - **Dividing by 2**: Since pairs \((i, j)\) and \((j, i)\) are the same in this context, we divide by 2 to avoid counting each pair twice.

# ### Applying the Formula:
# If a number appears:
# - 2 times: \(C(2, 2) = \frac{2 \times 1}{2} = 1\) pair
# - 3 times: \(C(3, 2) = \frac{3 \times 2}{2} = 3\) pairs
# - 4 times: \(C(4, 2) = \frac{4 \times 3}{2} = 6\) pairs
# - And so on.

# ### Summary:
# If a number appears \(n\) times in the array, the number of good pairs that can be formed with this number is given by:

# \[ \text{Number of good pairs} = \frac{n \times (n-1)}{2} \]

# This formula efficiently calculates the number of ways to select pairs where both elements are the same, which directly applies to counting "good pairs" in the context of this problem.

from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[x] += 1
        
        for value in cnt.values():
            ans += value * (value - 1) // 2
        
        return ans

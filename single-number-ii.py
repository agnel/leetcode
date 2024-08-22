# 137. Single Number II
# Ref: https://leetcode.com/problems/single-number-ii/
# Solution Ref: https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly
# tags: bca, day-5, assignment, bit manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        size = 32
        ans = 0
        for i in range(size):
            total = 0
            for n in nums:
                # Convert the number to two's complement representation to handle large test case
                if n < 0:
                    n = n & (2**32-1)
                total += (n >> i) & 1
            total %= 3
            
            ans |= total << i 
        
        # Convert the result back to two's complement representation if it's negative to handle large test case
        if ans >= 2**31:
            ans -= 2**32
        
        return ans

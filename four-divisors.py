# 1390. Four Divisors
# Ref: https://leetcode.com/problems/four-divisors/description/
# tags: bca, day-4, assignment
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        for n in nums:
            divisors = set()
            i = 1
            while i * i <= n:
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                
                if len(divisors) > 4:
                    break
                
                i += 1

            if len(divisors) == 4:
                total_sum += sum(divisors)
            
        return total_sum

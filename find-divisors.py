# find all divisors of a number
# tags: bca, home-work
class Solution:
    def findDivisors(n: int):
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                if n // i == i:
                    divisors.append(i)
                else:
                    divisors.append(i)
                    divisors.append(n // i)
            i += 1
        return divisors

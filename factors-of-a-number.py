# tags: practice, math, factors
# T: O(root(n))
# S: O(n/2) = O(n)
from typing import List

class Solution:
    def factors(self, n: int) -> List[int]:
        res = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                res.append(i)
            i += 1
        return res

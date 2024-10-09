# 875. Koko Eating Bananas
# Ref: https://leetcode.com/problems/koko-eating-bananas/
# Solution Ref: https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems
# tags: bca, IL, day-6, medium, koko-eating-bananas, array, binary-search,
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def feasible(speed):
            return sum([ceil(pile / speed) for pile in piles]) <= h

        while l < r:
            m = l + (r - l) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1

        return l

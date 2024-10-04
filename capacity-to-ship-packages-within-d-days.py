# 1011. Capacity To Ship Packages Within D Days
# Ref: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# Solution Ref: https://www.youtube.com/watch?v=4lK5pdSXhCk
# tags: bca, day-6, array, binary-search, medium, capacity-to-ship-packages-within-d-days
# comments:
# best explanation
# also explains why l < r intead of l <= r
# and why r = mid instead of r = mid - 1
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        # watch solution video to understand 
        # why l < r instead of l <= r
        while l < r:
            mid = l + (r - l) // 2

            if self.can_ship(mid, weights, days):
                r = mid
            else:
                l = mid + 1

        return r

    def can_ship(self, candidate: int, weights: List[int], days: int) -> bool:
        current_weight = 0
        days_taken = 1

        for weight in weights:
            current_weight += weight

            if current_weight > candidate:
                current_weight = weight
                days_taken += 1
            
        return days_taken <= days

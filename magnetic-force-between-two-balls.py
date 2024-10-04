# 1552. Magnetic Force Between Two Balls
# Ref: https://leetcode.com/problems/magnetic-force-between-two-balls/
# Editorial: https://leetcode.com/problems/magnetic-force-between-two-balls/editorial
# Solution template: https://leetcode.com/discuss/study-guide/3444552/binary-search-on-answer-template-generic-template
# tags: bca, day-6, array, binary-search, sorting, binary-search-on-answer, magnetic-force-between-two-balls, aggressive-cows

# Comments:
# wonderful explanation in the editorial
# refer solution template for other binary search problems

# Must do to master the binary search on answer:
# https://leetcode.com/problems/minimum-time-to-repair-cars/ <-- this one is gold!!!
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# https://leetcode.com/problems/koko-eating-bananas/
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
# https://leetcode.com/problems/divide-chocolate/ <-- this one is gold!!! (hard)

import math

class Solution:
    def canPlaceBalls(self, x: int, position: List[int], m: int) -> bool:
        last_placed_ball_position = position[0]
        balls_placed = 1

        for i in range(1, len(position)):
            if last_placed_ball_position + x <= position[i]:
                last_placed_ball_position = position[i]
                balls_placed += 1
            
            if balls_placed == m:
                return 1
        
        return 0

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # The left boundary l starts from 1 because the minimum distance must be positive.
        # And, we subtract 1.0 from m, because the number of gaps between n balls will be n-1
        # Note: The calculation position[-1] // (m - 1) gives you a rough idea of how far apart the balls can be placed. However, since integer division can lead to truncation, using math.ceil ensures that you consider all potential placements, especially when the positions don’t divide evenly.
        l, r = 1, math.ceil(position[-1] // (m - 1))
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2

            if self.canPlaceBalls(mid, position, m):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
            
        return ans

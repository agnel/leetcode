# 769. Max Chunks To Make Sorted
# Ref: https://leetcode.com/problems/max-chunks-to-make-sorted/description/
# tags: bca, day-3, assignment
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)

        ans = 0  # no. of chunks
        m = -1  # maximum value

        for i in range(n):
            m = max(m, arr[i])
            if m == i:
                ans += 1  # increment count
                m = -1  # reset maximum

        return ans

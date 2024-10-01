# 162. Find Peak Element
# Ref: https://leetcode.com/problems/find-peak-element/description/
# Solution: https://youtu.be/VFC1oxkn5-E, more: https://youtube.com/playlistlist=PLICVjZ3X1AcYYdde4GTp79zfdp_VACSkX
# Solution Ref: https://leetcode.com/problems/find-peak-element/solutions/1290642/intuition-behind-conditions-complete-explanation-diagram-binary-search/comments/1978758
# tags: bca, day-6, searching, array, binary-search, medium, peak-element
class Peak:
    def __init__(self, arr):
        self.arr = arr
        
    def peak(self):
        arr = self.arr
        l = 0
        r = len(arr) - 1
        
        while l < r:
            m = l + ((r - l) // 2)
            if arr[m] > arr[m + 1]:
                r = m
            else:
                l = m + 1
        
        return l

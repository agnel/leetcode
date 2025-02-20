# 729. My Calendar I
# Ref: https://leetcode.com/problems/my-calendar-i/description/
# Solution Ref: AM
# tags: am, speedrun, binary-search, medium, array, ordered-set
# comments:
# two things are important - the feasible condition for the binary search
# and the conditions to check if the entry can be made?
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        left = 0
        right = len(self.calendar) - 1
        idx = len(self.calendar)

        while left <= right:
            mid = left + (right - left) // 2
            if self.calendar[mid][0] > startTime:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        
        # supposedly we found the index at which to insert the entry i.e. idx
        # if the index idx is not the first position in list i.e. 0 AND
        # if the previous entry's endTime > the startTime of the entry we want to make,
        # then there is an overlap, so we reject the entry
        # if the entry is not to be put after the last entry of the list i.e.
        # the idx < len(self.calendar) [meaning the entry will be in the list somewhere] AND if the entry at index idx has startTime < endTime of the entry we wan to make, then there is an overlap, so we reject the entry. 
        if (idx > 0 and self.calendar[idx - 1][1] > startTime) or (idx < len(self.calendar) and self.calendar[idx][0] < endTime):
            return False
        
        self.calendar.insert(idx, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

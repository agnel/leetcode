# 1185. Day of the Week
# Ref: https://leetcode.com/problems/day-of-the-week/description/
# tags: bca, day-4, assignment, math

# we follow the tomohiko sakamoto's algorithm for this
# Ref: https://medium.com/@sunil01966/tomohiko-sakamotos-algorithm-finding-the-day-of-the-week-e168d34d8402
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

        # an array with leading number of days for each month
        # For JAN- 0 ;
        # For FEB- (31 days of jan ) %7 = 3;
        # For MARCH- (0+31+28) % 7 = 3 and so on..
        # leading_no_of_days = (0,3,3,6,1,4,6,2,5,0,3,5)
        #
        # For January and February if we calculate day then
        # there will be no change if that year is leap year or not.
        # Now in future we are going to do add 1 day extra
        # to every leap year. When that will happen January
        # and February will get affected. Because they require
        # no addition. Addition will be from march onwards.
        #
        # A leap year definition is:
        # If year is divisible by 400 its leap year OR
        # its divisible by 4 but not by 100.
        # 
        # Now y/400 will surely give those days added at
        # every 400th cycle, For example, At 400th AD 1 extra day
        # i.e 400/400=1, at 800th AD — : 800/400 = 2 extra days,
        # Which in total let’s say For 800th AD -: 800+(800/400)
        # which is 800 years and 2 days.
        #
        # Now Every 4th year, A leap year comes too.
        # So for 800 AD -: 800+ (800/400) +(800/4) =
        # 800+2+200=800 years + 202 days. But when leap year
        # comes at every 4th year, At its 25th cycle
        # i.e At 100th year, It takes a break. So it does not
        # come that year. So we simply remove from 202 extra days
        # all the time when 100 years has completed which is — :
        #
        # 800+(800/400)+(800/4)-(800/100) = 800+2+200–8 = 800 years and 194 days.
        # 
        # You are adding 1 extra day for all leap year
        # till that year, irrespective of even if that year
        # is a leap year or not, If that year got any
        # single leap year before it , a day is added.
        # 
        # Now let’s suppose it’s a normal year, Not a leap year,
        # and You just added 1 extra day because 1 leap year
        # was before it. Now You gotta compensate that extra day
        # because it is going to affect some months.
        # Either you don’t add or before you add take 1 out from them.
        # Last 3rd is 6 because -1 is nothing in week days. Saturday basically.
        leading_no_of_days = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)

        if month < 3:
            year -= 1
        
        return days_of_the_week[(year + year//4 - year//100 + year//400 + leading_no_of_days[month - 1] + day) % 7]

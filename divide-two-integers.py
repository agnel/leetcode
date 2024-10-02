# 29. Divide Two Integers
# Ref: https://leetcode.com/problems/divide-two-integers/
# best explanation:
# Solution Ref: https://leetcode.com/problems/divide-two-integers/solutions/1516367/complete-thinking-process-intuitive-explanation-all-rules-followed-c-code
# nice technique to find sign:
# Solution Ref: https://leetcode.com/problems/divide-two-integers/solutions/5768210/c-runtime-beats-96-83-memory-beats-92-06-explained
# tags: bca, day-6, math, bit-manipulation, medium, divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1

        # determine the sign of the quotient
        # false if both same
        # true if different
        is_negative = (dividend < 0) ^ (divisor < 0)

        # work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0

        # find the highest power of two that fits into the dividend
        while dividend >= divisor:
            q = 0

            while dividend > (divisor << (q + 1)):
                q += 1
            
            # add the power of 2 we found, to the answer
            ans += (1 << q)

            # subtract dividend by (divisor * power of 2 we found)
            dividend -= (divisor << q)

        # max positive int value is 2^31 - 1
        # whereas min negative int value is -2^31
        # since our count can go to a value of 2^31
        # so we check for it and also
        # for the sign of the required result
        # and return 2^31 - 1 accordingly
        # tip: 2^31 can be written using bitwise i.e. 1 << 31
        if ans == (1 << 31) and not is_negative:
            return (1 << 31) - 1
        
        # apply the sign to the quotient and return it
        return -ans if is_negative else ans 

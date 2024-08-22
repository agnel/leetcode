# 137. Single Number II
# Ref: https://leetcode.com/problems/single-number-ii/
# Solution Ref: https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly
# tags: bca, day-5, assignment, bit manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize two variables, ones and twos, 
        # to keep track of the count of each bit position.
        #
        # ones: Tracks the bits that have appeared once.
        # twos: Tracks the bits that have appeared twice.
        ones = 0
        twos = 0

        # Iterate through the array of numbers.
        # For each number `n` in the array:
        # Update ones and twos:

        # Let's analyze each step of the update process:
        # a. ones = (ones ^ n) & (~twos);:
        # ones ^ n XORs the current number `n` with the 
        # previous value of ones. This operation toggles 
        # the bits that have appeared an odd number of times, 
        # keeping the bits that have appeared twice unchanged.
        # (~twos) negates the bits in twos, effectively removing
        # the bits that have appeared twice from consideration.
        # The & operation ensures that only the bits that
        # have appeared once (after XOR) and not twice
        # (after negating twos) are retained.
        #
        # b. twos = (twos ^ n) & (~ones);:
        # twos ^ n XORs the current number n with
        # the previous value of twos. This operation
        # toggles the bits that have appeared
        # an even number of times, effectively removing
        # the bits that have appeared twice.
        # (~ones) negates the bits in ones, effectively
        # removing the bits that have appeared once from consideration.
        # The & operation ensures that only the bits
        # that have appeared twice (after XOR) and
        # not once (after negating ones) are retained.
        for n in nums:
            ones ^= n & ~twos
            twos ^= n & ~ones

        # After iterating through all the numbers,
        # the value stored in ones will represent
        # the single number that appears only once in the array.
        #
        # In summary, the algorithm uses bit manipulation to efficiently
        # keep track of the counts of each bit position.
        # By utilizing XOR and AND operations, it can identify
        # the bits of the single number that appears only once
        # in the array while ignoring the bits that appear multiple times.
        return ones

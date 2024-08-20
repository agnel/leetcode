# 1497. Check If Array Pairs Are Divisible by k
# Ref: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
# tags: bca, day-4, assignment

# Intuition
# The task is to determine whether we can pair 
# the elements of the array such that the sum
# of each pair is divisible by k. This requires
# us to ensure that for each possible remainder
# when an element is divided by k, there exists
# a complementary remainder such that their sum is k or 0.

from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # return false if arr length is odd
        size = len(arr)
        if size % 2 != 0:
            return 0  # 0 translates to False

        # Calculate Remainders: For each element in the array,
        # calculate the remainder when it is divided by k.
        # Use the formula ((x % k) + k) % k to ensure
        # non-negative remainders.
        freq = defaultdict(int)
        for x in arr:
            rem = ((x % k) + k) % k
            freq[rem] += 1 # increment the frequency for remainder `rem`

        # check pairs
        for r, f in freq.items(): # r is key i.e. remainder; f is value i.e. frequency
            # For remainder 0, ensure there are an even number of
            # such elements i.e. frequency f, as they can only pair among themselves.
            if r == 0 or r == (k - r):
                if f & 1:
                    return 0
            # For other remainders i, ensure that the number of elements with
            # remainder i is equal to the number of elements with remainder k-i.
            elif freq[r] != freq[k - r]:
                return 0
        
        return 1

# Explanation by ChatGPT:
# To solve the problem of checking whether an array can be divided into pairs such that the sum of each pair is divisible by a given integer \( k \), the solution utilizes the concept of remainders when elements are divided by \( k \). Here’s a step-by-step explanation of the solution and its time-space complexity:

# ### Explanation

# 1. **Edge Case Check**:
#    - First, the solution checks if the length of the array is even. If it's not, pairing elements to satisfy the condition is impossible, and it returns `False` (which is represented as `0` in the code).

# 2. **Calculate Remainders**:
#    - For each element in the array, compute the remainder when the element is divided by \( k \). To ensure non-negative remainders, the formula `((x % k) + k) % k` is used. This ensures that remainders are always between `0` and `k-1`.
#    - Use a frequency dictionary (`freq`) to count how many times each remainder appears in the array.

# 3. **Pairing Check**:
#    - For each remainder `r`:
#      - If `r` is `0` or `r` is equal to `k-r`:
#        - Remainders of `0` need to pair with themselves. Therefore, their count (`f`) should be even.
#        - Remainders of `r` where `r` is `k-r` should also pair with themselves. Thus, their count should be even.
#      - For other remainders `r`:
#        - Ensure that the number of elements with remainder `r` is equal to the number of elements with remainder `k-r`. This is because a remainder `r` needs to be paired with a remainder `k-r` to form a sum divisible by \( k \).

# 4. **Return Result**:
#    - If all checks pass, return `True` (represented as `1` in the code); otherwise, return `False` (represented as `0`).

# ### Time Complexity

# - **Computing Remainders**: This step involves iterating over the array once to calculate and store the remainders in the frequency dictionary. This operation is \( O(n) \), where \( n \) is the number of elements in the array.
# - **Checking Pairs**: After computing the frequencies, the solution iterates over the keys of the frequency dictionary. The number of unique remainders is at most \( k \), so this operation is \( O(k) \). Since \( k \) is usually much smaller than \( n \), this step is \( O(1) \) relative to the size of the array.

# Overall, the time complexity is dominated by the \( O(n) \) operation to compute remainders, making the total time complexity \( O(n) \).

# ### Space Complexity

# - **Frequency Dictionary**: The space used for storing the frequencies of remainders is proportional to the number of unique remainders, which is at most \( k \). Therefore, the space complexity for the dictionary is \( O(k) \). In practice, this is often much smaller compared to \( n \), so it can be considered \( O(1) \) in relative terms to the array size.

# - **Input Storage**: The space needed to store the input array itself is \( O(n) \), but this is not part of the additional space used by the algorithm.

# Thus, the overall space complexity is \( O(k) \), which is effectively \( O(1) \) for practical purposes since \( k \) is typically much smaller than \( n \).

# 125. Valid Palindrome
# Ref: https://leetcode.com/problems/valid-palindrome/description/
# Solution Ref: AM
# tags: string, two-pointers, easy, AM, valid-palindrome

class Solution:
    # In this approach, we are not using any extra space
    # TC: O(n)
    # SC: O(1)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

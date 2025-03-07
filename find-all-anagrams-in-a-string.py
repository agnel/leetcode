# 438. Find All Anagrams in a String
# Ref: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# Solution Ref: AM
# tags: medium, hash-table, string, sliding-window, find-all-anagrams-in-a-string, AM

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        input_str, window_str = s, p
        input_len, window_len = len(input_str), len(window_str)

        if input_len < window_len:
            return []
        
        input_counter = [0] * 26
        window_counter = [0] * 26

        a_ord = ord('a')
        res = []

        for i in range(window_len):
            input_counter[ord(input_str[i]) - a_ord] += 1
            window_counter[ord(window_str[i]) - a_ord] += 1
        
        if input_counter == window_counter:
            res.append(0)

        for right in range(window_len, input_len):
            input_counter[ord(input_str[right - window_len]) - a_ord] -= 1
            input_counter[ord(input_str[right]) - a_ord] += 1
            if input_counter == window_counter:
                res.append(right - window_len + 1)
        
        return res

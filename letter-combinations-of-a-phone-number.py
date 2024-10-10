# 17. Letter Combinations of a Phone Number
# Ref: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Solution Ref: https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/5890819/simple-solution-with-diagrams-in-video-javascript-c-java-python
# tags: bca, day-7, medium, hash-table, string, backtracking, letter-combinations-of-a-phone-number, letter-combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append(path)
                return
            
            letters = digits_map[digits[index]]

            for letter in letters:
                backtrack(index + 1, path + letter)
        
        combinations = []
        backtrack(0, '')

        return combinations

# 1672. Richest Customer Wealth
# Ref: https://leetcode.com/problems/richest-customer-wealth/description/
# tags: bca, day-3, assignment
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # richest amount
        r = 0
        
        for i in range(len(accounts)):
            r = max(r, sum(accounts[i]))

        return r
            

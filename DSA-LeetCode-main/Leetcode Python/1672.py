class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in accounts:
            wealth = max(wealth , sum(i))
        return wealth

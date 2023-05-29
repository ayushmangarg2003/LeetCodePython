class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            ans+=empty//numExchange
            empty = empty//numExchange + empty%numExchange
        return ans

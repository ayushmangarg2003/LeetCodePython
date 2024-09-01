class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        if costs[0] > coins:
            return 0
        for i in range(len(costs)):
            coins-= costs[i]
            if coins < 0:
                return i
        return len(costs)
            

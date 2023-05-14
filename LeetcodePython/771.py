class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sub = 0
        for i in stones:
            if i not in jewels:
                sub+=1
        return len(stones) - sub

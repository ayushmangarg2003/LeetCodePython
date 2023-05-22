class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0
        return math.floor(n**0.5)

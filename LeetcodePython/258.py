class Solution:
    def addDigits(self, n: int) -> int:
        while len(str(n))!=1:
            n = sum( int(i) for i in str(n))
        return n

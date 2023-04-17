class Solution:
    def pivotInteger(self, n: int) -> int:
        return isqrt(n*(n+1)//2) if n in {1, 8, 49, 288} else -1

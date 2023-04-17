class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0: return False
        factors = (2, 3, 5)
        while n != 1:
            for f in factors:
               if n % f == 0:
                   n = n // f
                   break
            else:
                return False
        return True

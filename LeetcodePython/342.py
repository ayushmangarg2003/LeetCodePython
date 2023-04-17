class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return 0
        i=0
        num=1
        while num<=n:
            if num == n:
                return True
            i+=1
            num = 4**i
        return False

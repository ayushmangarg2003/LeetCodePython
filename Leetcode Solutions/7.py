class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x = x*(-1)
            x = str(x)
            x = x[::-1]
            x = int(x)
            if -x < -1*(2**31 +1):
                return 0
            return -x
        x = str(x)
        x = x[::-1]
        x = int(x)
        if x > (2**31 - 1):
            return 0
        return x

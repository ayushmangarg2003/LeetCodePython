class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        temp = (n-1)*4
        ans = 1
        while temp > 0:
            ans+=temp
            temp-=4
        return ans

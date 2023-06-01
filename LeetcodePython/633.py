class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c))+1):
            temp=sqrt(c-i*i)
            if temp==int(temp): return True

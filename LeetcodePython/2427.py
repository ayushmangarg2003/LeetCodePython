class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        temp = 1
        while temp <= min(a,b):
            if a%temp==0 and b%temp==0:
                ans+=1
            temp+=1
        return ans

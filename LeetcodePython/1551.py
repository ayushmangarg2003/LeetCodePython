class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        if n%2 == 0:
            for i in range(n//2):
                ans+= (2*i )+1
        else:
            for i in range((n+1)//2):
                ans+= 2*i
        return ans

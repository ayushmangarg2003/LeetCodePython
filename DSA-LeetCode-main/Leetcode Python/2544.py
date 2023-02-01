class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        n = str(n)
        for i in range(len(n)):
            if i%2==0:
                ans+=int(n[i])
            else:
                ans-=int(n[i])
        return ans

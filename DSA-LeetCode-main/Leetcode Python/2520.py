class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        for val in str(num):
            if num%int(val) == 0:
                ans+=1
        return ans

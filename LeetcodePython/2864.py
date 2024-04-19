class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num = s.count("1")
        ans=''
        ans += '1'*(num-1)
        ans += '0'*(len(s)-num)
        ans += '1'
        return ans

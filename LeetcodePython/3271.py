class Solution:
    def stringHash(self, s: str, k: int) -> str:
        alp = 'abcdefghijklmnopqrstuvwxyz'
        ans = ""
        i = 0
        while i < len(s):
            temp = 0
            for j in range(i,i+k):
                temp+= ord(s[j])-ord('a')
            temp %= 26
            ans+=alp[temp]
            i+=k
        return ans

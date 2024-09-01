class Solution:
    def partitionString(self, s: str) -> int:
        i = 0
        ans = 1
        temp = []
        while i < len(s):
            if s[i] in temp:
                temp = []
                ans+=1
            temp.append(s[i])
            i+=1
        return ans

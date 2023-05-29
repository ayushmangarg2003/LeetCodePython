class Solution:
    def maxScore(self, s: str) -> int:
        temp = []
        for i in range(1,len(s)):
            temp.append(s[:i].count('0') + s[i:].count('1'))
        return max(temp)

class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        count = True
        for i in s:
            if i == '|':
                count = not count
            if count and i == '*':
                ans+=1
        return ans

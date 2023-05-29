class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        alldis = []
        for i in range(len(s)):
            if s[i]==c:
                alldis.append(i)
        ans = []
        for i,v in enumerate(s):
            mindis = float(inf)
            for j in alldis:
                mindis = min(mindis , abs(i-j))
            ans.append(mindis)
        return ans
                 

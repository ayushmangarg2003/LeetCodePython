class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True

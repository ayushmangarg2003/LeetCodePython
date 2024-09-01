class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        test=True
        while test:
            test=False
            i=s.find(part)
            if i!=-1:
                s=s[:i]+s[i+len(part):]
                test=True
        return s

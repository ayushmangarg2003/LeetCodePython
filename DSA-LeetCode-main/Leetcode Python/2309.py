class Solution:
    def greatestLetter(self, s: str) -> str:
        temp = []
        for i in s:
            if i.lower() in s and i.upper() in s:
                temp.append(ord(i.upper()))
        if len(temp) > 0:
            return chr(max(temp))
        return ""

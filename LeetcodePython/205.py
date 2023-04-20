class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp = {}
        for i in range(len(s)):
            if s[i] not in temp.keys():
                if t[i] not in temp.values():
                    temp[s[i]] = t[i]
                else:
                    return False
            if s[i] in temp.keys():
                if temp[s[i]] == t[i]:
                    continue
                return False
        return True

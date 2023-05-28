class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp = s.split(" ")
        if len(temp) != len(pattern):
            return False
        dict1 = {}
        dict2 = {}
        for k, v in zip(pattern,temp):
            if k in dict1:
                if dict1[k] != v:
                    return False
            else:
                dict1[k] = v
            
            if v in dict2:
                if dict2[v] != k:
                    return False
            else:
                dict2[v] = k
        return True

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for char in set(s): 
            i, j = s.find(char), s.rfind(char)  
            if j > i + 1:  
                res += len(set(s[i+1:j])) 
        return res

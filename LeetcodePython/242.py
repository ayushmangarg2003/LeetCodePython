class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) != Counter(t):
            return False
        return True

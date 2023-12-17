class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # The idea is that if a string s can be constructed by repeating a substring, then concatenating two copies of s together and removing the      first and last character would still contain s as a substring.
        return s in s[1:]+s[:-1]

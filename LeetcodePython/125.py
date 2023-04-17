class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            if i.isalnum():
                new+= i
        new = new.lower()
        return new == new[::-1]

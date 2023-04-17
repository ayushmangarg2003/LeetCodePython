class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return 1
        return 0

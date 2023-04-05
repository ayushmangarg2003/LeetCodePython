class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a = 0
        for i in columnTitle:
            a = a * 26 + ord(i) - ord('A') + 1
        return a

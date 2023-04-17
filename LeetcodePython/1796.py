class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        s = list(set(s))
        for letter in s:
            if letter.isdigit():
                digits.add(letter)
        digits = sorted(list(digits))
        return -1 if len(digits) < 2 else int(digits[-2])

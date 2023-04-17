class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return 1
        if word.isupper():
            return 1
        if word.islower():
            return 1
        if word[0].isupper() and word[1:len(word)].islower():
            return 1
        return 0

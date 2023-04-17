class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        dum1 = "".join(word1)
        dum2 = "".join(word2)
        return dum1 == dum2

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        temp1 = []
        temp2 = []
        for i in Counter(word1).values():
            temp1.append(i)
        for i in Counter(word2).values():
            temp2.append(i)
        if sorted(temp1) != sorted(temp2):
            return False
        for i in word1:
            if i not in word2:
                return False
        for i in word2:
            if i not in word1:
                return False
        return True

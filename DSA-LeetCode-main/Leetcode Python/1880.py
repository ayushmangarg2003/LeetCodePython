class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d = {}
        alp = "abcdefghij"
        j = 0
        for i in alp:
            if i not in d:
                d[i] = j
                j+=1
        x = ""
        for i in firstWord:
            x += str(d[i])
        y = ""
        for i in secondWord:
            y += str(d[i])
        z = ""
        for i in targetWord:
            z += str(d[i])
        return (int(x)+int(y))==int(z)

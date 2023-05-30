class Solution:
    def sortSentence(self, s: str) -> str:
        ans = s.split(" ")
        temp = []
        i = 1
        while i <= len(ans):
            for j in ans:
                if str(i) in j:
                    temp.append(j[:-1])
            i+=1
        return " ".join(temp)

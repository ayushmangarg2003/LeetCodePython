class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        alp = 'abcdefghijklmnopqrstuvwxyz'
        temp1 = []
        temp2 = []

        for i in range(len(s1)):
            temp1.append(alp.index(s1[i]))
            temp2.append(alp.index(s2[i]))

        temp1 = sorted(temp1)
        temp2 = sorted(temp2)

        for i in range(len(s1)):
            temp1[i] -= temp2[i]
        if min(temp1) >=0:
            return True
        if max(temp1) <= 0:
            return True
        return False

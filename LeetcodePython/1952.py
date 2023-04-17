class Solution:
    def isThree(self, n: int) -> bool:
        temp = 0
        for i in range(1, n+1):
            if n%i==0:
                temp+=1
        if temp == 3:
            return 1
        return 0

class Solution:
    def isFascinating(self, n: int) -> bool:
        temp=str(n)
        temp+=str(n*3)
        temp+=str(n*2)
        if "0" in temp or len(list(temp)) != 9:
            return False
        if len(set(list(temp))) == 9:
            return True
        return False

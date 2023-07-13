class Solution:
    def largestGoodInteger(self, num: str) -> str:
        temp = float(inf) * (-1)
        for i in range(len(num)-2):
            if num[i:i+3] == num[i]*3:
                temp = max(int(num[i:i+3]) , temp)
        if temp<0:
            return ""
        elif temp == 0:
            return "000"
        return str(temp)

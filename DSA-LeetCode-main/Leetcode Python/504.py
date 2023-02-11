class Solution:
    def convertToBase7(self, num: int) -> str:
        sign=""
        if num<0:
            sign+="-"
            num*=-1
        ans=""
        while(num>0):
            ans+=str(num%7)
            num=num//7
        ans=ans[::-1]
        if len(sign+ans)==0:
            return "0"
        return sign+ans

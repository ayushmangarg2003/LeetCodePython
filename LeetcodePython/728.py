class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isdiv(num):
            temp = True
            for i in str(num):
                if i == '0':
                    temp = False
                    break
                if num%int(i)!=0:
                    temp = False
            return temp
        ans = []
        for i in range(left,right+1):
            if isdiv(i):
                ans.append(i)
        return ans

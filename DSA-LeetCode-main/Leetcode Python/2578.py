class Solution:
    def splitNum(self, num: int) -> int:
        l=list(str(num))
        l.sort()
        even, odd= "", ""
        for i in range(0,len(l)):
            if i%2==0:
                even+= l[i]
            else:
                odd+= l[i]
        return int(even)+int(odd)

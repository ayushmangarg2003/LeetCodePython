class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k = k-1
        num = 0
        l = [i for i in range(1,n+1)]
        def find(k,num):
            if len(l) == 1:
                return l[0]
            num = (num + k)% len(l)
            del l[num]
            return find(k,num)
        return find(k,num)

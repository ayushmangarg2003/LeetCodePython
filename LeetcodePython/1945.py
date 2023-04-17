class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dum = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        sol = 0
        for i in s:
            ans += str(dum.index(i)+1)
        while k>0:
            sol = 0
            for j in ans:
                sol+=int(j)
            ans = str(sol)
            k-=1
        return sol

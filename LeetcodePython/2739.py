class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        d=0
        while mainTank>0:
            if mainTank>=5:
                mainTank-=5
                d+=5
                if additionalTank>=1:
                    additionalTank-=1
                    mainTank+=1
            if mainTank<5:
                d+=mainTank
                mainTank=0
        return d*10

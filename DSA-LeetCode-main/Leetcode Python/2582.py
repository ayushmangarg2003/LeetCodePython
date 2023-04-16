class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time > n:
            if (time//(n-1))%2==0:
                return (time-time//(n-1)*(n-1))+1
            return n-((time-time//(n-1)*(n-1))+1)+1
        if time < n:
            return time+1
        return time-1

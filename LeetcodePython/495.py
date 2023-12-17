class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1]-timeSeries[i] < duration:
                ans+=timeSeries[i+1]-timeSeries[i]
            else:
                ans+= duration
        return ans + duration

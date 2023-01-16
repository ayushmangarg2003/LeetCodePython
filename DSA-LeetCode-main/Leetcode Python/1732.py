class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = [0]
        count = 0
        for i in range(len(gain)):
            count+=gain[i]
            if count>0:
                maxAltitude.append(count)
        return max(maxAltitude)

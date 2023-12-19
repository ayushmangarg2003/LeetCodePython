class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        def calSum(arr):
            num = 0
            for i in range(len(arr)):
                 num+= (i+1) * arr[i]
            return num
        
        sat.sort()
        maxx = 0
        for i in range(len(sat)):
            maxx = max(maxx , calSum(sat[i:]))
        return maxx
        
        

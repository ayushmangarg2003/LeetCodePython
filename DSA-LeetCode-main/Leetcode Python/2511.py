class Solution: 
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        index = 0 
        for i, x in enumerate(forts): 
            if x: 
                if forts[index] == -x: ans = max(ans, i-index-1)
                index = i 
        return ans 

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res, arr = [], []
        for i in reversed(range(len(heights))):
            counter = 0        
            while arr and arr[-1] <= heights[i]:
                counter += 1
                arr.pop()
            if arr:
                counter += 1
            res.append(counter)
            arr.append(heights[i])
        return reversed(res)

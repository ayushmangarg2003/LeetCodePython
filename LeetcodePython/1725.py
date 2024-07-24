class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp = []
        for i in range(len(rectangles)):
            temp.append(min(rectangles[i]))
        val = 0
        key = 0
        for k,v in Counter(temp).items():
            if key <= k:
                key = k
                val = v
        return val

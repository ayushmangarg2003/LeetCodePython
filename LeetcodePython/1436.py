class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = []
        end = []
        for i in paths:
            start.append(i[0])
            end.append(i[-1])
        for j in end:
            if j not in start:
                return j

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        dummy = []
        for i in matrix:
            for j in i:
                dummy.append(j)
        dummy.sort()
        return dummy[k-1]

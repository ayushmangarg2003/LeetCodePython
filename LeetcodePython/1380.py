class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky = []
        minrow = []
        maxcol = []
        for i in range(len(matrix)):
            minrow.append(min(matrix[i]))
        for j in range(len(matrix[0])):
            temp = []
            for i in range(len(matrix)):
                temp.append(matrix[i][j])
            maxcol.append(max(temp))
        ans = []
        for i in maxcol:
            if i in minrow:
                ans.append(i)
        return ans

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        column = set()
        row = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    column.add(j)
                    row.add(i)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in range(len(matrix)):
            for j in column:
                matrix[i][j] = 0
         

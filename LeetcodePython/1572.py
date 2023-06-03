class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    ans += mat[i][j]
                if i+j+1 == len(mat):
                    ans += mat[i][j]
        if len(mat)%2==0:
            return ans
        minus = (len(mat)-1)//2
        ans-= mat[minus][minus]
        return ans
      

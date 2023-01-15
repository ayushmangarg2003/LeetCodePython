class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        temp = []
        for i in range(len(mat)):
            temp.append(max(mat[i])) 
        return [temp.index(max(temp)) , mat[temp.index(max(temp))].index(max(mat[temp.index(max(temp))]))]

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top , bot = 0 , len(matrix)-1
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
                
        if not (top<=bot):
            return 0
        row = (top+bot)//2
        lef , rig = 0 , len(matrix[0])-1
        while lef<=rig:
            mid = (lef+rig)//2
            if target > matrix[row][mid]:
                lef = mid+1
            elif target < matrix[row][mid]:
                rig = mid-1
            else:
                return 1
        return 0

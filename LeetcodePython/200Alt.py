class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length = len(grid)
        width = len(grid[0])
        def zero(i,j):
            if (i!=length and i!=-1 and j!=width and j!=-1 and grid[i][j]=="1"):
                grid[i][j] = '0'
                zero(i+1,j)
                zero(i-1,j)
                zero(i,j+1)
                zero(i,j-1)
            return
        ans = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == '1':
                    ans+=1
                    zero(i,j)
        return ans

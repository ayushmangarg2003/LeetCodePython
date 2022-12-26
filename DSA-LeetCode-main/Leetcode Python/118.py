class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        
        for r in range(2,numRows+1):
            temp = [1]
            for c in range(1,r-1):
                temp.append(output[-1][c] + output[-1][c-1])
            temp.append(1)
            output.append(temp)
        return output

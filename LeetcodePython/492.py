class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = []
        for i in range(1,int(area**(0.5))+1):
            if area%i==0:
                ans.append([i,area//i])
        return ans[-1][::-1]

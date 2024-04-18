class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        temp = []
        for i in points:
            temp.append(i[0])
        temp.sort()
        ans = 0
        for i in range(len(temp)-1):
            ans= max(ans, temp[i+1]-temp[i])
        return ans

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for i,j in Counter(arr).items():
            if i == j:
                ans=max(ans ,j)
        return ans

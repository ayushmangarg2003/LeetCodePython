class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        for i in range(0, target[-1]):
            if i+1 in target:
                ans.append('Push')
            else:
                ans.append('Push')
                ans.append('Pop')
        return ans

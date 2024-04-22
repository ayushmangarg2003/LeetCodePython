class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        min = 0
        max = len(s)
        for i in s:
            if i == 'I':
                ans.append(min)
                min+=1
            elif i == 'D':
                ans.append(max)
                max-=1
        if s[-1] == 'D':
            ans.append(max)
        if s[-1] == 'I':
            ans.append(min)
        return ans

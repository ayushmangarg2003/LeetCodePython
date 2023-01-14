class Solution:
    def removeStars(self, s: str) -> str:
        temp = []
        ans =''
        for i in s:
            if i == '*':
                temp.pop()
            else:
                temp.append(i)

        for k in temp:
            ans+=k
        return ans

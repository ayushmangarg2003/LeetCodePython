class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans = []
        for i in s:
            if i not in ans:
                ans.append(i)
            else:
                return i

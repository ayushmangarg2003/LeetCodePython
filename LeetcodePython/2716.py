class Solution:
    def minimizedStringLength(self, s: str) -> int:
        temp = []
        for i in s:
            if i not in temp:
                temp.append(i)
        return len(temp)

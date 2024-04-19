class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        # return ((ord(s[3])-ord(s[0])+1) * (int(s[1]) - int(s[4]) + 1))
        letters = []
        numbers = []
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if ord(s[0]) <= ord(i) <= ord(s[3]):
                letters.append(i)
        for i in range(int(s[1]), int(s[4])+1):
            numbers.append(i)
        ans = []
        for i in letters:
            temp = i
            for j in numbers:
                ans.append(temp + str(j))
        return ans
        

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0] * (len(s)+1)
        for start, end, dir in shifts:
            temp[start] += (2*dir) - 1
            temp[end+1] -= (2*dir) - 1
        shared = 0
        s = list(s)
        for i in range(len(s)):
            shared += temp[i]
            s[i] = chr(((ord(s[i]) - 97 + shared) % 26) + 97) 
        return "".join(s)

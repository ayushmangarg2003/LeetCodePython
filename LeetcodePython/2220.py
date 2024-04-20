class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        st = str(bin(start).replace("0b", ""))
        end = str(bin(goal).replace("0b", ""))
        if len(st) < len(end):
            st = "0"*(len(end)-len(st)) + st
        if len(end) < len(st):
            end = "0"*(len(st)-len(end)) + end
        ans = 0
        for i in range(min(len(end), len(st))):
            if st[i] != end[i]:
                ans+=1
        return ans

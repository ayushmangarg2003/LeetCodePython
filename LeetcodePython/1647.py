class Solution:
    def minDeletions(self, s: str) -> int:
        temp = []
        for i in Counter(s).values():
            temp.append(i)
        if len(temp) == len(set(temp)):
            return 0
        ans = 0
        while len(temp) != len(set(temp)):
            for i in range(len(temp)):
                if temp[i] in temp[:i] + temp[i+1:]:
                    temp[i]-=1
                    if temp[i] == 0:
                        temp.remove(temp[i])
                        temp.append(max(temp)+2)
                    ans+=1
        return ans
        

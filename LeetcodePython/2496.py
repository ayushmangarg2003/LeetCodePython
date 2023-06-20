class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxx = 0
        for i in strs:
            if i.isnumeric():
                maxx=max(maxx,int(i))
            elif i.isalnum():
                maxx=max(maxx , len(i))
        return maxx
        

class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s)-1
        temp = 'AEIOUaeiou'
        templist = list(s)

        while start < end:
            while start < end and s[start] not in temp:
                start+=1
            while start < end and s[end] not in temp:
                end-=1
            templist[start], templist[end] = templist[end], templist[start]
            start+=1
            end-=1
        s = "". join(templist)
        return s

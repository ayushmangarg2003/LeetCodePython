class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i] == words[j][::-1]:
                    ans+=1
        return ans

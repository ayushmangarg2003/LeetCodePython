class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        def check(a,b):
            if b.find(a) == 0 and b.rfind(a) == (len(b) - len(a)):
                return True
            return False


        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if check(words[i], words[j]):
                    ans+=1
        return ans

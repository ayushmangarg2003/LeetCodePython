class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for i in words:
            if i.find(pref) == 0:
                ans+=1
        return ans

class Solution:
    from collections import Counter
    def longestPalindrome(self, s: str) -> int:
        ans = len(s)+1
        for k,v in Counter(s).items():
            if v%2 != 0:
                ans-=1
        return min(ans,len(s))

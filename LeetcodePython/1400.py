class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        odd_count = 0
        for key,v in Counter(s).items():
            if v%2 == 1:
                odd_count+=1
        return odd_count <= k

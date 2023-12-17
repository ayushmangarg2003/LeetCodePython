class Solution:
    from collections import Counter

    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = Counter(str(bin(i)))
            ans.append(count['1'])
        return ans

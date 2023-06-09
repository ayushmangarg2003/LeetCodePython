class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        l = []
        rem = 0
        for i in word:
            rem = (rem * 10 +int(i))%m 
            if rem%m==0:
                l.append(1)
            else:
                l.append(0)
        return l

class Solution:
    def twoEggDrop(self, n: int) -> int:
        i = 1
        while i < n:
            n-=i
            i+=1
        return i

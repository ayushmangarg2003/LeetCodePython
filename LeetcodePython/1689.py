class Solution:
    def minPartitions(self, n: str) -> int:
        x=0
        for i in n:
            x = max(x , int(i))
        return x

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        dummy = [n for n in range(1,2001)]
        for i in arr:
            dummy.remove(i)
        return dummy[k-1]

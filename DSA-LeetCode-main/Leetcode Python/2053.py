class Solution:
    def kthDistinct(self, arr: List[str], k1: int) -> str:
        dummy = []
        for k,v in Counter(arr).items():
            if v==1:
                dummy.append(k)
        if int(len(dummy)) < k1:
            return ""
        return dummy[k1-1]

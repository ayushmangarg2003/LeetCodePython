class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k>0:
            i = gifts.index(max(gifts))
            gifts[i] = math.floor(gifts[i]**(1/2))
            k-=1
        return sum(gifts)

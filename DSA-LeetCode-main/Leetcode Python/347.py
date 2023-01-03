class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c=[x[0] for x in list(Counter(nums).most_common(k))]
        return c

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        words = sorted(words)
        c = Counter(words)
        c2 = [k for k,v in sorted(c.items() , key= lambda item:item[1], reverse=True)]
        return c2[:k]

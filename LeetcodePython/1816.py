class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        dummy = s.split()
        return " ".join(dummy[:k])

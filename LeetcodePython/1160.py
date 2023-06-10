class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(i) if collections.Counter(i) <= collections.Counter(chars) else 0 for i in words)

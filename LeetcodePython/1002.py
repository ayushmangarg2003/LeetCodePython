class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        for word in words:
            counter &= Counter(word)
        return list(counter.elements())

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_chars = sorted(freq, key=freq.get, reverse=True)
        sorted_string = ''.join([char*freq[char] for char in sorted_chars])
        return sorted_string

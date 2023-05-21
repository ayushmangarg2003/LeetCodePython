class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        frequency = {}
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            frequency[sub] = frequency.get(sub, 0) + 1
        return [sub for sub in frequency if frequency[sub] > 1]

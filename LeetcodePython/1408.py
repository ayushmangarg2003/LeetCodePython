class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = ' '.join(words)
        subStr = [i for i in words if arr.count(i) >= 2]
        return subStr

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        val = count.values()
        if len(val) == len(set(val)):
            return True
        return False

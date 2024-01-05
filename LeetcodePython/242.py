class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) != Counter(t):
            return False
        return True


# Alternate Solution
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

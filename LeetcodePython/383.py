class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine or ransomNote.count(i)>magazine.count(i):
                return False
        else:
            return True

class Solution:
    def checkIfPangram(self, s: str) -> bool:
        temp = [*s]
        if len(set(temp)) == 26:
            return True
        return False

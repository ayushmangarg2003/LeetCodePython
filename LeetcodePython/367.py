class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if math.floor(num**0.5)==num**0.5:
            return True
        return False

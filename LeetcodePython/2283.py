class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if str(num.count(str(i))) != num[i]:
                return False
        return True

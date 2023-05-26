
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if 0 in arr:
            arr.remove(0)
        for i in arr:
            if i*2 in arr:
                return True
        return False

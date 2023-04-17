class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        temp = 0
        for i in nums:
            if i<0:
                temp+=1
        if temp%2 != 0:
            return -1
        return 1

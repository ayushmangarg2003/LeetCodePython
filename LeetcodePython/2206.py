class Solution:
    def divideArray(self, nums: List[int]) -> bool: 
        for i, j in Counter(nums).items():
            if j%2 != 0:
                return 0
        return 1

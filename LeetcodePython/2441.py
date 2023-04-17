class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for i in sorted(nums, reverse=True):
            if i*(-1) in nums:
                return i
        return -1
                

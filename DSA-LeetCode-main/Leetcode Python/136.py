class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x0 = 0
        for i in range(len(nums)):
            x0 = x0^nums[i]
        return x0

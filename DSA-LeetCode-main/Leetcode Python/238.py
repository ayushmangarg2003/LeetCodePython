class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1] * (len(nums))
        product = 1
        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]
        product2 = 1
        for i in range(len(nums) -1 , -1 , -1):
            res[i]*=product2
            product2 *= nums[i]
        return res

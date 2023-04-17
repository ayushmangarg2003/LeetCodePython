class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        n = len(nums)/2
        num = nums[0]
        
        for i in range(len(nums)):
            if num == nums[i]:
                count+=1
            else:
                count =1
            if count>n:
                return num
            num = nums[i]

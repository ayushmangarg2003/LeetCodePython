class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = 0
        for i in range(len(nums)):
            a = a + nums[i]
            nums[i]=a
        return nums

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        for i in nums:
            if i == 0:
                nums.append(0)
                nums.remove(i)
        return nums

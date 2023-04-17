class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]==0:
            nums = set(nums)
            return len(nums)-1
        nums = set(nums)
        return len(nums)

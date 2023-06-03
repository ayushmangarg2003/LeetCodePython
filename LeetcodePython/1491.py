class Solution:
    def average(self, nums: List[int]) -> float:
        nums.remove(max(nums))
        nums.remove(min(nums))
        return sum(nums)/len(nums)

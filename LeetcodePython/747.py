class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        dummy = sorted(nums)
        if dummy[-1] >= dummy[-2]*2:
            return nums.index(dummy[-1])
        return -1

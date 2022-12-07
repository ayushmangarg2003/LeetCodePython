class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = -1
        if target in nums:
            i = nums.index(target)
            nums = nums[::-1]
            j = len(nums)-nums.index(target)-1
            return [i,j]
        return [-1,-1]

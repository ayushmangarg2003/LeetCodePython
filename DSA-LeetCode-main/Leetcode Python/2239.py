class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dummy = []
        nums.sort()
        for i in nums:
            dummy.append(abs(0-i))
        dummy = dummy[::-1]
        nums = nums[::-1]
        return nums[dummy.index(min(dummy))]

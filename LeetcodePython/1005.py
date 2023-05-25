class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k > 0:
            nums[nums.index(min(nums))] *= (-1)
            k-=1
        return sum(nums)

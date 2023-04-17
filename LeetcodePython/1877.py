class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summ = []
        n = len(nums)
        for i in range(n//2):
            summ.append(nums[i]+nums[n-i-1])
        return max(summ)

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0
        while k>0:
            ans+= max(nums)
            nums[nums.index(max(nums))] += 1
            k-=1
        return ans

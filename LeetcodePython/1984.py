class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        ans = float(inf)
        nums.sort(reverse=True)
        for i in range(len(nums)-k+1):
            ans = min(ans , max(nums[i:i+k]) - min(nums[i:i+k]))
        return ans

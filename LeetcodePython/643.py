class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        ans = s
        for i in range(len(nums)-k):
            s = s + nums[i+k] - nums[i]
            ans = max(ans , s)
        return ans/k

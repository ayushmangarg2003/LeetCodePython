class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float("inf")
        for i, n in enumerate(nums):
            if n == target:
                res = min(res, abs(i-start))
        return res

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for k,v in enumerate(nums):
            diff = target - v
            if diff in prev:
                return [prev[diff],k]
            prev[v]=k

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in nums:
            return 1
        return 0

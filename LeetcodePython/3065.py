class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        while nums[i] < k:
            i+=1
        return i

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dummy = []
        for i in range(len(nums)):
            if nums[i] == 1:
                dummy.append(i)
        for i in range(len(dummy)-1):
            if dummy[i+1] - dummy[i] <= k:
                return False
        return True

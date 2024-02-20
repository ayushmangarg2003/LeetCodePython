class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in nums:
                length = 0
                while i+length in nums:
                    length+=1
                ans = max(ans, length)
        return ans

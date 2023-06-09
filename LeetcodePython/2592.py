class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        i,j = 0,0
        while i < len(nums):
            if nums[j] < nums[i]:
                ans+=1 
                j+=1
            i+=1
        return ans

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        temp = 0
        ans = 0
        for i in range(len(nums)):
            temp+=nums[i]
            if temp == 0:
                ans+=1
        return ans

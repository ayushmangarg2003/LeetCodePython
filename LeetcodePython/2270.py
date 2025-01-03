class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        summ = sum(nums)/2
        prefixsum = 0        
        ans = 0
        for i in range(len(nums)-1):
            prefixsum += nums[i] 
            if prefixsum >= summ :
                ans+=1
        return ans

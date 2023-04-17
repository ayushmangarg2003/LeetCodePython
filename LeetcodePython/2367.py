class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            for k in range(i,len(nums)):
                j=(nums[i]+nums[k])/2
                if j in nums and nums[k]-nums[i] == 2*diff:
                    count+=1
        return count

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        nums = [0] * (n+1)
        nums[1] = 1
        for i in range(2,len(nums)):
            if i%2==0:
                nums[i] = nums[int(i/2)]
            if i%2 !=0:
                nums[i] = nums[i//2] + nums[i//2 +1]
        return max(nums)

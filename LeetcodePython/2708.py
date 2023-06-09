class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        ans = 1
        if len(nums) == 1:
            return nums[0]
        if 0 in nums:
            while 0 in nums:
                nums.remove(0)
            if len(nums) == 1:
                return max(nums[0] , 0)
            if len(nums) == 0:
                return 0
        nums.append(1)
        for i in nums:
            ans*=i
        if ans<0:
            nums = sorted(nums)
            for i in range(len(nums)):
                if nums[i] > 0:
                    ans = ans//nums[i-1]
                    break
        return ans

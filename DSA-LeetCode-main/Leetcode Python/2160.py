class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        for i in str(num):
            nums.append(int(i))
        nums.sort()
        return nums[0]*10 + nums[1]*10 + nums[2]+nums[3]

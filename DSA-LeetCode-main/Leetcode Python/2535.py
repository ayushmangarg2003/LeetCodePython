class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if i >=10:
                temp = 0
                for j in str(i):
                    temp+=int(j)
                ans+= (i-temp)
        return ans

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        for k,v in Counter(nums).items():
            if v==1:
                ans+=k
        return ans

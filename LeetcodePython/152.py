class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        currmin , currmax = 1,1
        
        for n in nums:
            tmp1 = n*currmax
            tmp2 = n*currmin
            currmax = max(tmp1 , tmp2 , n)
            currmin = min(tmp1 , tmp2 , n)
            res = max(res , currmax , currmin)
        return res

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        for x in set(nums):
            if nums.count(x)> len(nums)/3:
                ans.append(x)
        return ans

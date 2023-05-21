class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(lambda x:str(x), nums))
        nums.sort(reverse=True, key= lambda x:x*10)
        return str(int(''.join(nums)))

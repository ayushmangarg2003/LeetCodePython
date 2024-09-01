class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        temp = []
        for i in nums:
            temp.append(int(str(i)[::-1]))
        return len(set(nums+temp))

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for i in nums:
            output+=[o + [i] for o in output]
        return output
        

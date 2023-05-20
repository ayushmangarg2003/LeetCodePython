class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        total = []
        if len(nums) == 1:
            return [nums[:]] 
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permuteUnique(nums)
            for perm in perms:
                perm.append(n)
                if perm not in total:
                    total.append(perm)
            nums.append(n)
        return total

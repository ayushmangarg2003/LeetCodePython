class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort()
        res = []
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                c = b+1
                d = len(nums)-1
                while c < d:
                    summ = nums[a]+nums[b]+nums[c]+nums[d]
                    ans = [nums[a], nums[b], nums[c], nums[d]]
                    if summ == target and ans not in res:
                        res.append(ans)
                    if summ > target:
                        d -= 1
                    else:
                        c += 1
                        while c < d and nums[c-1] == nums[c]:
                            c += 1
        return res                    
        

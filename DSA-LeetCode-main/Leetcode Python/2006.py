class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        temp = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]-nums[j] == k or nums[j]-nums[i] == k:
                    temp+=1
        return temp

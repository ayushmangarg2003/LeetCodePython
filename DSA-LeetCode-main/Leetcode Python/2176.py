class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        temp = 0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    temp+=1
        return temp

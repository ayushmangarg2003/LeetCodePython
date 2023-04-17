class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(1,len(nums),2):
            ans+=[nums[i]]*nums[i-1]
        return(ans)
